# app.py
import streamlit as st
from nutrition_analysis import analyze_nutrition
from ai_suggester import get_ai_suggestion
from qr_scanner import scan_qr_code
import pandas as pd
from report_generator import generate_pdf_report
import os

st.set_page_config(page_title="NutriCheck", layout="centered")

st.title("🥗 NutriCheck – AI Nutrition Analyzer")

# Sidebar navigation
menu = st.sidebar.radio("Navigate", ["Scan QR", "Manual Entry", "View Analysis", "Download Report"])

# Placeholder for product data
product_data = {}

# QR Scanner Page
if menu == "Scan QR":
    st.header("📷 Scan Food QR/Barcode")
    uploaded_image = st.file_uploader("Upload QR/Barcode Image", type=["jpg", "png", "jpeg"])
    if uploaded_image:
        code = scan_qr_code(uploaded_image)
        if code:
            st.success(f"Scanned Code: {code}")
            # (Later) Fetch data from DB using code
        else:
            st.error("No QR/Barcode detected.")

# Manual Entry Page
elif menu == "Manual Entry":
    st.header("📝 Enter Nutrition Data Manually")
    name = st.text_input("Product Name")
    calories = st.number_input("Calories (kcal)", 0, 1000)
    sugar = st.number_input("Sugar (g)", 0.0, 100.0)
    protein = st.number_input("Protein (g)", 0.0, 100.0)
    fat = st.number_input("Fat (g)", 0.0, 100.0)

    if st.button("Analyze"):
        product_data = {
            "Name": name,
            "Calories": calories,
            "Sugar": sugar,
            "Protein": protein,
            "Fat": fat
        }
        st.session_state["product_data"] = product_data
        st.success("Data saved! Go to 'View Analysis'")

# View Analysis Page
elif menu == "View Analysis":
    st.header("📊 Nutritional Analysis")
    if "product_data" in st.session_state:
        data = st.session_state["product_data"]
        st.write("### Product Info", pd.DataFrame([data]))
        rating = analyze_nutrition(data)
        st.success(f"🔎 Health Score: {rating}")
        suggestion = get_ai_suggestion(data)
        st.info(f"🤖 AI Suggestion: {suggestion}")
    else:
        st.warning("No data found. Please scan or enter manually first.")

# Report Download Page
elif menu == "Download Report":
    st.header("📄 Download Nutrition Report")
    st.write("Coming soon... (PDF generator)")
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
