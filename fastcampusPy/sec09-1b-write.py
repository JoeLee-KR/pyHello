# 파일 쓰기

# 예제1
with open('../resource/test.txt', 'w') as fd:
    fd.write('niceman!')

# 예제2
with open('../resource/test.txt', 'a') as fd:
    fd.write('niceman!!')

# 예제3
from random import randint

with open('../resource/score2.txt', 'w') as fd:
    for cnt in range(6):
        fd.write(str(randint(50, 100)))
        fd.write('\n')

# 예제4
# writelines : 리스트 -> 파일로 저장
with open('../resource/test2.txt', 'w') as fd:
    list = ['Kim\n', 'Park\n', 'Lee\n']
    fd.writelines(list)

# 예제5
with open('../resource/test3.txt', 'w') as fd:
    print('Test Contents!', file=fd)
    print('Test Contents!!', file=fd)
