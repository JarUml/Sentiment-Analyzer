# Sentiment-Analyzer

This web app, built with Python and Streamlit, enables customer experience management teams to automate sentiment analysis of verbatim feedback using multiple approaches.

## Features

- **Automated Sentiment Analysis:** Analyze textual feedback efficiently.
- **Multiple Analysis Methods:** Compare rule-based and AI-powered sentiment classification.
- **User-Friendly Interface:** Simple and intuitive Streamlit UI.

## Sentiment Analysis Methods

### Rule-Based Lexical Analysis

This method uses libraries like **VADER (vaderSentiment)** and **TextBlob** for sentiment classification. These libraries rely on predefined rules and lexicons, offering a fast, lightweight way to gauge sentiment. While effective for basic analysis, they may struggle with nuanced language, sarcasm, or domain-specific contexts.

### LLM-Based Sentiment Analysis

Large Language Models (LLMs), such as **ChatGPT**, provide a more nuanced and context-aware sentiment analysis. Unlike rule-based methods, LLMs understand complex expressions, sarcasm, and industry-specific jargon. However, they require significantly more computational resources, making them costlier compared to traditional approaches.

## Installation & Usage

### Prerequisites

- Python 3.x
- Streamlit
- Required NLP libraries (`vaderSentiment`, `TextBlob`, OpenAI API for LLM-based analysis)

### Installation

```sh
pip install streamlit vaderSentiment textblob openai
