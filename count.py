import read
import pandas as pd
import numpy as np

if __name__=='__main__':
	df = read.load_data()
	words = []
	print(df.columns)
	print(df['headline'].head())
	for headline in list(df['headline']):
		print(headline[0])
	#	split_headline = headline.str.split(" ")
	#	for splits in split_headline:
	#		words.append(splits)
	#print(len(words))
	#print(words[:5])
