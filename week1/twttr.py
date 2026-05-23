word = input("Input: ")
for c in word:
    if c not in "aeiouAEIOU":
        print(c, end="")
print()

