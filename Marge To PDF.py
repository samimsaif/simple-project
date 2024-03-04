from PyPDF2 import PdfMerger

AllPDF = ["A1.pdf", "A2.pdf"]

marger = PdfMerger()
for PDF in AllPDF:
    marger.append(PDF)

marger.write("saif.pdf")
marger.close()