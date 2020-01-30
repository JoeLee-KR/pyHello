# Section09
# 파일 읽기, 쓰기

# 읽기 모드 r, 쓰기 모드(기존 파일 삭제) w, 추가 모드(파일 생성 또는 추가) a
# 기타 : https://docs.python.org/3.7/library/functions.html#open
#       Reference file handling....

# 상대 경로('../', './'), 절대 경로 확인('C:\...')
#

# 파일 읽기
# 예제1
print("EX 1 ==================")
fd = open('../resource/review.txt', 'r')
contents = fd.read()
print(contents)
# print(dir(fd))
# fd에 포함된 가능한 메소드들을 확인한다. dir
# 반드시 close 리소스 반환
fd.close()

print()


# 예제2 : fd life scope is with paragraph
print("EX 2 ==================")
with open('../resource/review.txt', 'r') as fd:
    c = fd.read()
    print(iter(c))  #
    print(list(c))  #
    print(c)

print()

# read : 전체 내용 읽기, read(10) : 10글자 읽기

# 예제3
print("EX 3 ==================")
with open('../resource/review.txt', 'r') as fd:
    for c in fd:
        # print(c)
        print(c.strip())

print()

# 예제4
with open('../resource/review.txt', 'r') as fd:
    contents = fd.read()
    print('>', contents)
    contents = fd.read()
    print('>', contents)  # 내용 없음
    fd.seek(0, 0)
    contents = fd.read()
    print('>', contents)

# readline : 한 줄씩 읽기, readline(문자수) : 문자수 읽기

print()

# 예제5
with open('../resource/review.txt', 'r') as fd:
    line = fd.readline()
    while line:
        print(line, end='')
        line = fd.readline()

# readlines : 전체 읽은 후 라인 단위 리스트 저장

print()
print()

# 예제6
with open('../resource/review.txt', 'r') as fd:
    contents = fd.readlines()
    print(contents)
    print()
    for c in contents:
        print(c, end='')

print()
print()

# 예제7
with open('../resource/score.txt', 'r') as fd:
    score = []
    for line in fd:
        score.append(int(line))
    print(score)
    print('Average : {:6.3f}'.format(sum(score) / len(score)))

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
