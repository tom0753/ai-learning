def main():
    liczba = int(input("Podaj liczbe: "))
    if czyparzysta(liczba):
        print("Parzysta")
    else:
        print("Nieparzysta")

def czyparzysta(n):
    return True if n % 2 == 0 else False

main()