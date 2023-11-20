from fpdf import FPDF
import pandas as pd

df = pd.read_csv("topics.csv")

pdf = FPDF(orientation='p', unit='mm', format='a4')
pdf.set_auto_page_break(auto=False, margin=0)

pdf.set_font(family='Times', style='B', size=24)
pdf.set_text_color(100, 100, 100)

for index, row in df.iterrows():
    # set header
    pdf.set_font(family='Times', style='B', size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.add_page()
    pdf.cell(w=0, h=12, align='L', ln=1, txt=row['Topic'])
    pdf.line(10, 22, 200, 22)

    # set footer
    pdf.ln(265)
    pdf.set_font(family='Times', style='I', size=12)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=12, align='R', ln=1, txt=row['Topic'])

    for i in range(0, row['Pages'] - 1):
        pdf.add_page()
        pdf.ln(277)
        pdf.set_font(family='Times', style='I', size=12)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=12, align='R', ln=1, txt=row['Topic'])

pdf.output("Python_pdf.pdf")
