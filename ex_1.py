
try:
    vel = int(input("розмір квадрату"))
    for i in range(vel):
        for j in range(vel):
            print("*",and"")
            print(' ')
except Exception as ex:
    print(f"error information:{ex}")
finally:
    print("exit")