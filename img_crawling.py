from bs4 import BeautifulSoup
import urllib.request
import urllib.parse  # 한글검색 가능하게

baseUrl = "https://search.naver.com/search.naver?where=image&sm=tab_jum&query="
searchUrl = input("검색어를 입력하세요: ")
url = baseUrl + urllib.parse.quote_plus(searchUrl)

html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

images = soup.find_all("img", attrs={"class": "_img"})

for idx, image in enumerate(images):
    img_url = image['data-source']
    img_data = urllib.request.urlopen(img_url).read()

    with open("{0}{1}.jpg".format(searchUrl, idx+1), "wb") as f:
        f.write(img_data)

    if idx >= 9:
        break
