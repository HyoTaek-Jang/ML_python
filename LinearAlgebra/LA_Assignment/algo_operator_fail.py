
if __name__ == "__main__":
    num = int(input('총 수 : '))
    num_value = [int(a) for a in input('각 수의 값 : ').split(' ')]
    num_operator = [int(a) for a in input('각 부호 + - * / : ').split(' ')]

    num_value.sort()


    def cal_max(num_value, num_op):
        max = 0
        num_operator = num_op[:]
        for i in range(num):
            if i==0:
                max = num_value[0]

            # 부호 -
            if(num_operator[1] != 0):
                max = num_value[i+1] - max
                num_operator[1] -= 1
            # 부호 /
            elif (num_operator[3] != 0):
                if(max==0):
                    max = 0
                else:
                    max = max // num_value[i+1]
                num_operator[3] -= 1
            # 부호 +
            elif(num_operator[0] != 0):
                max = num_value[i+1] + max
                num_operator[0] -= 1
            # 부호 *
            elif(num_operator[2] != 0):
                max =max * num_value[i+1]
                num_operator[2] -= 1

        return max

    def cal_min(num_value, num_operator):
        min = 0

        for i in range(num):
            if i == 0:
                min = num_value[0]

            # 부호 +
            if (num_operator[0] != 0):
                min = num_value[i + 1] + min
                num_operator[0] -= 1
            # 부호 /
            elif (num_operator[3] != 0):
                if (min == 0):
                    min = 0
                else:
                    min = min // num_value[i + 1]
                num_operator[3] -= 1
            # 부호 -
            elif (num_operator[1] != 0):
                min =  min - num_value[i + 1]
                num_operator[1] -= 1
            # 부호 *
            elif (num_operator[2] != 0):
                min = min * num_value[i + 1]
                num_operator[2] -= 1

        return min


    print(num, num_value, num_operator)
    print(cal_max(num_value, num_operator),cal_min(num_value,num_operator))