def main():
    times = get_number()
    meow(times)

def get_number():
    while True:
        n = int(input("Ile wynosi n? "))
        if n > 0:
            return n

def meow(n):
    for i in range(n):
        print("meow")


main()