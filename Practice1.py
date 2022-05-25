import random
import time

for i in range(3,13):
    bit_s = 2**i                                  #біти
    keys = bit_s**i                               #кількість варіантів ключів
    for k in range(1,keys+1):
        rand_key = int(random.getrandbits(bit_s)) #випадкове значення ключа,що залежить від довжини ключа
        def key_mean():
            start = time.monotonic_ns()
            print(start)
            k = 0
            while k != rand_key:
                k += 1
                continue
            print(k)
            finish = time.monotonic_ns()
            print(finish)
            duration = finish - start
            print(f"That took {duration // 1000000}ms")   #кількість часу в мілісекундах,яка була витрачена
                                                          #для знаходження ключа
        key_mean()








