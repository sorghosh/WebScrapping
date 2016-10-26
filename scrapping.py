import urllib
from bs4 import BeautifulSoup
import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

class Scrap:
    
    def gettext(self,url):
        text = url.string
        if text == None:
            cnt = url.contents
            resultset = ''
            for c in cnt:
                subtext = self.gettext(c)
                resultset = resultset + subtext+"\n"
            return resultset
        return text.strip()
    
    def getwords(self,text):
        
        spliter = re.compile("\\W*")
        words   = [t.lower() for t in spliter.split(text) if t != '']
        return words
    
    def word_normalization(self,url):
        text = []
        for i in url:
            urlread = urllib.urlopen(i)
            soup    = BeautifulSoup(urlread.read(),'lxml')
            text.append(self.gettext(soup))
            
        count_vec = CountVectorizer()
        wordcounts = count_vec.fit_transform(text)
        Tfid_obj = TfidfTransformer(use_idf = True)
        Tfid_obj.fit(wordcounts)
                
        return Tfid_obj.transform(wordcounts).toarray(),sorted(count_vec.vocabulary_.items())[0]
        
        

url1 = ["https://in.news.yahoo.com/jaitley-trying-please-narcissist-pm-modi-congress-074242917.html?nhp=1" ,"https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"]
Scrap_obj = Scrap()
word_array,column_header = Scrap_obj.word_normalization(url1)
print "test"



