from report_generator import generate_pdf_report

# Download Report page
elif menu == "Download Report":
    st.header("📄 Download Nutrition Report")
    if "product_data" in st.session_state:
        data = st.session_state["product_data"]
        rating = analyze_nutrition(data)
        suggestion = get_ai_suggestion(data)

        if st.button("Generate PDF Report"):
            filepath = generate_pdf_report(data, rating, suggestion)
            st.success("✅ Report generated successfully!")
            with open(filepath, "rb") as f:
                st.download_button("📥 Download Report", f, file_name=os.path.basename(filepath))
    else:
        st.warning("Please analyze a product first.")
