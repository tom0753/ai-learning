def main():
    times=int(input("ile razy kot miauczy: "))
    meow(times)

def meow(n):
    for i in range(n):
        print("meow")
main()