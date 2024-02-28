import camelot

# extract all the tables in the PDF file
tables = camelot.read_pdf("table.pdf")  # address of file location

# print the first table as Pandas DataFrame
print(tables[0].df)
