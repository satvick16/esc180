# secret_num = 10
# temp = secret_num + 10
# temp = temp * 2
# temp = temp / 4
# answer = temp - secret_num / 2
# print(answer)

#######################################

# exam_grade = 99

# if exam_grade == 98:
#     print('i won the bet')
#     print('i am happy')
# elif exam_grade > 98:
#     print('i am happy')
# else:
#     print(':(')

# print("at least i'm not an artsci")

#######################################

# # compute the roots of the equation
# # ax^2 + bx + c

# import math

# a = 1
# b = 3
# c = 1

# disc = b**2 - 4*a*c

# if disc > 0:
#     r1 = (-b - math.sqrt(disc))/(2*a)
#     r2 = (-b + math.sqrt(disc))/(2*a)
#     print(r1, r2)
# elif disc == 0:
#     r = -b/(2*a)
#     print(r)
# else:
#     print('nor real roots')

#######################################

def f(x):
    return x*x


print(f(5))


def my_add(a, b):
    res = a + f(b)
    print("hi", res)
    return res


print(my_add(5, 2) * 10)
my_add(1, 2)
