from mylib import core 
from bs4 import BeautifulSoup
import re  
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import jieba


print('please input paragraph')
pa = input()
ret = core.main(pa)
for i in ret:
	print(i.strip())