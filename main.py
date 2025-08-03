# main.py

from scraper import scrape_wikipedia
from processor import process_text
from visualizer import plot_word_freq
from insight_generator import get_insight

if __name__ == "__main__":
    keyword = input("Enter a keyword: ")
    text = scrape_wikipedia(keyword)
    freq = process_text(text)
    plot_word_freq(freq)
    print(get_insight(text))
