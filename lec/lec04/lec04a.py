a = 5
b = 6

a1, a2 = 2, 3

# swapping values
a, b = b, a

temp = a
a = b
b = temp

# swapping values without using temp or multiple assignments
b = a + b
a = b - a
b = b - a

#######################################

# type: int, float, str, bool
int(3.14)  # = 3
int(3.75)  # = 3 as well

float(3)  # = 3.0

str(3.14)  # = "3.14"

approx_pi = 3.14
s1 = "the value of pi is approx. " + str(approx_pi)

float("3.14")  # = 3.14
int("5")  # = 5

int("3.14")  # not allowed
int(float("3.14"))  # allowed

# anything that's not "" or 0 is True, and "" and 0 are False
if "abc":
    print("hi")
