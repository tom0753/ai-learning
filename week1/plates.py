def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if len(s) > 6 or len(s) < 2:
        return False
    elif not s[0].isalpha() or not s[1].isalpha():
        return False
    elif not s.isalnum():
        return False
    
    found_digit = False
    for c in s:
        if c.isdigit():
            if c == "0":
                return False
            found_digit = True
        if found_digit and c.isalpha():
            return False


    return True


main()