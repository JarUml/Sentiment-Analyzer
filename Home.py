import streamlit as st
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def main():

    st.title("Sentiment Analyzer")
    st.write("Welcome to the Sentiment Analyzer")

    # Sidebar Footer (Bottom)
    st.sidebar.write("© 2025 Sentiment Analyzer - All Rights Reserved")
    
if __name__ == "__main__":
    main()
