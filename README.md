# AI-Powered Search & Recommendation Engine

A portfolio project inspired by modern e-commerce search systems. It combines text-based semantic-style search, relevance ranking and a lightweight personalization signal.

## Features
- Natural-language product search
- TF-IDF based text representation
- Cosine-similarity relevance scoring
- Product ranking
- User-history personalization signal
- Streamlit dashboard
- CSV-based product catalog
- Reproducible sample dataset

## Architecture

User Query -> Query Vectorization -> Similarity Search -> Ranking -> Personalization -> Recommendations

## Tech Stack

Python, Pandas, NumPy, Scikit-learn, TF-IDF, Cosine Similarity, Streamlit, Git/GitHub.

## Run

```bash
python -m venv venv
```

Windows:
```bash
venv\Scripts\activate
```

Install:
```bash
pip install -r requirements.txt
```

Generate sample data:
```bash
python generate_data.py
```

Run:
```bash
streamlit run app.py
```

Then upload `products.csv` and search for products.

## Interview Explanation

"I built an AI-powered search and recommendation engine for an e-commerce style use case. The system converts product information and the user's natural-language query into TF-IDF vectors and calculates cosine similarity to measure relevance. I then combine the relevance score with a lightweight user-history personalization signal to rank products. The application is built with Python and Streamlit, with Pandas and Scikit-learn for data processing and machine-learning components."

## Future Improvements

- Replace TF-IDF with transformer embeddings
- Add FAISS/vector database for large catalogs
- Add collaborative filtering
- Train a learning-to-rank model
- Add FastAPI backend
- Add A/B testing and offline recommendation metrics
