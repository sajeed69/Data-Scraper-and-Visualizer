# processor.py

import pandas as pd

def process_text(text):
    words = text.lower().split()
    df = pd.DataFrame(words, columns=["word"])
    return df["word"].value_counts().head(20)
