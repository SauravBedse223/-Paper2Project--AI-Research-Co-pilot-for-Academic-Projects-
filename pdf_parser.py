import streamlit as st
import fitz  # PyMuPDF library

def extract_text_from_pdf(uploaded_file):
    """
    Extracts text content from an uploaded PDF file.
    """
    try:
        # Open the PDF file directly from the uploaded file's in-memory buffer
        pdf_document = fitz.open(stream=uploaded_file.read(), filetype="pdf")

        full_text = ""
        for page_num in range(len(pdf_document)):
            page = pdf_document.load_page(page_num)
            full_text += page.get_text()

        return full_text
    except Exception as e:
        st.error(f"Error reading {uploaded_file.name}: {e}")
        return None