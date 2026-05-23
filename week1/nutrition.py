item = input("Item: ").lower()
fruits = {
    "apple" : 130,
    "banana" : 110,
    "pear" : 100,
    "strawberries" : 140,
}
if item in fruits:
    print(fruits[item])