import math
import random
import time


keys = 0
step = 0
for i in range(8, 4097):

    if (math.log(i, 2)) % 1 != 0:
        continue
    else:
        step = i
        keys = math.log(step, 2)
        keys = int(step ** keys)      #кількість варіантів ключів для послідовностей різної бітності
        r_key = 0
        for r in range(keys):
            r_key = int(random.getrandbits(step))    #випадкове значення ключа для кожного з варіантів

            def key_mean():
                start = time.monotonic_ns()
                print(start)
                k = 0
                while k != r_key:
                    k += 1
                    continue
                print(k)
                finish = time.monotonic_ns()
                print(finish)
                duration = finish - start
                print(f"That took {duration // 1000000}ms")     #час,витрачений для знаходження ключа
            key_mean()

