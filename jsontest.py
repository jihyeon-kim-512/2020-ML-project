import sys
import io
import json

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

from konlpy.tag import Kkma

kkma = Kkma()
# content = kkma.morphs("사랑드림어서 5000원을 썼다")
content = kkma.pos("오늘 사랑드림에서 짜장밥을 먹어서 5000원을 썼다.")
# content = kkma.nouns("오늘 사랑드림에서 짜장밥을 먹어서 5000원을 썼다.")

# print(content)
clean_words = []
for word in kkma.pos(document, stem=True): #어간 추출
    if word[1] in ['NR']: #명사, 동사, 형용사
        clean_words.append(word[0])
print(clean_words) #['스토리', '진짜', '노잼']


# with open('C:/AI_ML_Project/gun/sample_out.json', 'r', encoding='utf-8') as f:
#     sample = json.load(f)
#     print(sample['user_name'])

# with open('sample_out.json', 'w', encoding='utf-8') as w:
#     ctn={
#             "user_name"  : "김미미",
#             "time"       : "2020-11-01",
#             "money"      : "요즘 날씨가 너무 추워요"
#         }
#     json.dump(ctn, w, indent='\t')
