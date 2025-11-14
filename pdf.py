from  PyPDF2  import PdfMerger 
mypdf = ["hello.pdf","hi.pdf"]
merger = PdfMerger()
for x in mypdf:
    merger.append(x)
merger.write("all.pdf")
merger.close()