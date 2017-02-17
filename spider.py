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

class LykkeSpider():

	def readTxhasid(self, csv_path):
		'''
		The script to read txhasid from csv file 
		'''
		print "reading txhasid from csv file ..."
		df = pd.read_csv(csv_path)
		txhasidColumn = df['TxHashId']
		return txhasidColumn.tolist()

	def requestHTML(self, id):
		'''
		Crawl the fee information from Lykke
		'''
		content = urllib2.urlopen("https://www.coinprism.info/tx/"+id).read()
		parsed_html = BeautifulSoup(content,"lxml")
		table_soup = parsed_html.body.find('table', attrs={'class':'table table-rounded '})
		rows = table_soup.find_all("tr")
		for row in rows:
			cells = row.find_all("td")
			txt = cells[0].get_text()
			if txt== "Fee paid":
				#get the transaction fee
				print cells[1].get_text()

lykkeSpider = LykkeSpider()
txhasidlist = lykkeSpider.readTxhasid("trade_log_20160801_20161231.csv")
for l in txhasidlist:
	lykkeSpider.requestHTML(l)
