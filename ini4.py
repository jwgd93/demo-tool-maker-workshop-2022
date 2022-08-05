def SumOddInts(a,b):
    if (a!= int(a) or b != int(b)):
        print("Inputs must both be integers.")
    elif (a >= b):
        print("First integer must be less than second integer.")
    elif (b >= 10000):
        print("Second integer must be less than 10,000.")
    else:
        out = 0
        for num in range(a,b):
            if num % 2 == 1:
                out = out + num
            else:
                continue
        return out
