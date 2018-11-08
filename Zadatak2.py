def recStep(nn, d):
    print(str(nn))
    if d < 0:
        if nn > 0:
            recStep(nn-m, d)
        else:
            recStep(nn+m, d * -1)
    else:
        if nn < n:
            recStep(nn+m, d)
        else:
            return


n = int(input("N: "))
m = int(input("M: "))

recStep(n, -1)