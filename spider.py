'''
The file to extract trade log data from lykke
Author: Jinhua Wang 
University of Toronto
Feburary, 2017
MIT License

Copyright (c) 2017 Jinhua Wang

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

import pandas as pd 
from bs4 import BeautifulSoup
import urllib2
import csv 
import datetime

class LykkeSpider():

	totalCount = 0

	def readTxhasid(self, csv_path):
		'''
		The script to read txhasid from csv file 
		'''
		print "reading txhasid from csv file ..."
		df = pd.read_csv(csv_path)
		txhasidColumn = df['TxHashId']
		self.totalCount = df['TxHashId'].count()
		print "There are total "+ str(self.totalCount) +" records ..."
		return txhasidColumn.tolist()

	def requestHTML(self, id):
		'''
		Crawl the fee information from Lykke
		'''
		self.totalCount -= 1
		print str(self.totalCount) + " remaining ..."
		a = datetime.datetime.now()
		content = urllib2.urlopen("https://www.coinprism.info/tx/"+id).read()
		parsed_html = BeautifulSoup(content,"lxml")
		table_soup = parsed_html.body.find('table', attrs={'class':'table table-rounded '})
		rows = table_soup.find_all("tr")
		for row in rows:
			cells = row.find_all("td")
			txt = cells[0].get_text()
			if txt== "Fee paid":
				#get the transaction fee
				#print cells[1].get_text()
				b = datetime.datetime.now()
				#print ((b-a).total_seconds())
				sec_remaining = int(float(self.totalCount)*float((b-a).total_seconds()))
				print(str(sec_remaining) + " seconds remaining ...")
				return cells[1].get_text()

def isNaN(num):
	'''
	Util to check if the numebr if nan
	'''
	return str(num) == str(1e400*0)

result = []
result.append(['TxHashId', 'Fee'])
lykkeSpider = LykkeSpider()
txhasidlist = lykkeSpider.readTxhasid("trade_log_20160801_20161231.csv")
for l in txhasidlist:
	if l is not None and isNaN(l) is False:
		fee = lykkeSpider.requestHTML(l)
		fields = [l, fee]
		result.append(fields)
	elif isNaN(l) is True:
		print "skipping" + str(l)

with open("fee.csv",'wb') as resultFile:
    wr = csv.writer(resultFile, dialect='excel')
    wr.writerows(result)