from flask import Flask, request, jsonify
import google.generativeai as genai
from serpapi import GoogleSearch

# Configure Gemini API
genai.configure(api_key="AIzaSyDiuTDSD33lLBuqgZyVfmtmmUtjO8PWoPA")

# Initialize Flask app
app = Flask(__name__)

# Function to extract key factual statements from text
def extract_facts(text):
    model = genai.GenerativeModel("gemini-1.5-pro-latest")
    prompt = f"Extract key factual statements from the following text:\n\n{text}\n\nReturn them as a numbered list."
    response = model.generate_content(prompt)
    return response.text  # Returns extracted facts

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
    
    sources = []
    for item in results.get("organic_results", []):
        if "snippet" in item:
            sources.append(item["snippet"])
    
    if not sources:
        sources.append("No relevant sources found.")
    
    return sources[:3]  # Get up to 3 sources

# Function to verify facts using Gemini + web search
def verify_fact(fact):
    sources = search_web(fact)  # Get web results
    source_texts = "\n\n".join(sources)  # Extract summaries

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

# API endpoint to process fact-checking
@app.route('/fact-check', methods=['POST'])
def fact_check():
    data = request.json
    text = data.get("text", "")

    if not text:
        return jsonify({"error": "No text provided"}), 400

    extracted_facts = extract_facts(text).split("\n")
    results = {}

    for fact in extracted_facts[:3]:  # Limit to 3 facts per request
        fact = fact.strip()
        if fact:
            check_result = verify_fact(fact)
            results[fact] = check_result

    return jsonify(results)

# Run the Flask app
if __name__ == '__main__':
    app.run(port=5000, debug=True)
