# 크롤링 실습2 ㅣ 예스 24 베스트셀러 크롤링
# 카테고리: 소설 시 희곡 , 에세이 it 모바일
# 3가지 각 카테고리의 베스트 셀러 도서 크롤링 하기


import urllib.request
from bs4 import  BeautifulSoup
categorylist = ['001001046','001001047','001001003']
# 3. 반복문을 이용한 여러개 카테고리 url 요청
for category in categorylist: # 리스트내 요소(카테고리번호)를 하나씩 추출 # f 포메팅 f'문자열(변수 또는 리터널 또는 연산자} 문자열'
    url = f'https://www.yes24.com/Product/Category/BestSeller?pageNumber=1&pageSize=24&categoryNumber={category}'
    response = urllib.request.urlopen( url )
    htmldata = response.read()
    # 4. BeautifulSoup 객체 이용한 마크업 추출, 도서정보(순위,도서명,저자)
    soup = BeautifulSoup(htmldata,'html.parser')
    contents = soup.select_one('#yesBestList') # 식별자 작성법 : 1. 마크업  - 마크업명 2. class - 'clascs명' 3. id
    rows = contents.select('li')
for row in rows:
# print(row)
# 5. 도서정보 지려에서 도서명 추출
    gdname = row.select_one('.gd_name')
    if gdname != None:
        if gdname != None:
            bookName = gdname.string
            print(bookName)
# 6. 도서정보 자료 에서 저자 추출하기
    authpub = row.select_one('.authPub')
