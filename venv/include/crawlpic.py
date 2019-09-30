import requests
import os
from bs4 import BeautifulSoup
import lxml

url = "https://www.airbnb.com.au/s/NSW--Australia/homes?refinement_paths%5B%5D=%2Fhomes&current_tab_id=home_tab&selected_tab_id=home_tab&place_id=ChIJDUte93TLDWsRLZ_EIhGvgBc&source=mc_search_bar&search_type=unknown&screen_size=large&hide_dates_and_guests_filters=false&map_toggle=false"
r = requests.get(url)
t = r.text
#print(t)
#soup = BeautifulSoup(t, 'lxml')
with open ('into.html') as h:
    soup = BeautifulSoup(h, 'lxml')

#print(soup.prettify())
#print(soup.title)

'''
using .a only return the first target, as well as .title
'''
tag = soup.a
#print(soup.prettify())
#print(tag)
#a_par = soup.a.parent.name
#print(a_par)

#tag_attributs = tag.attrs
#print(tag_attributs)

#tag_att_class = tag_attributs['class']
#print(tag_att_class)

'''
get the context between the tags: .string
'''
title_line = soup.title

#print(title_line.string)

tag_p = soup.div
#print(tag_p)

'''
html loop method
'''
###There are 3 ways to loop a DOM tree : up&down, bottom to top, parallel

tag_body = soup.body
print("-----------------------------head------------------------------------------")
#print(tag_head)
print("==============================head==========================================")

#tag_body_children = tag_body.contents
#print(tag_head_children)
#print("==================================head_children==================================")
#print(len(tag_body_children))

#for child in tag_head_children:
    #print(child)


#First Page data:
'''
html shown friendly: prettify
'''
#print(soup.prettify())
#print(soup.prettify())
#print(soup.img)
#1.Total house amount in NSW is 306
house_amount = soup.find_all(class_ = '_1dss1omb')
print(len(house_amount))
#print(house_amount)
for e in house_amount:
    print(e.string)
#2.the house title
house_title = soup.find_all(class_ = '_1dss1omb')
print(len(house_title))
#3.each house peice has 4 class, from 5 to 616, each house has two class, including price and number of reviews
house_price = soup.body.find_all(class_ ='_krjbj')
#print(soup.body.prettify())
print(len(house_price))
#4.house stars
house_stars = soup.find_all(class_ = '_tghtxy2')
print(len(house_stars))
count = 0
'''
for e in house_stars:
    print(e.string)
    print(count)
    count = count + 1
'''
#print(house_stars)
#5.house_image
#house_image = soup.find_all(class_ = '_1df8dftk')
#print(len(house_image))
#type(house_image)
houseim = soup.find_all(attrs={'class':'_1df8dftk'})
#print(len(house_image))
#print(houseim)
print(len(houseim))
house_image_list = []


'''
for e in houseim:
    #print(e)
    e_string = str(e)
    print(e_string)
    e_string = e_string.split('("')
    print(e_string)
    e_string = e_string[-1]
    print(e_string)
    #print(type(e_string))
    result = e_string.split('")')[0]
    print(result)
    house_image_list.append(result)
    print(house_image_list)

'''
#print(type(houseim))
