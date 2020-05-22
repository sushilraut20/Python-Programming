def fibbo(num):
    a,b=0,1
    count=1

    while count<=num:
        yield a
        a,b=b,a+b
        count+=1

fibbo_series=fibbo(5)

for digit in fibbo_series:
    print(digit)