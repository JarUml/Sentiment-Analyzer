import streamlit as st
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def read_upload(file) -> pd.DataFrame:
    try:
        if file.name.endswith('.csv'):
            return pd.read_csv(file)
        elif file.name.endswith('.xlsx'):
            return pd.read_excel(file)
        else:
            raise ValueError("File type not supported")
    except Exception as e:
        return str(e)

def filter_for_verbatims(df: pd.DataFrame) -> pd.DataFrame:
    for column in df.columns:
        if 'verbatim' in column.lower():
            return df[column]
        else:
            raise ValueError("No column containing 'verbatim' found in the DataFrame")

def sentiment_analysis_verbatims(verbatims: pd.Series) -> pd.DataFrame:
    analyzer = SentimentIntensityAnalyzer()
    sentiments = pd.DataFrame()
    for verbatim in verbatims:
        sentiment  = analyzer.polarity_scores(verbatim)
        sentiments.append(sentiment)
    return

st.title("Lexical Analysis")
st.write("Upload an excel file to perform a lexical sentiment analysis of you verbatim data")

st.write("Accepted file types: csv, excel")

uploaded_file = st.file_uploader("Choose a file", type=["csv, excel"])

if uploaded_file is not None:
    st.write("File uploaded successfully")
    
    st.write("Processing")
    
    # Placeholder for Loading Bar
    # Placeholder for Loading Bar

    try:
        uploaded_df = read_upload(uploaded_file)
        verbatims = filter_for_verbatims(uploaded_df)
        sentiments = sentiment_analysis_verbatims(verbatims)
        download_df = uploaded_df.append(sentiments)
        st.download_button(download_df)  # Display the DataFrame for demonstration
    except ValueError as e:
        st.error(f"Error: {e}")
