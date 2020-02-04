import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/news')
res2 = requests.get('https://news.ycombinator.com/news?p=2') #2nd page
soup = BeautifulSoup(res.text, 'html.parser') #converts it to an object string-->html
soup2 = BeautifulSoup(res2.text, 'html.parser')

links = soup.select('.storylink')
subtext = soup.select('.subtext')
links2 = soup2.select('.storylink')
subtext2 = soup2.select('.subtext')

mega_links = links + links2 #combining two pages
mega_subtext = subtext + subtext2

def sort_stories_by_votes(hnlist):
	#can't sort dictory like sorting a list. Need to give a parameter to sort it by. Here we sort by votes
  return sorted(hnlist, key= lambda k:k['votes'], reverse=True) # reverse = True, sorts it in reverese order 

def create_custom_hn(links, subtext):
  hn = []
  for idx, item in enumerate(links):  #enumerate gives an index and value, here received by idx and item respectively 
    title = item.getText()
    href = item.get('href', None)
    vote = subtext[idx].select('.score')#here the index is needed sincewe are only enumerating links.So to get the subtext,we need index
    if len(vote): #to make sure the links with no points creates no error 
      points = int(vote[0].getText().replace(' points', ''))#votes came as ex:136 points,we need to remove points and replace with space
      if points > 99:
        hn.append({'title': title, 'link': href, 'votes': points}) #dictionary 
  return sort_stories_by_votes(hn)
 
pprint.pprint(create_custom_hn(mega_links, mega_subtext))
