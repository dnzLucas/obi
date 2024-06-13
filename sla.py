while(t > 0):
    s += t
    if (s > 59):
        s = 0
        if (t >= 60):
            t -= 60
            m += t
        else:
            m += t
            break
    else:
        break

    if(m > 59):
        m = 0
        if(t >= 60):
            t -= 60
            h += 1
        else:
            h+=1
            break

    else:
        break

    if (h > 23):
        h = 00
        if (t >= 60):
            t -= 60
    else:
        break