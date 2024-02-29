import camelot
import csv

src = 'table.pdf'

tables = camelot.read_pdf(src, strip_text='\n', pages='1-10')

headers = ['Defendant First Name', 'Defendant Last Name', 'Case Number', 'Offense', 'Government Recommendation',
           'Sentence Imposed']

bigList = []

for table in tables:
    temp = table.df.values.tolist()
    bigList.append(temp)

print(bigList)

with open('sentences.csv', 'w', newline='', encoding='utf-8') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(headers)

    for table in bigList:
        for cell in table[1:]:
            if ', ' in cell[0]:
                split_str = cell[0].split(', ')
                cell[0] = split_str[1]
                cell.insert(1, split_str[0])
            else:
                cell.insert(1, '')
        writer.writerows(table[1:])

    print("Wrote sentences.csv")
