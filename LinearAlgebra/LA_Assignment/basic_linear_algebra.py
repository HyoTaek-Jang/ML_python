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

a= [[1,2,3],[1,1,1]]
b= [[2,2,2],[1,1,3],[1,2,3]]
print(matrix_size_check(a,b))

def is_matrix_equal(*matrix_variables):
    return None


def matrix_addition(*matrix_variables):
    if matrix_size_check(*matrix_variables) == False:
        raise ArithmeticError
    return None


def matrix_subtraction(*matrix_variables):
    if matrix_size_check(*matrix_variables) == False:
        raise ArithmeticError
    return None


def matrix_transpose(matrix_variable):
    return None


def scalar_matrix_product(alpha, matrix_variable):
    return None


def is_product_availability_matrix(matrix_a, matrix_b):
    return None


def matrix_product(matrix_a, matrix_b):
    if is_product_availability_matrix(matrix_a, matrix_b) == False:
        raise ArithmeticError
    return None
