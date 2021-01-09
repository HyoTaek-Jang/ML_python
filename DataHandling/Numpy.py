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