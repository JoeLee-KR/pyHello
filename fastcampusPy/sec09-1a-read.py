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
#print(dir(fd))
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

# 예제3 / line strip?
print("EX 3 ==================")
with open('../resource/review.txt', 'r') as fd:
    for c in fd:
        # print(c)
        print(c.strip(),".")

print()

# 예제4
print("EX 4 ==================")
with open('../resource/review.txt', 'r') as fd:
    contents = fd.read()
    print('a>', contents)
    contents = fd.read()
    print('b>', contents)  # 내용 없음
    fd.seek(0, 0)
    contents = fd.read()
    print('c>', contents)

# readline : 한 줄씩 읽기, readline(문자수) : 문자수 읽기

print()

# 예제5
print("EX 5 ================== fd.readlin, once line")
with open('../resource/review.txt', 'r') as fd:
    line = fd.readline()
    while line:
        print(">>", line, end='')
        line = fd.readline()

# readlines : 전체 읽은 후 라인 단위 리스트 저장

print()
print()

# 예제6
print("EX 6 ================== fd.readlines, multiple lines")
with open('../resource/review.txt', 'r') as fd:
    contents = fd.readlines()
    print(contents)
    print()
    print("*********")
    for c in contents:
        print(c, end='')

print()
print()

# 예제7
print("EX 7 ================== score file by line")
with open('../resource/score.txt', 'r') as fd:
    score = []
    for line in fd:
        score.append(int(line))
    print(score)
    print('Average : {:6.3f}'.format(sum(score) / len(score)))

print("********** score file by whitespace???   ")
