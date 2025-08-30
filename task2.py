import pandas as pd
from fpdf import FPDF


data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Score': [85, 90, 78]}
df = pd.DataFrame(data)

average_score = df['Score'].mean()

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="Student Report", ln=True, align='C')
pdf.cell(200, 10, txt=f"Average Score: {average_score:.2f}", ln=True)
for index, row in df.iterrows():
    pdf.cell(200, 10, txt=f"{row['Name']}: {row['Score']}", ln=True)

pdf.output("report.pdf")
print("PDF Report Generated Successfully!")