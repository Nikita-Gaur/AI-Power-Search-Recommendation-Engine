import streamlit as st
import pandas as pd
import numpy as np
from recommender import SearchRecommendationEngine

# Page configuration
st.set_page_config(
    page_title="AI Search & Recommendation Engine",
    page_icon="🔎",
    layout="wide"
)

# Header
st.title("🔎 AI-Powered Search & Recommendation Engine")
st.caption("Semantic product search • Ranking • Personalized recommendations")

@st.cache_resource
def get_engine():
    return SearchRecommendationEngine()

engine = get_engine()

# Sidebar
with st.sidebar:
    st.header("📂 Dataset")

    uploaded = st.file_uploader(
        "Upload product CSV",
        type=["csv"]
    )

    if uploaded:
        df = pd.read_csv(uploaded)
        engine.load_data(df)

        st.success(f"✅ {len(df)} products loaded")

# Main application
if uploaded:
    st.subheader("🔍 Search Products")

    col1, col2 = st.columns([3, 1])

    with col1:
        query = st.text_input(
            "Enter your search query",
            placeholder="Example: wireless headphones"
        )

    with col2:
        user_id = st.number_input(
            "User ID",
            min_value=1,
            value=1,
            step=1
        )

    if st.button("🚀 Search & Recommend", type="primary"):
        if query.strip():

            with st.spinner("Finding relevant products..."):
                results = engine.recommend(
                    query,
                    int(user_id),
                    top_k=10
                )

            st.subheader("✨ Recommended Products")

            if results.empty:
                st.info("No matching products found.")

            else:
                for _, row in results.iterrows():

                    with st.container(border=True):
                        st.markdown(
                            f"### 🛍️ {row['product_name']}"
                        )

                        col1, col2, col3 = st.columns(3)

                        with col1:
                            st.write(
                                f"**Category:** "
                                f"{row.get('category', 'N/A')}"
                            )

                        with col2:
                            st.write(
                                f"**Price:** "
                                f"${row.get('price', 'N/A')}"
                            )

                        with col3:
                            st.write(
                                f"**Recommendation Score:** "
                                f"{row['recommendation_score']:.3f}"
                            )

                        st.write(
                            row.get("description", "")
                        )

    with st.expander("📊 Dataset Preview"):
        st.dataframe(
            engine.data.head(20),
            use_container_width=True
        )

else:
    st.info("👈 Upload a product CSV from the sidebar to get started.")

st.divider()
st.caption(
    "Portfolio project: semantic search, ranking and personalization using Python."
)
