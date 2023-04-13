# get two integer parameters
# return sum
def plus(x, y):
    return x+y

# main function
def main():
    check = 1
    print("Welcome to calcuator")
    while check >= 1:
        try:
            print("0: exit, 1: plus")
            check = int(input())
            if check == 1:
                print("First Number")
                x = float(input())
                print("Second Number")
                y = float(input())
                print("answer : ", plus(x,y))
            elif check > 1:
                print("Unsupported")
            else:
                print("Thank you")
        except valueError:
            print("제대로 된 숫자를 입력하세요")

if __name__ == "__main__":
    main()
