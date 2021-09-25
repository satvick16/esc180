def get_adj_grade(grade):
    return grade - 5


if __name__ == '__main__':
    grade = 95
    grade = get_adj_grade(grade)
    print("new grade outside function:", grade)  # 90
