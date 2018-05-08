import requests
from bs4 import BeautifulSoup
from itertools import groupby


def search(restaurant_name="", cuisine_id="", district_id="", dishes_id="", amenity_id="", theme_id="", price=""):
    url = 'http://api.openrice.com/english/mobile/' \
          'sr1.htm?inputcategory=cname' \
          '&inputstrrest={}' \
          '&cuisine_id=' \
          '&district_id=' \
          '&dishes_id=' \
          '&amenity_id=' \
          '&theme_id=' \
          '&price='.format(restaurant_name, cuisine_id, district_id, dishes_id, amenity_id, theme_id, price)
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    res = soup.find_all("span", {"class": "basic_info_spacing"})

    res2 = [list(group) for k, group in groupby(res, lambda x: x.find('font', {"color": "red"}))]
    restaurants = [list(a) + list(b) for a, b in zip(res2[::2], res2[1::2])]
    res_dict = []

    for each in restaurants:
        d = {}
        d['name'] = each[0].find('a').string
        d['link'] = each[0].find('a')['href']
        for eachp in each:
            if '地址' in eachp.text:
                d['address'] = eachp.text.split(':', 1)[1].strip()
            if '電話' in eachp.text:
                d['phone'] = eachp.find('a').string
            if '類別' in eachp.text:
                d['category'] = [x.string for x in eachp.find_all('a')]
            if '消費' in eachp.text:
                d['expense'] = eachp.text.split(':', 1)[1].strip()
            if '總評分' in eachp.text:
                d['rating'] = eachp.text.split(':', 1)[1].strip()
            if '食評' in eachp.text:
                d['full_rating'] = dict(zip([x['alt'] for x in eachp.find_all('img')], [x.text for x in eachp.find_all('b')][1:]))
        res_dict.append(d)
    return {"result": res_dict}
