def load_data():
	df = pd.read_csv("hn_stories.csv",header=None,names=['submisssion_time','upvotes','url','headline'])
	return df
import pandas as pd
import numpy as np

if __name__=="__main__":
	hn = load_data()
	print(hn.head())
