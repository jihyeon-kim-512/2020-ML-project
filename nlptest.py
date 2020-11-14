import sys
import io
import re

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


from datetime import date, timedelta
from konlpy.tag import Okt
okt = Okt()

# from konlpy.tag import Kkma
# kkma = Kkma()

# print(okt.pos("오늘 사랑드림에서 짜장밥을 먹어서 5000원을 썼다."))
# print(okt.nouns("오늘 사랑드림에서 짜장밥을 먹어서 5000원을 썼다."))

today = date.today()
yesterday = date.today() - timedelta(1)

# def haha(json):
    # txt = okt.morphs(json['msg'])
txt = okt.morphs('어제 새우볶음밥 5000원')
time_list = ['어제', '오늘']

if time_list[0] in txt:
    date = yesterday.strftime('%Y-%m-%d')
elif time_list[1] in txt:
    date = today.strftime('%Y-%m-%d')
else:
    date = today.strftime('%Y-%m-%d')


str2 = '원'
sum=0
for i in range(len(txt)):
    str1=txt[i]
    # for a in re.finditer(str2,str1) :
    #     endstr = a.start()
    vv = okt.pos(str1)
    print(vv)
    if vv[0][1]=='Number' :
        money = vv[0][0]
        for a in re.finditer('원', money) :
            endstr = a.start()
            try :
                sum += int(money[:endstr])
            except :
                money = (money[:endstr])
                print('e')
            print(sum)
        for b in re.finditer('십', money) :
            bs = b.start()
            be = b.end()
            sum += int(money[:bs] + '0' + money[be:])
            print(sum)
        for b in re.finditer('백', money) :
            bs = b.start()
            be = b.end()
            sum += int(money[:bs] + '00' + money[be:])
            print(sum)
        for b in re.finditer('천', money) :
            bs = b.start()
            be = b.end()
            sum += int(money[:bs] + '000' + money[be:])
            print(sum)
        for b in re.finditer('만', money) :
            bs = b.start()
            be = b.end()
            sum = int(money[:bs] + '0000' + money[be:])
            print(sum)

    else :
        continue

print('날짜: ' + date + '\n금액: ' + str(sum))


    # return


# from konlpy.tag import Kkma
# kkma = Kkma()
# print(kkma.morphs("오늘 사랑드림에서 짜장밥을 먹어서 5000원을 썼다."))
#
# print(kkma.pos("오늘 사랑드림에서 짜장밥을 먹어서 5000원을 썼다."))
#
# print(kkma.nouns("오늘 사랑드림에서 짜장밥을 먹어서 5000원을 썼다."))
#
# from konlpy.tag import Kkma
# from konlpy.tag import Komoran
# from konlpy.tag import Hannanum
#
# kkma = Kkma()
# kom = Komoran()
# hann = Hannanum()
#
# print(kkma.nouns(u'오늘 사랑드림에서 짜장밥을 먹어서 5000원을 썼다.'))
# print(kom.nouns(u'오늘 사랑드림에서 짜장밥을 먹어서 5000원을 썼다.'))
# print(hann.nouns(u'오늘 사랑드림에서 짜장밥을 먹어서 5000원을 썼다.'))
# print(hann.pos("5000 만원 bag"))
