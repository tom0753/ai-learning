def main():
    liczba = int(input("Podaj liczbe: "))
    if czyparzysta(liczba):
        print("Parzysta")
    else:
        print("Nieparzysta")

def czyparzysta(n):
    return n % 2 == 0

main()