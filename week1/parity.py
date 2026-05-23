def main():
    liczba = int(input("Podaj liczbe: "))
    if czyparzysta(liczba):
        print("Parzysta")
    else:
        print("Nieparzysta")
def czyparzysta(n):
    if n % 2 == 0:
        return True
    else:
        return False



main()