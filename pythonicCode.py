# 한 문자열에 넣기
colors = ['red','Blue','Yellow','Green']

# 방법 1.
result = ''
for i in colors:
    result += i
print(result)

# 방법 2. (pythonic code) -> 더욱 간단하게 만든다.
# 파이썬 특유의 문법을 활용하여 간결하게 만듬.
result2 = ''.join(colors)
print(result2)
# split과 join
items = 'zero one two three four'.split()
print(items)
ex = 'hi jane, im taek'.split(",")
print(ex)

# unpacking : 리스트 값을 각 변수에 넣어줌
a,b,c,d,e = 'zero one two three four'.split()
a,b,c,d,e = items
print(a,d)

colors = ['red','red1','red2','red3']
result = ', '.join(colors) # 앞에 ' '는 중간에 뭐로 이을지 정함
print(result)

# list comprehension
# 기존 리스트로 다른 리스트를 만드는 기법
# 자주 사용함
result = [i for i in range(10)]
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(result)

# 조건도 넣을 수 있음, 필터라고함
result = [i for i in range(10) if i % 2 == 0]
print(result)

#list comprehension for loop 두개 사용
word_1 = 'Hello'
word_2 = "Bye"
result = [i+j for i in word_1 for j in word_2]
# == 이중포문
print(result)
#결과물은 1차원 배열
#['HB', 'Hy', 'He', 'eB', 'ey', 'ee', 'lB', 'ly', 'le', 'lB', 'ly', 'le', 'oB', 'oy', 'oe']

result = [[i+j for i in word_1] for j in word_2]
print(result)
#결과물은 2차원 배열
# [['HB', 'eB', 'lB', 'lB', 'oB'], ['Hy', 'ey', 'ly', 'ly', 'oy'], ['He', 'ee', 'le', 'le', 'oe'...

# Zip , Enumerate
# enum : 인덱스와 밸류를 같이 저장. 아래 코드는 i에 인덱스, v에 밸류를 언팩킹함
# enum 함수를 돌리면 인덱스랑 밸류가 나오나봄
for i, v in enumerate(['tic','tac','toc']):
    print(i,v)

mylist = ["a","b","c","d","e"]
enumlist = list(enumerate(mylist))
print(enumlist)
#[(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd'), (4, 'e')]
print(enumlist[0][1])
# a
# 튜플로 묶어서 나옴

dictenum = {i:v for i,v in enumerate(mylist)}
print(dictenum)
# 딕셔너리 타입으로 나옴

#zip : 두 개의 리스트 값을 병렬적으로 추출
alist = ['a1','a2','a3']
blist = [1,2,3]
# 튜플 형식으로 들어감
for a in zip(alist,blist):
    print(a)

x = (1,11,111)
#튜플에 들어간거 다 더해줌
print(sum(x))
