import sys
try:
    vel = int(input("розмір квадрату"))
    for i in range(vel):
        for j in range(vel):
            if i==0 or j==0 or i== vel-1 or j == vel-1:
                sys.stdout.write("*")
            else:
                sys.stdout.write(" ")
            print(' ')
except Exception as ex:
    print(f"error information:{ex}")
finally:
    print("exit")