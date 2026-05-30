try: 
    x = int(input("Podaj wartosc x: "))
    print(f"x wynosi {x}.")
except ValueError:
    print("x nie jest integerem!")