def input_two_numbers():
    a=int(input("Enter 1st number?"))
    b=int(input("Enter 2nd number?"))
    return a,b
def add(a, b):
    return a+b


def output(a, b, sum):
    print(a,end="")
    print("+",end="")
    print(b,"is",sum)


def main():
    a, b = input_two_numbers()
    sum = add(a, b)

    output(a, b, sum)
main()
