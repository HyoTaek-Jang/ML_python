# Vector representation of python
# 리스트 튜플 딕트로 표현가능
# 리스트 곱셈
u = [1,2,3]
v = [4,5,6]
print([sum(z) for z in zip(u,v)])

#매트릭스는 TWO dimensional로 표현함
matrix_a = [[1,2],[3,4]]
matrix_b = [[3,2],[7,7]]
result = [[sum(row)for row in zip(*p)] for p in zip(matrix_a,matrix_b)]
print((result))
#매트릭스 역함수
matrix_c = [[1,2,3],[4,5,6]]
result = [[ele for ele in i]for i in zip(*matrix_c)]
result1 = [i for i in zip(*matrix_c)]

print(result)
print(result1)
# 매트릭스 곱.... 어렵다 복습해야할듯
A = [[1,2,3],[4,5,6]]
B = [[1,4],[2,5],[3,6]]

C = [[sum(row1*col1 for row1, col1 in zip(row, col))for row in A] for col in zip(*B)]
print(C)

# 컴퓨터에서 유사하다 = 가깝다.
# 가깝다는 걸 알려면 숫자를 벡터로 바꿔줘야함. 두 백터사이의 거리를 알아냄.

# 문자를 백터로 만드는 법 , One-hot Encoding
# 하나의 단어를 백터의 인덱스로 인식. 단어 존재시 1 없으면 0
# bag of words

#유사성? 피타고라스 정의로 거리를 구하면 됨. or cosine distatnce : 두 점 사이의 각도를 측정 // 이걸 조금 더 많이씀

#80여개의 뉴스 기사를 가져와서 분류하기
'''
process
1. 파일 불러오기
2. 파일 읽어서 단어사전(corpus) 만들기
3. 단어별 index 만들기
4. 만들어진 인덱스로 문서별로 bag or words vector 생성
5. 비교하고자 하는 문서 비교하기
6. 얼마나 맞는지 측정하기
'''