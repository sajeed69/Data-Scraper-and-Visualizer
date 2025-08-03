# Data Scraper and Visualizer

## Overview
**Data Scraper and Visualizer** is a Python-based project that allows users to input a keyword, then automatically scrapes relevant data from multiple online sources, processes it, and creates insightful visualizations. Additionally, it leverages OpenAI's GPT models to generate a natural language summary and insights based on the scraped data.

---

## Features
- **Keyword-based data scraping** from sources like Wikipedia (with support for dynamic websites using Playwright).
- **Data processing and analysis** using Pandas.
- **Interactive and static visualizations** with Matplotlib and Plotly.
- **AI-powered summaries and insights** using OpenAI GPT models.
- Simple **Streamlit-based web interface** for easy interaction.

---
<img width="957" height="433" alt="data_scraper-1" src="https://github.com/user-attachments/assets/1df80dad-442e-46bf-a6d7-8119bd0c1f19" />
<img width="959" height="321" alt="data_scraper-2" src="https://github.com/user-attachments/assets/e4f92440-75ac-4c7e-b573-f0ade9af5ad3" />
<img width="959" height="434" alt="data_scraper-4" src="https://github.com/user-attachments/assets/6521ec84-6ad4-4c01-b0fe-7dc3a901688a" />
<img width="938" height="373" alt="data_scraper-3" src="https://github.com/user-attachments/assets/c3bb2439-cadc-4dc0-9815-d493698c5137" />

## Getting Started

### Prerequisites
- Python 3.9 or higher
- OpenAI API key ([Get your key here](https://platform.openai.com/account/api-keys))
- Git

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/sajeed69/Data-Scraper-and-Visualizer.git
    cd Data-Scraper-and-Visualizer
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # macOS/Linux
    source venv/bin/activate
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    playwright install
    ```

4. Set your OpenAI API key as an environment variable:
    - On Windows (CMD):
      ```cmd
      set OPENAI_API_KEY=your_api_key_here
      ```
    - On macOS/Linux:
      ```bash
      export OPENAI_API_KEY=your_api_key_here
      ```

---

## Usage

### Run the Streamlit app:
```bash
streamlit run app.py
```

- Enter a keyword in the input box.
- View the generated visualizations and AI-powered insights on the page.

### Run from command line (optional):
```bash
python main.py
```
- Enter a keyword when prompted.
- View the output in terminal and charts in a pop-up window.

---

## Project Structure
```
data_scraper_visualizer/
├── app.py               # Streamlit UI application
├── main.py              # CLI application (optional)
├── scraper.py           # Web scraping logic
├── processor.py         # Data cleaning and processing
├── visualizer.py        # Plotting and visualization functions
├── insight_generator.py # OpenAI integration for summaries
├── requirements.txt     # Python dependencies
└── output/              # Folder for saved images and charts
```

---

## Dependencies
- `streamlit`
- `requests`
- `beautifulsoup4`
- `pandas`
- `matplotlib`
- `plotly`
- `openai`
- `playwright`

---

## Contributing
Contributions are welcome! Feel free to open issues or submit pull requests.

---

## License
This project is licensed under the MIT License.

---

## Contact
Created by MD Sajeed Ahmed  
Email: [sajeed726@hotmail.com]  

---

## Acknowledgments
- OpenAI for GPT models  
- Playwright for web scraping  
- Streamlit for easy app development  
