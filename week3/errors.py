try: 
    x = int(input("Podaj wartosc x: "))
except ValueError:
    print("x nie jest integerem!")
else:
    print(f"x wynosi {x}.")