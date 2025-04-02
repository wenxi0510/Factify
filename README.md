# Factify – AI-Powered Fake News Detection

Factify is an AI-driven fact-checking tool that helps users verify the authenticity of news claims using Google Gemini API and web search results. The system consists of a Flask-based backend and a web-based front end, along with a Telegram bot integration for seamless access.

## Features
- **AI-Powered Fact-Checking**: Utilizes Google Gemini API to analyze and verify news claims.
- **Web Search Integration**: Fetches top search results for cross-referencing facts.
- **Flask-Based API**: Handles fact extraction and verification requests.
- **Interactive Web Interface**: Allows users to input claims and receive verification results.
- **Telegram Bot Support**: Enables quick fact-checking through Telegram.

## Tech Stack
- **Backend**: Flask, Python, Google Gemini API, SERPAPI
- **Frontend**: HTML, CSS, Bootstrap, JavaScript 
- **Deployment**: Flask (for API), Telegram Bot 


## Installation & Setup

### 1. Clone the Repository
```sh
git clone https://github.com/your-username/factify.git
cd factify
```

### 2. Install Dependencies
Ensure you have Python installed, then install the required libraries:
```sh
pip install flask flask-cors google-generativeai serpapi requests
```

### 3. Set Up API Keys
- **Google Gemini API**: Obtain an API key from Google AI and replace the placeholder in `app.py`.
- **SERPAPI**: Get an API key from [SerpAPI](https://serpapi.com/) and update the `search_web` function in `app.py`.
- **Telegram Bot** (Optional): Create a bot via `@BotFather` and store the API token if using the Telegram integration.

### 4. Run the Application
#### Open two terminals:
- **Terminal 1:** Run the backend API
```sh
python app.py
```
- **Terminal 2:** Run the Telegram bot (if applicable)
```sh
python telegram_bot.py
```

### 5. Access the Web Interface
Open `index.html` in a browser, enter a claim, and click “Check Now” to get results.

## Usage
- **Web App**: Users enter a news claim, and the system extracts key facts, searches the web, and provides fact-checking results.
- **Telegram Bot**: Users send claims to the bot, and it responds with verification results.

## Future Enhancements
- Integrate with more fact-checking databases.
- Improve NLP models for higher accuracy.
- Expand to other messaging platforms like WhatsApp.

##Contributors
- Chiang Wen Xi 
- Amelyn Siew
- Clarabelle Chua 
- Xinuo Zhu





