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
import scrapy as sp

class LykkeSpider():

	def readTxhasid(csv_path):
		'''
		The script to read txhasid from csv file 
		'''
		print "reading txhasid from cav file ..."
		df = pd.read_csv(csv_path)
		txhasidColumn = df['TxHashId']
		return txhasidColumn.tolist()

	def requestHTML(self):
		'''
		Crawl the Fee information from Lykke
		'''
		sp.Request(url="https://www.coinprism.info/tx/eae0316801df957138e97ab8ff7524d4e8ac611ffdd9845eba0772a6ac8469fe", callback=self.responseHTML)

	def responseHTML(self, response):
		'''
		The callback for requestHTML
		'''
		print response

	requestHTML()

	#txhasidlist = readTxhasid("trade_log_20160801_20161231.csv")

