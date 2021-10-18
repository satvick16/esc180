class Matrix:
    def __init__(self, arr):
        self.arr = arr

    def __str__(self) -> str:
        string = ""

        for i in range(len(self.arr) - 1):
            string += str(self.arr[i]) + "\n"

        string += str(self.arr[-1])

        return string

    def dot(row, col):
        result = 0

        for i in range(len(row)):
            result += row[i] * col[i]

        return result

    @staticmethod
    def can_multiply(m1, m2):
        return len(m1.arr[0]) == len(m2.arr)

    @staticmethod
    def multiply(m1, m2):
        if not Matrix.can_multiply(m1, m2):
            return None

        result = [[0 for i in range(len(m1.arr))]
                  for j in range(len(m2.arr[0]))]

        for i in range(len(m1.arr)):
            for j in range(len(m2.arr[0])):
                result[i][j] = Matrix.dot(
                    m1.arr[i], [m2.arr[x][j] for x in range(len(m2.arr))])

        return Matrix(result)


def main():
    arr1 = [[1, 2, 3], [4, 5, 6]]
    m1 = Matrix(arr1)

    arr2 = [[7, 8], [9, 10], [11, 12]]
    m2 = Matrix(arr2)

    res = Matrix.multiply(m1, m2)

    print(res)


if __name__ == "__main__":
    main()
