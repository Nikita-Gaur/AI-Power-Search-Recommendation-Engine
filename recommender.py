import re
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class SearchRecommendationEngine:
    def __init__(self):
        self.data=None
        self.vectorizer=None
        self.matrix=None
        self.user_history={}

    def load_data(self, df):
        df=df.copy()
        required=["product_name","description","category","price"]
        for col in required:
            if col not in df.columns:
                df[col]="" if col != "price" else 0
        df["search_text"]=(
            df["product_name"].fillna("").astype(str)+" "+
            df["description"].fillna("").astype(str)+" "+
            df["category"].fillna("").astype(str)
        )
        self.data=df.reset_index(drop=True)
        self.vectorizer=TfidfVectorizer(stop_words="english", ngram_range=(1,2))
        self.matrix=self.vectorizer.fit_transform(self.data["search_text"])

        if "user_id" in df.columns and "product_name" in df.columns:
            for uid, group in df.groupby("user_id"):
                self.user_history[int(uid)]=set(group["product_name"].astype(str).str.lower())

    def _query_scores(self, query):
        q=self.vectorizer.transform([query])
        return cosine_similarity(q,self.matrix).ravel()

    def recommend(self, query, user_id, top_k=10):
        scores=self._query_scores(query)
        result=self.data.copy()
        result["search_score"]=scores

        history=self.user_history.get(user_id,set())
        result["personalization_score"]=result["product_name"].astype(str).str.lower().apply(
            lambda x: 0.10 if x in history else 0.0
        )

        # Weighted ranking: relevance + small personalization signal.
        result["recommendation_score"]=(
            0.90*result["search_score"]+0.10*result["personalization_score"]
        )
        result=result.sort_values("recommendation_score",ascending=False).head(top_k)
        return result
