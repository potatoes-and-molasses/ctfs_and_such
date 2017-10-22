F = Zmod(93556643250795678718734474880013829509320385402690660619699653921022012489089)
B 




for p, k in factor(E.order()):

    f = p ** k
    nbase = base * (E.order() // f)
    nres = res * (E.order() // f)

    if b // (step - start) < f:
        bounds = (start, start + b // (step - start))
    else:
        bounds = (0, f)

    r = bsgs(nbase, nres, bounds, operation='+')

    start = crt(start, r, step, f)

    step *= f

print(start)