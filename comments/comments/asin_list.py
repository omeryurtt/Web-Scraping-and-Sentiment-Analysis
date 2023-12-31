import requests
from bs4 import BeautifulSoup

search_query="protein+powder"
base_url = "https://www.amazon.com/s?k="
url = base_url + search_query
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36", "referer":"https://www.amazon.com/s?k=protein+powder&crid=23BGILTDMSL6M&sprefix=protein+powder%2Caps%2C207&ref=nb_sb_noss_1"}
search_response = requests.get(url,headers=header)

def get_amazon_search(number):
    url = f"https://www.amazon.com/s?k=protein+powder&page={number}&crid=RXB2MWK23L7S&qid=1703686796&sprefix=protein+powd%2Caps%2C410&ref=sr_pg_3"
    page = requests.get(url,headers=header)
    if page.status_code == 200:
        return page
    else:
        return "Error"
def get_asin_list():
    asin_list=[]
    for i in range(1, 11):
        response=get_amazon_search(i)
        soup=BeautifulSoup(response.content, features="lxml")
        for a in soup.findAll("div",{'class':"sg-col-4-of-24 sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col s-widget-spacing-small sg-col-4-of-20"}):
            asin_list.append(a['data-asin'])

    return asin_list

