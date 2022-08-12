import PyPDF2
 
merger =PyPDF2.PdfFileMerger()
file_names=["Fast_medicine.pdf","Doc2.pdf"]
for file_name in file_names:
    merger.append(file_name) 

merger.write("Join.pdf")
