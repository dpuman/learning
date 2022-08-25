import PyPDF2
with open("./Fast_medicine.pdf", "rb") as File:
    reader = PyPDF2.PdfFileReader(File)
    print(reader.numPages)
    page = reader.getPage(0)
    # page.rotateClockwise(90)
    page.rotateCounterClockwise(90)
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)
    with open("Doc2.pdf", "wb") as output:
        writer.write(output)
