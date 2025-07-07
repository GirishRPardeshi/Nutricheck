# report_generator.py

from fpdf import FPDF
import os
from datetime import datetime

def generate_pdf_report(data, rating, suggestion, save_path="reports/generated_reports"):
    """
    Generates a PDF report from nutrition data, rating, and AI suggestion.
    Saves it inside reports/generated_reports/
    """
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    filename = f"{data['Name'].replace(' ', '_')}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
    filepath = os.path.join(save_path, filename)

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.set_fill_color(230, 230, 250)
    pdf.cell(200, 10, txt="NutriCheck – Nutrition Report", ln=True, align='C', fill=True)

    pdf.ln(10)
    pdf.cell(200, 10, txt=f"Product Name: {data['Name']}", ln=True)
    pdf.cell(200, 10, txt=f"Calories: {data['Calories']} kcal", ln=True)
    pdf.cell(200, 10, txt=f"Sugar: {data['Sugar']} g", ln=True)
    pdf.cell(200, 10, txt=f"Protein: {data['Protein']} g", ln=True)
    pdf.cell(200, 10, txt=f"Fat: {data['Fat']} g", ln=True)

    pdf.ln(5)
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(200, 10, txt=f"Health Rating: {rating}", ln=True)
    pdf.set_font("Arial", '', 12)
    pdf.multi_cell(0, 10, txt=f"AI Suggestion:\n{suggestion}")

    pdf.output(filepath)
    return filepath
