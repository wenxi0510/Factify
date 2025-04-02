from flask import Flask, request, jsonify
import google.generativeai as genai
from serpapi import GoogleSearch
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Configure Gemini API
genai.configure(api_key="AIzaSyDiuTDSD33lLBuqgZyVfmtmmUtjO8PWoPA")

# Function to extract key factual statements from text
def extract_facts(text):
    model = genai.GenerativeModel("gemini-1.5-pro-latest")
    prompt = f"Extract key factual statements from the following text:\n\n{text}\n\nReturn them as a numbered list."
    response = model.generate_content(prompt)
    return response.text

# Function to search the web for fact-checking
def search_web(query):
    params = {
        "q": query,
        "hl": "en",
        "gl": "us",
        "api_key": "8e47e68c2c7c6b68517c7d5be6243b84c3bf3b2ce203761eb8a2115fdb0e4e46"
    }
    search = GoogleSearch(params)
    results = search.get_dict()
    return results.get("organic_results", [])[:3]  # Get top 3 search results

# Function to verify facts using Gemini + web search
def verify_fact(fact):
    sources = search_web(fact)  # Get web results
    source_texts = "\n\n".join([s["snippet"] for s in sources])  # Extract summaries

    model = genai.GenerativeModel("gemini-1.5-pro-latest")
    prompt = f"""
    Compare the following fact with the provided sources and determine if it is true, misleading, or false.

    Fact: "{fact}"

    Sources:
    {source_texts}

    Provide a fact-checking report with a True/False/Misleading label and a short explanation.
    """
    response = model.generate_content(prompt)
    return response.text

# API endpoint to handle fact-checking
@app.route('/check-fact', methods=['POST'])
def check_fact():
    data = request.json
    claim = data.get("claim")
    if not claim:
        return jsonify({"error": "Claim is required"}), 400

    # Extract facts and verify
    extracted_facts = extract_facts(claim).split("\n")
    results = {}
    for fact in extracted_facts:
        fact = fact.strip()
        if fact:
            check_result = verify_fact(fact)
            results[fact] = check_result

    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
