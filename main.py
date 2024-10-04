import streamlit as st
from scrape2 import (
    scrape_website, 
    split_dom_content, 
    clean_body_content, 
    extract_body_content
    )
from parse import parse_with_ollama

st.title("AI Web Scraper")
url = st.text_input("Enter a Website URL")
if st.button("Scrape Site"):
    if url:
        st.write("Scraping the website...")
        result = scrape_website(url)
        # st.text_area("Scraped HTML", result, height=300)
        # print(result)
        body_content = extract_body_content(result)
        cleaned_content = clean_body_content(body_content)
        # st.session_state.dom_content = cleaned_content
        st.session_state.dom_content = result

        with st.expander("View DOM Content"):
            # st.text_area("DOM Content", cleaned_content, height=300)
            st.text_area("DOM Content", result, height=300)
    else:
        st.write("Please enter a URL to scrape.")

if "dom_content" in st.session_state:
    parse_description = st.text_area("Describe what you want to parse")

    if st.button("Parse Content"):
        if parse_description:
            st.write("Parsing the content")

            dom_chunks = split_dom_content(st.session_state.dom_content)
            result = parse_with_ollama(dom_chunks, parse_description)
            st.write(result)
