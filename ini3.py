def StringSlice():
    while True:
        s = input("Please enter a string of at most 200 letters: ")
        try:
            s = str(s)
            if len(s) <= 200:
                break
            else:
                print("The string must be at most 200 letters.")
        except Exception:
            print("Input must be a string.")
            continue
    while True:
        a = input("Please enter your first integer: ")
        try:
            a = int(a)
            break
        except ValueError:
            print("Input must be an integer.")
            continue
    while True:
        b = input("Please enter your second integer: ")
        try:
            b = int(b)
            break
        except ValueError:
            print("Input must be an integer.")
            continue
    while True:
        c = input("Please enter your third integer: ")
        try:
            c = int(c)
            break
        except ValueError:
            print("Input must be an integer.")
            continue
    while True:
        d = input("Please enter your final integer: ")
        try:
            d = int(d)
            break
        except ValueError:
            print("Input must be an integer.")
            continue
    return(s[a:b+1] + " " + s[c:d+1])
