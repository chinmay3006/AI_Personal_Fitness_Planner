# 💪 AI-Powered Personal Fitness Planner

*Problem Statement: Personalized Workout & Diet Planner with AI

# 📌 Project Overview
This project addresses the need for personalized fitness guidance by using AI to generate custom workout plans. Unlike generic fitness apps, this tool considers the user's specific goals (Muscle Gain, Weight Loss, Strength) and target muscle groups to recommend tailored exercises.

# 🚀 Key Features
* Smart Recommendation System: Filters over 2,900 exercises from the "Mega Gym Dataset" to find the best match for the user.
* AI Motivation Coach: Integrates the **Hugging Face `distilgpt2` model** to generate unique, context-aware motivational quotes in real-time.
* Data Visualization: Automatically cleans raw data and presents a distribution of exercises using **Seaborn** graphs.
* Interactive Dashboard: Built with **Streamlit** for an easy-to-use web interface.

# 🛠️ Tech Stack
* Language: Python
* Platform: Google Colab
* Libraries: Pandas, Streamlit, Scikit-Learn, Transformers (Hugging Face)
* Visualization: Matplotlib, Seaborn

# 📸 Project Screenshots
(Note: These are the actual outputs from the project)**

# 1. Data Analysis & Distribution
Visualizing the dataset to understand exercise variety.*
![Graph](Output_1.png)

# 2. AI Dashboard & Recommendations
The final interface where users get their plan and AI advice.*
![Dashboard](Output_2.png)

## 💡 How to Run
Option 1: Google Colab (Recommended)
1. Open `AI_Fitness_Project.ipynb` in Google Colab.
2. Upload `megaGymDataset.csv`.
3. Run all cells to launch the app.

### Option 2: Local Execution
1. Install dependencies: `pip install streamlit pandas transformers`
2. Run the script:
   ```bash
   streamlit run app.py
