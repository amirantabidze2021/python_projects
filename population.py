import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook
from openpyxl.styles import *
from openpyxl.worksheet.table import Table,TableStyleInfo

records=[]



r= requests.get('https://www.worldometers.info/world-population/population-by-country/')
c=r.text

soup=BeautifulSoup(c, 'html.parser')
data = soup.find('tbody')
rows = data.find_all('tr')

for index, row in enumerate(rows, 1):

	columns = row.find_all('td')
	
	country=columns[1].text
	population=int(columns[2].text.replace(',',''))
	percentage=columns[3].text

	item=[index,country,population,percentage]
	records.append(item)

records.insert(0, ['N','Countries', 'Population','Percentage'] )


workbook = Workbook()

fileName = 'population.xlsx'
workbook.save(fileName)

sheet=workbook['Sheet']
sheet.title='Population'
sheet = workbook['Population']

for item in records:
	sheet.append(item)

table=Table(displayName='Population_Data', ref = 'A1:D236')
style=TableStyleInfo(name = 'TableStyleMedium4', 
	                  showRowStripes=True, showColumnStripes=True )
table.tableStyleInfo = style

sheet.add_table(table)
font = Font(color='00FF0000', bold=True , italic=True)

for cell_no in range(2, 237):
	if sheet[f'C{cell_no}'].value < 5000000:
		sheet[f'C{cell_no}'].font=font


workbook.save(fileName)
workbook.close()