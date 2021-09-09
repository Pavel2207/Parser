def check_password(p):
    b = 0
    s = 0
    d = 0
    if len(p) >= 10:
        for i in p:
            if i in '0123456789':
                b = b + 1
            if i in '!@#$%*':
                s = s + 1
            if i.isupper() == True:
                d = d + 1
        if b >= 3 and s >= 1 and d >= 1:
            print("Perfect password")
        else:
            print("Easy peasy")

    else:
        print("Easy peasy")
