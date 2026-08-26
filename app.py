import streamlit as st
import pandas as pd
import numpy as np
from recommender import SearchRecommendationEngine

st.set_page_config(page_title="AI Search & Recommendation Engine", page_icon="🔎", layout="wide")

st.title("🔎 AI-Powered Search & Recommendation Engine")
st.caption("Semantic product search + personalized recommendations")

@st.cache_resource
def get_engine():
    return SearchRecommendationEngine()

engine=get_engine()

with st.sidebar:
    st.header("Dataset")
    uploaded=st.file_uploader("Upload product CSV", type=["csv"])
    if uploaded:
        df=pd.read_csv(uploaded)
        engine.load_data(df)
        st.success(f"{len(df):,} products loaded")

if engine.data is not None:
    st.subheader("🛍️ Product Search")
    query=st.text_input("Search products", placeholder="Example: affordable wireless headphones for travel")
    user_id=st.number_input("User ID", min_value=1, value=1, step=1)

    if st.button("Search & Recommend", type="primary") and query.strip():
        results=engine.recommend(query, int(user_id), top_k=10)
        st.subheader("Recommended Products")
        if results.empty:
            st.info("No matching products found.")
        else:
            for _, row in results.iterrows():
                with st.container(border=True):
                    st.markdown(f"### {row['product_name']}")
                    st.write(f"**Category:** {row.get('category','N/A')}  |  **Price:** ${row.get('price', 'N/A')}")
                    st.write(f"**Recommendation Score:** {row['recommendation_score']:.3f}")
                    st.write(row.get("description",""))

    with st.expander("Dataset Preview"):
        st.dataframe(engine.data.head(20), use_container_width=True)
else:
    st.info("Upload a product CSV from the sidebar to start.")

st.markdown("---")
st.caption("Portfolio project: semantic search, ranking and personalization using Python.")
