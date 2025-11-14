from reportlab.pdfgen import canvas

pdf = canvas.Canvas("mytext.pdf")


pdf.drawString(100, 750, "Hello, I am learning Python!")
pdf.drawString(100, 730, "This is my first PDF file!")

pdf.save()