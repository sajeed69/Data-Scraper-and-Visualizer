# app.py

import streamlit as st
from scraper import scrape_wikipedia
from processor import process_text
from visualizer import plot_word_freq, plot_interactive
from insight_generator import get_insight
from PIL import Image

# Page config
st.set_page_config(
    page_title="🔍 Data Scraper & Visualizer",
    layout="wide",
    page_icon="📊",
)

# Custom styling
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .block-container {
        padding: 2rem 2rem;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
    }
    .stTextInput>div>div>input {
        background-color: #ffffff;
    }
    .section-title {
        font-size: 24px;
        font-weight: 600;
        margin-top: 40px;
        color: #333333;
    }
    </style>
""", unsafe_allow_html=True)

# Title and banner
st.title("📊 Data Scraper and Insight Visualizer")
st.markdown("Turn any keyword into visual summaries and insights using scraping, data analysis, and AI.")
st.markdown("---")

# Input section
with st.container():
    st.markdown('<div class="section-title">🔍 Enter Keyword</div>', unsafe_allow_html=True)
    keyword = st.text_input("Type a keyword (e.g., Climate Change, AI in Healthcare)", max_chars=50)

# Process if keyword entered
if keyword:
    st.markdown("---")
    
    with st.container():
        st.markdown('<div class="section-title">📥 Scraped Data Summary</div>', unsafe_allow_html=True)
        text_data = scrape_wikipedia(keyword)
        st.text_area("Raw Summary (Wikipedia)", value=text_data[:1500], height=200)

    with st.container():
        st.markdown('<div class="section-title">📊 Word Frequency Visualization</div>', unsafe_allow_html=True)
        word_freq = process_text(text_data)

        col1, col2 = st.columns([1, 1])
        with col1:
            st.pyplot(plot_word_freq(word_freq))  # Static
        with col2:
            plot_interactive(word_freq)  # Interactive

    with st.container():
        st.markdown('<div class="section-title">🧠 AI-Generated Insights</div>', unsafe_allow_html=True)
        with st.spinner("Generating insights from OpenAI..."):
            insights = get_insight(text_data)
        st.success("Insight Generated!")
        st.write(insights)
