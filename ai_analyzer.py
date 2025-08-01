import os
import google.generativeai as genai
from dotenv import load_dotenv
import json

# Load environment variables from .env file
load_dotenv()

def get_ai_analysis(paper_text: str) -> dict:
    """
    Analyzes paper text and returns a structured dictionary (JSON).
    """
    # ... (code for this function remains the same)
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        return {"error": "GOOGLE_API_KEY not found."}

    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-1.5-flash')
        prompt = f"""
        You are a highly skilled AI research assistant. Analyze the provided research paper text.
        Your response MUST be a valid JSON object with three keys: "summary", "research_gap", and "project_idea".
        1.  "summary": A concise summary of the paper's core problem, methodology, and findings.
        2.  "research_gap": A single, clear research gap identified from the paper.
        3.  "project_idea": A specific project idea for a final-year engineering student to address this gap.
        Do not include any text or formatting outside of the JSON object.
        Here is the text from the research paper:
        ---
        {paper_text}
        ---
        """
        response = model.generate_content(prompt)
        json_string = response.text.strip().replace("```json", "").replace("```", "")
        analysis_dict = json.loads(json_string)
        return analysis_dict
    except Exception as e:
        return {"error": f"An error occurred during AI analysis or JSON parsing: {e}"}

def get_feasibility_and_roadmap(project_idea: str) -> dict:
    """
    Generates a feasibility analysis and a project roadmap using the Gemini AI model.
    """
    # ... (code for this function remains the same)
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        return {"error": "GOOGLE_API_KEY not found."}

    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-1.5-flash')
        prompt = f"""
        You are an expert project guide for final-year engineering students.
        Analyze the following project idea and provide a feasibility analysis and a detailed project roadmap.
        Your response MUST be a valid JSON object with two keys: "feasibility" and "roadmap".
        1.  "feasibility": An object containing a "score" (Low, Medium, or High) and a "justification" (a brief explanation).
        2.  "roadmap": A detailed, week-by-week project plan formatted as a markdown string. The plan should be structured into logical phases.
        Do not include any text or formatting outside of the main JSON object.
        Project Idea:
        ---
        {project_idea}
        ---
        """
        response = model.generate_content(prompt)
        json_string = response.text.strip().replace("```json", "").replace("```", "")
        analysis_dict = json.loads(json_string)
        return analysis_dict
    except Exception as e:
        return {"error": f"An error occurred during Roadmap generation: {e}"}


def get_project_ideas(domain: str) -> list:
    """
    Generates a list of project ideas for a given domain using the Gemini AI model.
    """
    # ... (code for this function remains the same)
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        return [{"error": "GOOGLE_API_KEY not found."}]

    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-1.5-flash')
        prompt = f"""
        You are an expert project guide for final-year engineering students in India.
        Given the domain "{domain}", generate a list of 3 innovative and feasible project ideas.
        Your response MUST be a valid JSON object containing a single key "project_ideas", which is a list of objects.
        Each object in the list must have two keys: "title" and "description".
        - "title": A concise and catchy project title.
        - "description": A short, 2-3 sentence description of the project.
        Do not include any text or formatting outside of the main JSON object.
        """
        response = model.generate_content(prompt)
        json_string = response.text.strip().replace("```json", "").replace("```", "")
        analysis_dict = json.loads(json_string)
        return analysis_dict.get("project_ideas", [])
    except Exception as e:
        return [{"error": f"An error occurred during idea generation: {e}"}]


def find_academic_papers(query: str) -> dict:
    """
    Simulates a powerful academic search across multiple sources.
    Returns a dictionary of results categorized by source.
    """
    print(f"Performing a categorized academic search for: '{query}'")
    # This simulates calling a search tool multiple times for different sources.
    # The structure of this mocked data matches your HTML prototype.
    mock_results = {
        "Google Scholar": [
            {"title": "Attention Is All You Need", "url": "https://scholar.google.com/scholar?q=attention+is+all+you+need", "snippet": "A new simple network architecture, the Transformer, based solely on attention mechanisms..."},
            {"title": "BERT: Pre-training of Deep Bidirectional Transformers", "url": "https://scholar.google.com/scholar?q=bert+pre+training", "snippet": "BERT stands for Bidirectional Encoder Representations from Transformers..."}
        ],
        "arXiv": [
            {"title": "Generative Adversarial Nets", "url": "https://arxiv.org/abs/1406.2661", "snippet": "We propose a new framework for estimating generative models via an adversarial process..."}
        ]
    }
    return mock_results