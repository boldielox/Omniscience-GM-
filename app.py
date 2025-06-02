import streamlit as st
import pandas as pd
import plotly.express as px
import openai

# --- Custom CSS for background and overlay ---
st.markdown(
    """
    <style>
    .stApp {
        background-image: url('https://pplx-res.cloudinary.com/image/upload/v1748805239/user_uploads/71937249/4b61bc3f-e625-4a1f-8dc3-8c3047d5b355/101.jpg');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    .main > div {
        background: rgba(0,0,0,0.7) !important;
        border-radius: 20px;
        padding: 2rem;
    }
    h1, h2, h3, h4, h5, h6, .stMarkdown, .stDataFrame, .stPlotlyChart {
        color: #fff !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Sidebar with logo and navigation ---
st.sidebar.image(
    "https://pplx-res.cloudinary.com/image/upload/v1748805239/user_uploads/71937249/4b61bc3f-e625-4a1f-8dc3-8c3047d5b355/101.jpg",
    width=120
)
st.sidebar.title("Omniscience")
page = st.sidebar.radio("Go to", ["Live Predictions", "Historical Analysis", "Model Insights", "AI Chat"])

# --- Example: Load your real model (replace with your own model loading code) ---
# import joblib
# model = joblib.load("your_model.pkl")

# --- Live Predictions Section ---
if page == "Live Predictions":
    st.title("👁️ Live Game Predictions")
    # Example DataFrame (replace with your real model/data)
    df = pd.DataFrame({
        "Minute": range(1, 91),
        "Home Win Probability": [0.5 + 0.3 * (i/90) for i in range(1, 91)],
        "Draw Probability": [0.3 - 0.1 * (i/90) for i in range(1, 91)],
        "Away Win Probability": [0.2 - 0.2 * (i/90) for i in range(1, 91)]
    })
    fig = px.line(
        df, x="Minute", y=["Home Win Probability", "Draw Probability", "Away Win Probability"],
        labels={"value": "Probability", "Minute": "Match Minute"},
        title="Win Probabilities Over Time"
    )
    st.plotly_chart(fig, use_container_width=True)
    st.success("Add your real-time model inference here!")

# --- Historical Analysis Section with File Upload ---
elif page == "Historical Analysis":
    st.title("📊 Historical Model Performance")
    uploaded = st.file_uploader("Upload results (CSV)", type="csv")
    if uploaded:
        hist_df = pd.read_csv(uploaded)
        st.dataframe(hist_df)
        numeric_cols = hist_df.select_dtypes(include=[float, int]).columns
        if len(numeric_cols) > 0:
            st.line_chart(hist_df[numeric_cols])
        else:
            st.info("No numeric columns to plot.")
    else:
        st.info("Upload and visualize your historical results here.")

# --- Model Insights Section with SHAP/Feature Importance Placeholder ---
elif page == "Model Insights":
    st.title("🧠 Model Insights and Feature Importance")
    st.info("Show SHAP values, feature importances, or model diagnostics here.")
    # Example: Placeholder for SHAP/feature importance plot
    # st.image("path/to/shap_plot.png")
    # Or use plotly/matplotlib for actual feature importances

# --- AI Chat Section: Option 2 Integration ---
elif page == "AI Chat":
    st.title("💬 Ask the Omniscient AI")
    user_q = st.text_input("Ask about a match, prediction, or model insight:")
    if user_q:
        # --- Replace this with your real model logic ---
        # For demonstration, we'll use a dummy prediction
        betting_recommendation = "Strong Buy on Team A, predicted win probability 78%."
        # Compose prompt for GPT/Gemini
        prompt = (
            f"User question: {user_q}\n"
            f"Omniscience betting model output: {betting_recommendation}\n"
            "Please explain the model's recommendation and reasoning in clear, helpful terms."
        )
        # Use OpenAI GPT (replace with Gemini if desired)
        openai.api_key = st.secrets["OPENAI_API_KEY"]
        with st.spinner("AI is thinking..."):
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt}]
            )
            ai_answer = response["choices"][0]["message"]["content"]
        st.success(ai_answer)

# --- Footer ---
st.markdown(
    '<div style="text-align:center; color: #bbb; margin-top: 2em;">'
    'Omniscience God Mode &copy; 2025</div>',
    unsafe_allow_html=True
)
