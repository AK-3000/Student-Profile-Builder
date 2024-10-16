import numpy as np
import pandas as pd
import webbrowser
def tupdate(link):
	webbrowser.open(link)
	dfc=pd.read_csv('final-moooc-list.csv')
	dft=pd.read_csv('TAGS.csv')
	d_tag={dft.iloc[i][0]:dft.iloc[i][1] for i in range(len(dft))}
	loc=list(dfc['link']).index(link)
	tags=eval(dfc.iloc[loc][6])
	for i in tags:
		if i in d_tag.keys():
			d_tag[i]=d_tag[i]+1

	dft=pd.DataFrame([(k,v) for (k,v) in d_tag.items()])
	dft.to_csv('TAGS.csv',index=False)
