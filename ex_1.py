
try:
    vel = int(input("розмір квадрату"))
    dov = int(input("розмір квадрату"))
    for i in range(vel):
        for j in range(dov):
            print(f'*', end=" ")
        print()
except Exception as ex:
    print(f"error information:{ex}")
finally:
    print("exit")