import random
def make_ranndom_int(num,lb,up):
    rand = random.Random()
    result = []
    for i in range(num):
        while True:
            candidate = rand.randrange(lb,up)
            if candidate in result:
                break
            result.append(candidate)
        return result

print(make_ranndom_int(5,1,13))