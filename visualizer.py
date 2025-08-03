# visualizer.py

import matplotlib.pyplot as plt
import plotly.express as px

def plot_word_freq(word_counts):
    word_counts.plot(kind='bar', figsize=(10,5))
    plt.title("Top Keyword Frequencies")
    plt.xlabel("Words")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig("output/word_freq.png")
    plt.show()

def plot_interactive(word_counts):
    fig = px.bar(x=word_counts.index, y=word_counts.values,
                 labels={'x':'Word', 'y':'Count'},
                 title="Top Word Frequencies")
    fig.show()
