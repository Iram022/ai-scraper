# AI-Powered Web Scraper & Report Generator 

This project is an AI-powered Python application that understands natural language queries, scrapes data from e-commerce/travel websites using browser automation, and generates Excel reports with analytics.

## Features
- Local LLM parsing via `ollama`
- Browser automation using Playwright (MCP-style)
- Multi-site scraping (Amazon, Flipkart)
- Excel reports with filters and price charts


## Setup Instructions

### 1. Clone the Repository
git clone https://github.com/your_username/ai-scraper.git
cd AI-scraper

### 2. Install Dependencies

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
playwright install


### 3. Install and Run Ollama

Install Ollama from: https://ollama.com

Pull a model like OpenChat:
> ollama pull openchat

### 4. Running the project
python main.py

Then enter the query like:
Find me smartphones under ₹30,000
