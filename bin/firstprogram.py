import sys
def addition(a, b):
    return a + b
def multiplication(a, b):
    return a * b
def subtraction(a, b):
    return a - b
def division(a, b):
    return a / b
def main():
    sum_value = addition(10, 30)
    print(sum_value)

    mul_value = multiplication(10, 30)
    print(mul_value)

    sub_value = subtraction(10, 30)
    print(sub_value)

    div_value = division(30, 10)
    print(div_value)
if __name__ == '__main__':
    print("calling main fucntion....")
    main()