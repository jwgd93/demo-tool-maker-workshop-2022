def Hypothenuse():
    while True:
        a = input("Please enter an integer less than 1000: ")
        try:
            a = int(a)
            if a < 1000:
                break
            else:
                print("The integer must be less than 1000.")
        except ValueError:
            print("Please enter an integer.")
            continue
    while True:
        b = input("Please enter another integer less than 1000: ")
        try:
            b = int(b)
            if b < 1000:
                break
            else:
                print("The integer must be less than 1000.")
        except ValueError:
            print("Please enter an integer.")
            continue
    return(a**2 + b**2)
