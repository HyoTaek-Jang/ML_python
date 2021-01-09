# Numpy 고성능 과학 계산용 패키지, 매트릭스와 백터와 같은 어레이 연산의 사실상의 표준
# 반복문 없이 배열처리 가능, 일반 리스트보다 빠름.

#numpy 설치, 미니콘다 설치하고 프롬프트에서 pip install numpy scipy matplotlib ipython scikit-learn pandas pillow 명령어 입력
'''
미니콘다 설치
미니콘다에 가상환경 설치 및 패키지 설치
파이참에서  세팅 인터프리터에서 아나콘다 환경 추가.
'''
# numpy 사용법
import numpy as np

# 파이썬의 큰 특징, 다이나믹 타이핑 : 실행 시점에 데이터 타입을 결정. 메모리 공간을 계속 수정함.
# 넘파이는 허락하지 않음 아래 경우 플로트로 데이터 타입을 정해놨기에 다 플로트로 만들어버림.
# 파이썬은 메모리 주소를 통해 리스트를 관리하고 넘파이는 그냥 값으로 보기에 속도가 더 빠름
test_array = np.array(['1','4',5,8], np.float32)
print(test_array)

# 튜플 타입, 매트릭스의 크기를 구하는 느낌
# 3rd order tensor(5,3,4)  5: 테이블 깊이, 3: row수, 4: col수
print(test_array.shape)

#ndim : 디멘션의 크기
#size : 전체 데이터의 갯수

#reshape 원래 2,4라면 2,2,2로 바꾸고 그럴수 있음.
test = [[1,2,3,4],[1,2,5,8]]
print(np.array(test).shape)
print(np.array(test))
print(np.array(test).reshape(2,2,2))
#reshape(-1,2) 이면 칼럼이 2개고 로우는 알아서 맞춰서 바꿔라
# 1차원 어레이로 쫙 펴주는거 .flatten()

#indexing
# a[0,0] == a[0][0]

#slicing
#a[:,2:] 로우는 전체, 컬럼은 2행 이상.
#x:y:z -> x 시작지점, y: 종료지점 z: 스탭

#arange : array 범위를 지정하여 리스트를 생성
# arange(0,5,0.5) floating point도 가능
a = np.arange(30).reshape(-1,5)
print(a)

#ones, zeros and empty -> 0으로 채워주고 1로 채워주고 메모리 공간만 잡아주고 ㅇㅇ
b = np.zeros(shape=(10,3), dtype=np.int8)
print(b)

# eye 대각선인 1인 행렬

#random sampling 데이터 분포에 따른 랜덤한 값을 가져올 수 있음

#axis : 기준, axis = 0 -> row기준 , axis = 1 -> col기준
# 새로 생기는 부분이 axis 0, 기존이 1

#concatenate : 어레이를 합치는 함수
# np.concatenate((a,b), axis=0) row에 붙임
# 속도가 느림. 메모리 공간을 확보하고 하나하나 붙어야함. 파이썬을 그냥 주소만 정해주면 되서 빠름.

'''
array 사칙 연산
그냥 + 하면 되고 -하면 되고..;;
*은 그냥 같은위치 곱해주는거고
 우리가 하는 매트릭스 곱은 x.dot(b)
 
 broadcasting
 쉐잎이 다른 배열간 연산을 지원
 스칼라와 매트릭스 연산이 가능하게함 백터 매트릭스도 가능.
 
 비교를 할때 넘파이 어레이와 스칼라를 비교하면 결과가 넘파이 어레이로 나옴
 any는 1개이상, all은 모두
 
 np.logical.and
 np.logical.not
 np.logical.or
 
 np.where -> 조건에 만족하는 위치를 뱉어냄
 
 np.where(a>0, 3,2) -> 트루면 3, 아니ㅕㅁㄴ 2
np.where(a>0) 0보다 큰 인덱스 반환

최대값 최소값 
argmax , argmin을 사용함.
np.argmax(array) -> 인덱스 번호 리턴
np.argmax(array, axis=1) -> 인덱스 번호 리턴

넘파이는 워낙 많은 좋은 함수가 있기에 포문은 거의 안씀

boolean index
컨디션에 맞춰서 해당하는 인덱스만 뽑음. 트루인 인덱스만 줌
test_array[condition]

astype(np.int) int형식으로 바꿔줌.

fancy index
a[b], a는 값 b에는  인덱스가 주룩 나열된 어레이가 이씀
인덱스에 맞는 밸류를 넣은 어레이가 나옴
a.take(b) 같은 기능인데 이렇게 표현하는걸 추천함
매트릭스도 가능

기억할거
where, broadcasting, fancy index, argmax, argmin, boolean index
'''