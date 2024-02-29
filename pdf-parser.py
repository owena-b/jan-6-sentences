import camelot
import pandas as pd

src = 'table.pdf'

tables = camelot.read_pdf(src, strip_text='\n', pages='1')

headers = ['Defendant First Name', 'Defendant Last Name', 'Case Number', 'Offense', 'Government Recommendation',
           'Sentence Imposed']

#df = pd.DataFrame(columns=headers)
df = tables.df

#for table in tables:
#    temp = table.df.copy()
#    df = pd.concat([df, temp])

df.to_csv('sentences.csv')
