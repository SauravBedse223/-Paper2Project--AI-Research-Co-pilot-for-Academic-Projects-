# 🚀 Paper2Project: AI Research Co-pilot

A multi-agent AI system built with Python and Streamlit that accelerates the academic research process for students.

**[Live Demo Link Here]** ---

## About The Project

This tool acts as an intelligent co-pilot for final-year engineering students, guiding them from the initial brainstorming phase to creating a detailed project plan. It leverages the Google Gemini API to provide insightful analysis and suggestions.

---

## Key Features

* **Domain Discovery:** Suggests novel project ideas based on a given domain (e.g., "AI in Healthcare").
* **Automated Paper Search:** Finds relevant starter research papers for any generated project idea.
* **In-Depth Paper Analysis:** Ingests user-uploaded PDFs to summarize content and identify unique research gaps.
* **Feasibility & Roadmap Generation:** Assesses a project idea's feasibility and automatically creates a detailed, week-by-week project roadmap.

---

## Tech Stack

* **Backend:** Python
* **Frontend:** Streamlit
* **AI Model:** Google Gemini API
* **Core Libraries:** PyMuPDF

---

## Setup and Installation

1.  Clone the repository:
    ```sh
    git clone [https://github.com/SauravBedse223/-Paper2Project--AI-Research-Co-pilot-for-Academic-Projects-.git](https://github.com/SauravBedse223/-Paper2Project--AI-Research-Co-pilot-for-Academic-Projects-.git)
    ```
2.  Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```
3.  Create a `.env` file and add your Google API key:
    ```
    GOOGLE_API_KEY="YOUR_API_KEY_HERE"
    ```
4.  Run the Streamlit app:
    ```sh
    streamlit run app.py
    ```
