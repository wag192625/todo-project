# https://kante-kante.tistory.com/11

# import는 상단에
import requests
from bs4 import BeautifulSoup
 
 
#네이버 경제 메인 (안 됨)
url = f'https://news.naver.com/section/100'

# url = f'https://news.nate.com/recent?mid=n0105'

# headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"}
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    # 'Referer': 'https://google.com',
    # 'Accept-Language': 'en-US,en;q=0.9',
    # 'Cookie': 'your-cookie-here'
    }
response = requests.get(url,headers=headers)
soup = BeautifulSoup(response.text,'html.parser')

news_title = soup.select('#newsct > div.section_component.as_section_headline._PERSIST_CONTENT > div > ul > li > div > div > div.sa_text > a')
news_content = soup.select('#newsct > div.section_component.as_section_headline._PERSIST_CONTENT > div > ul > li > div > div > div.sa_text > div.sa_text_lede')
news_writing = soup.select('#newsct > div.section_component.as_section_headline._PERSIST_CONTENT > div > ul > li > div > div > div.sa_text > div.sa_text_info > div.sa_text_info_left')
news_image = soup.select('#newsct > div.section_component.as_section_headline._PERSIST_CONTENT > div > ul > li > div > div > div > div.sa_thumb_inner > a >img')

# news = soup.select('#newsct > div.section_component.as_section_headline._PERSIST_CONTENT > div > ul > li > div > div > div > div.sa_thumb_inner > a >img')

# print(news)

def newslist() :
    newslist = list()
    nnews = list()

    for news in news_title: # 뉴스 제목을 리스트에 append
        nnews.append(news.text.strip())

    for i in range(len(nnews)):
        title = news_title[i].text.strip()
        link = news_title[i].get('href')
        content = news_content[i].text.strip()
        writing = news_writing[i].text.strip()

        try: #list index out of range 방지를 위한 예외처리
            image_s = news_image[i].get('data-src')
            image = news_image[i].get('data-src').replace('nf132_90','w647') # 크기 조정을 위한 replace
        except:
            image_s="NO IMAGE"
            image = "NO IMAGE"

        item_obj = {
            'title': title,
            'link': link,
            'content': content,
            'writing': writing,
            'image': image,
            'image_s': image_s,
        }

        newslist.append(item_obj)

    return newslist

# print(newslist, end='\n')