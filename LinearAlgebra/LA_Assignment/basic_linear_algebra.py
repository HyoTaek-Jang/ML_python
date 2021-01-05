def vector_size_check(*vector_variables):
    return len(set([len(matrix) for matrix in vector_variables])) == 1
# 처음에 a에 담아서 줬다가 가변인자로 돼있어 제대로 인자처리를 못해 문제가 발생. 가변인자의 형태로 전달하니 해결
a = [3,1],[1,1],[1,3]
print(vector_size_check([3,1],[1,1],[1,2]))

def vector_addition(*vector_variables):
    # print(vector_variables)
    # print(*vector_variables)
    # print(list(zip(vector_variables)))
    # print(list(zip(*vector_variables)))
    return [sum(ele) for ele in zip(*vector_variables)]

print(vector_addition([3,1],[1,1],[1,2]))

def vector_subtraction(*vector_variables):
    if vector_size_check(*vector_variables) == False:
        raise ArithmeticError
    return [2*a-b for a,b in zip(vector_variables[0] ,[sum(ele) for ele in zip(*vector_variables)])]

print(vector_subtraction([3,1],[1,1],[1,2]))

def scalar_vector_product(alpha, vector_variable):
    return [alpha*a for a in vector_variable]

print(scalar_vector_product(5,[1,2,3]))


def matrix_size_check(*matrix_variables):
    return len(set([len(matrix) for matrix in matrix_variables])) == 1 and len(set([len(matrix[0]) for matrix in matrix_variables])) == 1

a = [[2,3],[2,2]]
b = [[2,3],[2,2]]

print(matrix_size_check(a,b))

def is_matrix_equal(*matrix_variables):
    # 아래 함수에 인자로 넘기면 튜플이 또 감싸져서 함수가 제대로 작동을 안함.
    if matrix_size_check(*matrix_variables) == False:
        raise ArithmeticError
    # return all([ set(ele) == 1 for row in matrix_variables for ele in zip(*row) for ele in zip(*ele)])
    return all([ len(set(ele))==1 for matrix in matrix_variables for row in zip(*matrix) for ele in zip(*row)])

print(is_matrix_equal((a,b)))

def matrix_addition(*matrix_variables):
    if matrix_size_check(*matrix_variables) == False:
        raise ArithmeticError
    return [[sum(b) for b in zip(*a)] for a in zip(*matrix_variables)]

print(matrix_addition(a,b))

def matrix_subtraction(*matrix_variables):
    if matrix_size_check(*matrix_variables) == False:
        raise ArithmeticError
    return [[2*b[0]-sum(b) for b in zip(*a)] for a in zip(*matrix_variables)]

a = [[9,3],[9,2]]
b = [[1,2],[1,2]]
c = [[5,7],[2,1]]

print(matrix_subtraction(a,b,c))

def matrix_transpose(matrix_variable):
    return [[*a] for a in zip(*matrix_variable)]

a = [[9,3],[9,2],[1,1],[7,7]]

print(matrix_transpose(a))

def scalar_matrix_product(alpha, matrix_variable):
    return [[alpha*b for b in a]for a in matrix_variable]

print(scalar_matrix_product(5,a))

def is_product_availability_matrix(matrix_a, matrix_b):
    print(len([b for b in zip(*matrix_b)][0]))
    print(len(matrix_a))
    return len(matrix_a[0]) == len([b for b in zip(*matrix_b)][0])
    # return len(set(zip(*matrix_b[0],zip(matrix_a)[0]))) == 1

d= [[1,2],[2,2],[3,3],[1,1]]
print(is_product_availability_matrix(a,d))


def matrix_product(matrix_a, matrix_b):
    if is_product_availability_matrix(matrix_a, matrix_b) == False:
        raise ArithmeticError
    return [[sum([c*d for c,d in zip(a,b)]) for b in zip(*matrix_b)] for a in matrix_a]
f = [[1,1,2],[2,1,1]]
g = [[2,4],[5,3],[1,3]]

print(matrix_product(f,g))
