'''
PY[^PY]{0, 10}
'''
import re




#1.Location : The 'plus' house has class = _3fbupa, this will be a label to check whether a house is a plus one
#2.status
#3.introduction
#4.Amenities: _iq8x9is 2 to 15


with open('./htmls/0.html') as pg0:
    soup_pg0 = BeautifulSoup(pg0, 'lxml')