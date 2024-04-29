import time
def my_sum(xs):
    sum = 0
    for v in xs:
        sum += v
    return sum
test_data = range(10000000)

t1 = time.perf_counter()
user_result = my_sum(test_data)
t2 = time.perf_counter()
print("User result = {0} (Time taken: {1:4f}sec)".format(user_result,t2-t1))
t3 = time.perf_counter()
Computer_result = sum(test_data)
t4 = time.perf_counter()
print("Computer result = {0} (Time taken: {1:4f}sec)".format(Computer_result,t4-t2))