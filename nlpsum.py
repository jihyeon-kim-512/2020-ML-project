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
            return str, 1
        else:
            pass

    for each_line in f2:
        if each_line.find(str)>=0:
            print(each_line)
            return str, 2
        else:
            pass

    for each_line in f3:
        if each_line.find(str)>=0:
            print(each_line)
            return str, 3
        else:
            pass


    for each_line in f4:
        if each_line.find(str)>=0:
            print(each_line)
            return str, 4
        else:
            pass

    for each_line in f5:
        if each_line.find(str)>=0:
            print(each_line)
            return str, 5
        else:
            pass

    for each_line in f6:
        if each_line.find(str)>=0:
            print(each_line)
            return str, 6
        else:
            pass


def cutting(txt):
    place = ''
    something = ''
    result = txt.split(' ')

    for i in range(0, len(result)):
        if result[i].endswith('오늘') or result[i].endswith('어제') :
            print(i)
            stnum = i

            print(result[stnum])
            del result[stnum]
            print(result)

            break


    for i in range(0, len(result)):
        if result[i].endswith('에서'):
            print(i)
            endnum = i

            place = result[i].replace('에서','')

            print(result[endnum])
            del result[endnum]

            break




    for i in range(0, len(result)):
        if result[i].endswith('원'):
            print(i)
            endnum = i
            print(result[endnum])
            del result[endnum:]
            print(result)

            break

    return  result

txt = '어제 엄마랑 라면 4500원'
ctg = []
txt = cutting(txt)
print(txt)

for i in txt:
    ctg = category(i)

print(ctg[0], ctg[1])
