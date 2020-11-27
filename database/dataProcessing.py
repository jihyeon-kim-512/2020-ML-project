import re
import string
from konlpy.tag import Okt

okt = Okt()

def cash_change(money):
    sum = 0

    for a in re.finditer('원', money) :
        endstr = a.start()
        try :
            sum += int(money[:endstr])
        except :
            money = (money[:endstr])
            print('e')
        # print(sum)
    for b in re.finditer('십', money) :
        bs = b.start()
        be = b.end()
        sum += int(money[:bs] + '0' + money[be:])
        # print(sum)
    for b in re.finditer('백', money) :
        bs = b.start()
        be = b.end()
        sum += int(money[:bs] + '00' + money[be:])
        # print(sum)
    for b in re.finditer('천', money) :
        bs = b.start()
        be = b.end()
        sum += int(money[:bs] + '000' + money[be:])
        # print(sum)
    for b in re.finditer('만', money) :
        bs = b.start()
        be = b.end()
        sum = int(money[:bs] + '0000' + money[be:])
        # print(sum)

    return sum




def somethings(txt):
    place = ''
    something = ''
    result = okt.nouns(txt)

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

    something = " ".join(result)

    return place, something



def category(str) :
    print(str)
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

    if str == '월급':
        return str, 7
    else:
        pass

    if str == '용돈':
        return str, 8
    else:
        pass


    return str, 9
