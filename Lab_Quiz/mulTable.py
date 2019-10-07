def multiplication_table(n=12):
    for col in range(1,n+1):
        print('{:3}'.format(col),end = '\t')
    print()
    for col in range(1,n+1):
        print('{:3}'.format('---'), end = '\t')
    print()
    for row in range(1,13):
        for col in range(1,n+1):
            print('{:3}'.format(row*col),end = '\t')
        print()

multiplication_table(5)
