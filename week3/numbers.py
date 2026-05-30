def main():
    x = get_int()
    print(f"x wynosi {x}")

def get_int():
    while True:
        try:
            x = int(input("Podaj x: "))
            return x
        except ValueError:
            print("x nie jest integerem")
        else:
            break
main()



