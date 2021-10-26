def mywage(time):
    return time * 10000 + ((time - 40) * 5000 if time - 40 > 0 else 0)


print(mywage(41))
