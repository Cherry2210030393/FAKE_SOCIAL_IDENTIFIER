import streamlit as st
from utils.scraper import fetch_profile_data
from utils.image_check import compare_images
from utils.nlp_analysis import analyze_bio

st.title("Fake Social Media Account Identifier")

profile_url = st.text_input("Enter Social Media Profile URL")
real_image_url = st.text_input("Enter Official Image URL (Optional)")

if st.button("Analyze"):
    with st.spinner("Fetching and analyzing profile..."):
        bio, profile_image_url = fetch_profile_data(profile_url)
        st.subheader("Profile Bio")
        st.write(bio)

        flagged = analyze_bio(bio)
        if flagged:
            st.warning("Bio analysis: ⚠️ Possible impersonation or fake bio")

        if real_image_url:
            similarity_score = compare_images(profile_image_url, real_image_url)
            st.write(f"Image Similarity Score: {similarity_score:.2f}")
            if similarity_score > 0.9:
                st.warning("⚠️ Profile image likely copied from official account.")
            else:
                st.success("✅ Profile image seems unique.")
        else:
            st.info("No reference image provided.")