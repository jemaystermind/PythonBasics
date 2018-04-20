
def solve(equation):
    x, operator, num_1, equals, num_2 = str(equation).split()
    num_1, num_2 = int(num_1), int(num_2)
    return num_2 - num_1

equation = input("Enter addition equation: ")

print("X =", solve(equation))
