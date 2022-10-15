import sys
try:
    num_1 = int(input("розмір квадрату"))
    for width in range(num_1):
        for long in range(num_1):
            if width == 0 or long == 0 or width == num_1-1 or long == num_1-1:
                sys.stdout.write("*")
            else:
                sys.stdout.write(" ")
        print(' ')
except Exception as ex:
    print(f"error information:{ex}")
finally:
    print("exit")