import streamlit as st
from pdf_parser import extract_text_from_pdf
from ai_analyzer import get_ai_analysis, get_feasibility_and_roadmap , get_project_ideas , find_academic_papers

# --- Page Configuration ---
st.set_page_config(page_title="AI Research Co-pilot", layout="wide")

# --- Initialize session state ---
if 'analysis_results' not in st.session_state:
    st.session_state.analysis_results = {}

# --- App Title ---
st.title("AI Research Co-pilot 🚀")

# --- Create Tabs for Different Features ---
tab1, tab2 = st.tabs(["💡 Suggest Project Ideas", "📄 Analyze My Papers"])

# --- TAB 1: Suggest Project Ideas (New Feature) ---
# In app.py, replace the existing "with tab1:" block with this

# In app.py, replace the existing "with tab1:" block

with tab1:
    st.header("Explore a Domain to Get Project Ideas")

    if 'project_ideas' not in st.session_state:
        st.session_state.project_ideas = []

    domain_input = st.text_input(
        "Enter a domain (e.g., 'EV Technology', 'Healthcare AI')",
        key="domain_input"
    )

    if st.button("Generate Ideas", key="generate_ideas_button"):
        if domain_input:
            with st.spinner(f"Brainstorming ideas for {domain_input}..."):
                st.session_state.project_ideas = get_project_ideas(domain_input)
        else:
            st.warning("Please enter a domain to generate ideas.")
            st.session_state.project_ideas = []

    if st.session_state.project_ideas:
        st.subheader("Here are some project ideas for you:")
        for i, idea in enumerate(st.session_state.project_ideas):
            if "error" in idea:
                st.error(idea["error"]); break

            with st.container(border=True):
                st.write(f"**{idea.get('title')}**")
                st.write(idea.get('description'))

                button_key = f"find_papers_{i}"
                if st.button("Find Key Research Papers", key=button_key):
                    with st.spinner("Searching academic databases..."):
                        # Call the new, powerful search function
                        categorized_papers = find_academic_papers(idea.get('title'))
                        # Store results in session state to persist them
                        idea['categorized_papers'] = categorized_papers
                
                # Display the categorized papers if they exist in the session state
                if 'categorized_papers' in idea:
                    st.write("**Suggested Starting Papers:**")
                    for source, papers_list in idea['categorized_papers'].items():
                        st.subheader(f"Results from {source}")
                        for paper in papers_list:
                            st.markdown(f"**[{paper['title']}]({paper['url']})**")
                            st.caption(paper['snippet'])
                        st.divider()

# --- TAB 2: Analyze My Papers (Existing Feature) ---
with tab2:
    st.header("Upload Your Papers for Analysis")
    
    # All our existing code for uploading and analyzing PDFs goes here.
    uploaded_files = st.file_uploader(
        "Choose your research papers (PDFs)",
        type="pdf",
        accept_multiple_files=True,
        key="file_uploader" # Add a key to make it unique
    )

    if uploaded_files:
        if st.button("Analyze Papers"):
            st.session_state.analysis_results = {}
            with st.spinner('Reading papers and consulting the AI... Please wait.'):
                for file in uploaded_files:
                    extracted_text = extract_text_from_pdf(file)
                    if extracted_text:
                        analysis_result = get_ai_analysis(extracted_text)
                        st.session_state.analysis_results[file.name] = analysis_result
                    else:
                        st.session_state.analysis_results[file.name] = {"error": f"Could not extract text from {file.name}"}
            st.success("Initial analysis complete!")

    if st.session_state.analysis_results:
        for file_name, result in st.session_state.analysis_results.items():
            st.markdown(f"---")
            st.write(f"**Results for: {file_name}**")
            
            if "error" in result:
                st.error(result["error"])
            else:
                st.subheader("📄 Paper Summary")
                st.write(result.get("summary", "Not available."))
                
                st.subheader("💡 Research Gap & Project Idea")
                st.table({
                    "Category": ["Identified Research Gap", "Proposed Project Idea"],
                    "Details": [result.get("research_gap"), result.get("project_idea")]
                })

                button_key = f"roadmap_button_{file_name}"
                if st.button(f"Analyze Feasibility & Create Roadmap", key=button_key):
                    project_idea = result.get('project_idea')
                    if project_idea:
                        with st.spinner("Assessing feasibility and building your project plan..."):
                            roadmap_result = get_feasibility_and_roadmap(project_idea)
                            
                            if "error" in roadmap_result:
                                st.error(roadmap_result["error"])
                            else:
                                st.subheader("✅ Feasibility Analysis")
                                feasibility = roadmap_result.get("feasibility", {})
                                st.metric(label="Feasibility Score", value=feasibility.get("score", "N/A"))
                                st.write(f"**Justification:** {feasibility.get('justification', 'Not available.')}")

                                st.subheader("🗺️ Your Project Roadmap")
                                st.markdown(roadmap_result.get("roadmap", "Roadmap could not be generated."))