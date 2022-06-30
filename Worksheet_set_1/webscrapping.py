#!/usr/bin/env python
# coding: utf-8

# In[1]:


"1. Write a python program to display all the header tags from wikipedia.org.


# In[73]:


from bs4 import BeautifulSoup
import requests


# In[19]:


page=requests.get('https://en.wikipedia.org/wiki/Main_Page')


# In[20]:


page


# In[ ]:





# In[21]:



soup=BeautifulSoup(page.content)


# In[22]:


soup


# In[23]:


print(soup.title)


# In[24]:


print(soup.find_all(['h1', 'h2','h3','h4','h5','h6']))


# In[25]:


header=soup.find_all(['h1', 'h2','h3','h4','h5','h6'])


# In[26]:


h=[item for item in header]


# In[27]:


h


# In[28]:


"2. Write a python program to display IMDB’s Top rated 100 movies’ data (i.e. name, rating, year of release) and make data frame.


# In[36]:


page=requests.get('https://www.imdb.com/chart/top/')


# In[37]:


page


# In[38]:


soup=BeautifulSoup(page.content,'html.parser')


# In[42]:


movies=soup.find('tbody',class_='lister-list').find_all('tr')


# 

# In[44]:


print(len(movies))


# In[51]:


movies_all=[]
for movie in movies:
    name=movie.find('td',class_='titleColumn').a.text
    movies_all.append(name)


# In[52]:


movies_all


# In[57]:


movies_100=movies_all[0:101]


# 

# In[58]:


movies_100


# In[61]:


year=[]
for movie in movies:
    name=movie.find('td',class_='titleColumn').span.text.strip('()')
    year.append(name)


# In[62]:


year


# In[63]:


year_100=year[0:101]


# In[64]:


year


# In[65]:


rating=[]
for movie in movies:
    name=movie.find('td',class_='ratingColumn imdbRating').strong.text
    rating.append(name)


# In[66]:


rating


# In[67]:


rating_100=rating[0:101]


# In[68]:


rating


# In[69]:


import pandas as pd


# In[72]:


df=pd.DataFrame({'MovieName':movies_100,'Year':year_100,'Ratings':rating_100})


# In[73]:


df


# In[74]:


"3. Write a python program to display IMDB’s Top rated 100 Indian movies’ data (i.e. name, rating, year of release) and make data frame.


# In[76]:


page=requests.get('https://www.imdb.com/india/top-rated-indian-movies/')


# In[77]:


page


# In[78]:


soup=BeautifulSoup(page.content,'html.parser')


# In[80]:


print(soup)


# In[110]:


movie=soup.find('tbody',class_='lister-list').find_all('tr')


# In[116]:


movies=[]
year=[]
rating=[]
for item in movie:
    name=item.find('td',class_='titleColumn').a.text
    movies.append(name)
    y=item.find('td',class_='titleColumn').span.text.strip('()')
    year.append(y)
    r=item.find('td',class_='ratingColumn imdbRating').strong.text
    rating.append(r)
    


# In[118]:


movies_100=movies[0:100]
year_100=year[0:100]
rating_100=rating[0:100]


# In[119]:


df=pd.DataFrame({'Movies Name':movies_100,'Year':year_100,'Ratings':rating_100})


# In[120]:


df


# In[122]:


"4. Write s python program to display list of respected former presidents of India(i.e. Name , Term of office) 


# In[123]:


page=requests.get('https://presidentofindia.nic.in/former-presidents.htm')


# In[124]:


page


# In[125]:


soup=BeautifulSoup(page.content,'html.parser')


# In[128]:


president=soup.find('ul',class_='listing cf').find_all('li')


# In[162]:


l1=[]
for President in president:
    name=President.find('div',class_='presidentListing').h3.text
    l1.append(name)


# In[163]:


l1


# In[166]:


l2=[]
for President in president:
    name=President.find('div',class_='presidentListing').p.text
    l2.append(name)


# In[167]:


l2


# In[171]:


l=list(zip(l1,l2))


# In[172]:


l


# In[2]:


"5. Write a python program to scrape cricket rankings from icc-cricket.com. You have to scrape:


# In[5]:


page=requests.get('https://www.icc-cricket.com/rankings/mens/team-rankings/odi')


# In[6]:


page


# In[7]:


soup=BeautifulSoup(page.content,'html.parser')


# In[8]:


teams=soup.find_all('tr',class_='table-body')
teams


# In[10]:


Team=[]
for team in teams:
    name=team.find('td',class_='table-body__cell rankings-table__team').text.strip()
    Team.append(name)
    


# In[11]:


T=[]
for item in Team:
    T.append(item.strip('\n').replace('\n',' '))


# In[12]:


T


# In[13]:


Matches=[]
for team in teams:
    name=team.find('td',class_='table-body__cell u-center-text').text.strip()
    Matches.append(name)
   


# In[14]:


Matches


# In[16]:



"7. Write a python program to scrape mentioned news details from https://www.cnbc.com/world/?region=world :


# In[17]:


page=requests.get('https://www.cnbc.com/world/?region=world')


# In[18]:


page


# In[19]:


soup=BeautifulSoup(page.content,'html.parser')


# In[48]:


headline=soup.find_all('li',class_='LatestNews-item')
headline


# In[53]:


for i in headline:
    h=i.find('div',class_='LatestNews-container').text
    
    print(h)


# In[2]:


"8. Write a python program to scrape the details of most downloaded articles from AI in last 90 days. 


# In[4]:


page=requests.get('https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles')


# In[5]:


page


# In[6]:


soup=BeautifulSoup(page.content,'html.parser')


# In[7]:


p=soup.find('ul',class_='sc-9zxyh7-0 ffmPq')


# In[8]:



for item in p:
    article=item.find('h2',class_='sc-1qrq3sd-1 MKjKb sc-1nmom32-0 sc-1nmom32-1 hqhUYH ebTA-dR').text
    print(article)


# In[10]:


for item in p:
    Authors=item.find('span',class_='sc-1w3fpd7-0 pgLAT').text
    print(Authors)


# In[11]:


for item in p:
    Date=item.find('span',class_='sc-1thf9ly-2 bKddwo').text
    print(Date)


# In[40]:


for links in soup.find_all("a"):
    link=links.get('href')
    print(link)
   


# In[41]:


"9) Write a python program to scrape mentioned details from dineout.co.in :
"i) Restaurant name
"ii) Cuisine
"iii) Location 
"iv) Ratings
"v) Image URL
 


# In[42]:


page=requests.get('https://www.dineout.co.in/delhi-restaurants/buffet-special')


# In[43]:


page


# In[44]:


soup=BeautifulSoup(page.content,'html.parser')


# In[67]:


for i in soup.find_all('div',class_='restnt-info cursor'):
    print(i.text)


# In[68]:


for i in soup.find_all('div',class_='restnt-loc ellipsis'):
    print(i.text)


# In[69]:


for i in soup.find_all('span',class_='double-line-ellipsis'):
    print(i.text)


# In[71]:


for i in soup.find_all('img',class_='no-img'):
    print(i['data-src'])


# In[72]:


"10. Write a python program to scrape the details of top publications from Google Scholar.


# In[74]:


page=requests.get('https://scholar.google.com/citations?view_op=top_venues&hl=en')


# In[75]:


page


# In[76]:


soup=BeautifulSoup(page.content,'html.parser')


# In[124]:


p=soup.find_all('td',class_='gsc_mvt_t')


# In[129]:


Publication=[]
for i in p:
    Publication.append(i.text)
print(Publication)


# In[194]:


p=soup.find_all('td',class_='gsc_mvt_p')


# In[199]:


Rank=[]
for i in p:
    Rank.append(i.text.strip(" ',' "))
print(Rank)


# In[180]:


p=soup.find_all('a',class_='gs_ibl gsc_mp_anchor')


# In[185]:


h5=[]
for i in p:
    h5.append(i.text)
print(h5)


# In[186]:


p=soup.find_all('span',class_='gs_ibl gsc_mp_anchor')


# In[187]:


h5m=[]
for i in p:
    h5m.append(i.text)
print(h5m)


# In[200]:


import pandas as pd

len(Rank)


# In[201]:


df=pd.DataFrame({'Rank':Rank,'Publication':Publication,'h5-index':h5,'h5-median':h5m})


# In[202]:


df


# In[1]:


## Remaining questions


# In[2]:


##6) Write a python program to scrape cricket rankings from icc-cricket.com. You have to scrape:


# In[20]:


from bs4 import BeautifulSoup
import requests


# In[21]:


page=requests.get('https://www.icc-cricket.com/rankings/womens/team-rankings/odi')


# In[22]:


page


# In[23]:


soup= BeautifulSoup(page.content,'html.parser')


# In[24]:


Team_w=soup.find_all('span', class_="u-hide-phablet")
Team_w


# In[25]:


Team_W=[]
for team in Team_w:
    team=team.get_text().replace('\n','')


    
    Team_W.append(team)
    
Team_W[0:10]


# In[31]:


matches_w=soup.find('td', class_="rankings-block__banner--matches")
matches_w.text
match=matches_w.text
match


# In[27]:


Matches_w=soup.find_all('td', class_="table-body__cell u-center-text")
Matches_w


# In[28]:


Matches_W=[]
for match in Matches_w:
    match=match.get_text().replace('\n','')


    
    Matches_W.append(match)
    
Matches_W[0:19:2]
Matches_odi_w=Matches_W[0:19:2]
Matches_odi_w


# In[36]:


ODI_matches= [match]+[Matches_odi_w]


# In[37]:


ODI_matches


# In[38]:


Matches_odi=Matches_W[1:19:2]
Matches_odi
Point=Matches_odi
Point


# In[39]:


point_w=soup.find('td', class_="rankings-block__banner--points")
point_w.text
Point_w=point_w.text
Point_w


# In[40]:


Point_ODI=[Point_w]+[Point]
Point_ODI


# In[41]:


rating=soup.find('td', class_="rankings-block__banner--rating u-text-right")
rating.text.replace('\n','')
rating1= rating.text.replace('\n','')
rating1


# In[42]:


rating=soup.find_all('td',class_="table-body__cell u-text-right rating")
rating


# In[43]:


Rating=[]
for rating_1 in rating:
    rating_1= rating_1.get_text().replace('\n','')
    
    Rating.append(rating_1)
    
Rating


# In[44]:


Rating_ODI_W=[rating1]+[Rating]
Rating_ODI_W


# In[45]:


"6." Top 10 women’s ODI players along with the records of their team and rating.


# In[46]:


page= requests.get("https://www.icc-cricket.com/rankings/womens/player-rankings/odi")
page


# In[47]:


soup= BeautifulSoup(page.content,'html.parser')


# In[48]:


w_b=soup.find('div', class_="rankings-block__banner--name")
w_b.text
w=w_b.text
w


# In[49]:


w_1=soup.find_all('td', class_="table-body__cell name")
w_1


# In[50]:


Names=[]

for w_l in w_1:
    w_l=w_l.get_text().replace('\n','')
    
    Names.append(w_l)
    
Names[0:10]
N= Names[0:10]
N


# In[51]:


Names_Wteam=[w]+[N]
Names_Wteam


# In[54]:


T_w=soup.find('div', class_="rankings-block__banner--nationality")
T_w.text.replace("\n",'')


# In[55]:


t_w=soup.find_all('span', class_="table-body__logo-text")
t_w


# In[56]:


Team_w=[]
for team in t_w:
    team= team.get_text().replace('\n','')
    
    Team_w.append(team)
Team_w


# In[57]:


r_w=soup.find_all('td', class_="table-body__cell u-text-right rating")
r_w


# In[58]:


Rating_w=[]
for r in r_w:
    r= r.get_text().replace('\n','')
    
    Rating_w.append(r)
    
Rating_w


# In[59]:


page= requests.get("https://www.icc-cricket.com/rankings/womens/player-rankings/odi/all-rounder")
page


# In[60]:


soup= BeautifulSoup(page.content,'html.parser')


# In[61]:


Name=[]
for i in soup.find_all("div", class_="rankings-block__banner--name-large"):
    Name.append(i.text)
Name


# In[62]:


Name1=[]
for i in soup.find_all("td", class_="table-body__cell rankings-table__name name"):
    Name1.append(i.text.replace("\n",''))
Name1


# In[63]:


Team=[]
for i in soup.find_all("div", class_="rankings-block__banner--nationality"):
    Team.append(i.text.replace("\n",''))
Team


# In[64]:


Rating=[]
for i in soup.find_all("div", class_="rankings-block__banner--rating"):
    Rating.append(i.text.replace("\n",''))
Rating


# In[65]:


Team1=[]
for i in soup.find_all("span", class_="table-body__logo-text"):
    Team1.append(i.text.replace("\n",''))
Team1


# In[66]:


Rating1=[]
for i in soup.find_all("td", class_="table-body__cell rating"):
    Rating1.append(i.text.replace("\n",''))
Rating1


# In[ ]:




