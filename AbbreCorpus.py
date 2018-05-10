import pandas as pd

def readCorpus():
	excelfile = pd.read_excel('.\\Testing.xlsx',sheet_name = 0,header = 0)
	print(excelfile)

	for i in excelfile.index:
		print(excelfile['Abbreviation'][i]+' = '+excelfile['Origin'][i])
	return excelfile

def findWords(abbreWords,excelfile):
	originWords = ''
	for i in excelfile.index:
		print(abbreWords+' compare with '+excelfile['Abbreviation'][i])
		if(abbreWords.lower() == excelfile['Abbreviation'][i]):
			originWords = excelfile['Origin'][i]
			break
		else:
			pass
			
	return originWords


excelfile = readCorpus()
abbreWords = 'abg'
originWords = findWords(abbreWords,excelfile)
print(originWords)
