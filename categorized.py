import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


import string

def category(str) :
    f1 = open("dataset/cloth_words_self.csv", "r", encoding="ANSI")
    f2 = open("dataset/beauty_words_self.csv", "r", encoding="ANSI")
    f3 = open("dataset/house_words_self.csv", "r", encoding="ANSI")
    f4 = open("dataset/trip_words_self.csv", "r", encoding="ANSI")
    f5 = open("dataset/traffic_words_self.csv", "r", encoding="ANSI")
    f6 = open("dataset/food_crawl.csv", "r", encoding="ANSI")

    for each_line in f1:
        if each_line.find(str)>=0:
            print(each_line)
            return "의류"
        else:
            pass

    for each_line in f2:
        if each_line.find(str)>=0:
            print(each_line)
            return "뷰티"
        else:
            pass

    for each_line in f3:
        if each_line.find(str)>=0:
            print(each_line)
            return "생활비"
        else:
            pass


    for each_line in f4:
        if each_line.find(str)>=0:
            print(each_line)
            return "여행"
        else:
            pass

    for each_line in f5:
        if each_line.find(str)>=0:
            print(each_line)
            return "교통비"
        else:
            pass

    for each_line in f6:
        if each_line.find(str)>=0:
            print(each_line)
            return "식비"
        else:
            pass




from datetime import date, timedelta
from konlpy.tag import Okt
okt = Okt()

vivi = okt.nouns("바지4500원")
for i in range(len(vivi)) :
    chk = category(str(vivi[i]))

    if chk != None :
        break
print(chk)





# vivi = "어제 엄마랑 감성골에서 고추장불고기 11500원"
# result = vivi.split(' ')
#
# for i in range(0, len(result)):
#     if result[i].endswith('오늘') or result[i].endswith('어제') :
#         print(i)
#         stnum = i
#
#         print(result[stnum])
#         del result[stnum]
#         print(result)
#
#         break
#
#
# for i in range(0, len(result)):
#     if result[i].endswith('원'):
#         print(i)
#         endnum = i
#
#         print(result[endnum])
#         del result[endnum:]
#         print(result)
#
#         break
#
# place = ''
#
# for i in range(0, len(result)):
#     if result[i].endswith('에서'):
#         print(i)
#         endnum = i
#
#         place = result[i]
#
#         print(result[endnum])
#         del result[endnum]
#
#
#         break
#
# print(result)




#한글자 삭제
# with open("C:/Users/Admin/Documents/카카오톡 받은 파일/food_words_self.txt", encoding="utf-8") as f:
#     data = f.readlines()
# with open("C:/Users/Admin/Documents/카카오톡 받은 파일/food_words_self.txt", 'w') as outfile:
#     for i in data:
#         if len(i) != 2:
#             outfile.write(i)


# 웹페이지 크롤링
# import csv
# from urllib.request import urlopen
# from urllib.parse import quote_plus
# from bs4 import BeautifulSoup
#
# for num in range(2,61):
#     url = f'https://www.menupan.com/Cook/RecipeRe.asp?difficulty=10&page='+str(num)
#     html = urlopen(url).read()
#     soup = BeautifulSoup(html, 'html.parser')
#
#     total = soup.select('.link')
#
#     searchList = []
#
#     for i in total:
#         temp = []
#         temp.append(i.text)
#         searchList.append(temp)
#     searchList = searchList[:15]
#     print(searchList)
#
#     # f = open(f'food_crawl.csv', 'w', encoding='utf-8', newline='')
#     f = open(f'food_crawl.csv', 'a', encoding='utf-8', newline='')
#     csvWriter = csv.writer(f)
#     for i in searchList:
#         csvWriter.writerow(i)
#
#     f.close()
#
# print('완료되었습니다.')
