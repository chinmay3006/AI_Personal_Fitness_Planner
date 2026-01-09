import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from transformers import pipeline

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="AI Fitness Planner", page_icon="💪", layout="wide")

# --- LOAD DATA (Cached so it runs fast) ---
@st.cache_data
def load_data():
    try:
        # Ensure 'megaGymDataset.csv' is in your GitHub repository
        df = pd.read_csv("megaGymDataset.csv")
        df.dropna(inplace=True) # Clean null values
        return df
    except FileNotFoundError:
        return None

# --- LOAD AI MODEL (Cached) ---
@st.cache_resource
def load_model():
    return pipeline('text-generation', model='distilgpt2')

# Load everything
df = load_data()
ai_generator = load_model()

# --- MAIN APP UI ---
st.title("💪 AI-Powered Personal Fitness Planner")
st.markdown("### Project: Kaggle Data Analysis + Hugging Face AI")

# --- SECTION 1: DATA ANALYSIS ---
if df is not None:
    with st.expander("📊 View Data Analysis Report (Click to Open)", expanded=False):
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.write("### Cleaned Data Preview")
            st.write(f"Total Exercises: {len(df)}")
            st.dataframe(df.head(10)) # Fixed: Replaces display()

        with col2:
            st.write("### Top Target Body Parts")
            # Create the graph
            fig, ax = plt.subplots(figsize=(6, 4))
            sns.countplot(y='BodyPart', data=df, order=df['BodyPart'].value_counts().index[:7], palette='magma', ax=ax)
            st.pyplot(fig) # Fixed: Shows graph in Streamlit
else:
    st.error("❌ Error: 'megaGymDataset.csv' not found. Please upload it to your GitHub repository.")
    st.stop()

st.markdown("---")

# --- SECTION 2: AI COACH & FILTER ---
st.header("🤖 Your Personal AI Coach")

# Sidebar for User Input
st.sidebar.header("User Settings")
goal = st.sidebar.selectbox("Select Your Goal", ["Muscle Gain", "Weight Loss", "Strength", "Endurance"])
target_part = st.sidebar.selectbox("Select Target Muscle", df['BodyPart'].unique())

col_left, col_right = st.columns(2)

# Left Column: Exercise Table
with col_left:
    st.subheader(f"Exercises for: {target_part}")
    
    # Filter Logic
    filtered_data = df[df['BodyPart'] == target_part]
    
    if not filtered_data.empty:
        # Show 5 random exercises
        sample_size = min(5, len(filtered_data))
        st.table(filtered_data.sample(sample_size)[['Title', 'Type', 'Equipment']])
    else:
        st.warning("No exercises found for this body part.")

# Right Column: AI Motivation
with col_right:
    st.subheader("🧠 AI Motivation Generator")
    st.write(f"Goal: **{goal}**")
    
    if st.button("Generate AI Advice"):
        with st.spinner("AI is thinking..."):
            # Prompt logic
            prompt = f"To achieve {goal}, the most important mindset is"
            try:
                # Generate text
                res = ai_generator(prompt, max_length=50, num_return_sequences=1)
                quote = res[0]['generated_text']
                st.success(f"💡 **AI says:**\n\n'{quote}'")
            except Exception as e:
                st.error(f"AI Error: {e}")
