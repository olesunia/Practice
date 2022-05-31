def hex_in_littleEndian(val):
    res = ''
    if len(val) % 2 != 0:
        val = '0' + val

    for a in range(len(val) - 1, 0, -2):
        res += val[a - 1]
        res += val[a]
    by_vall = ''
    for i in res:
        if i == '0':
            k = '0000'
            by_vall = by_vall + k
        if i == '1':
            k = '0001'
            by_vall = by_vall + k
        if i == '2':
            k = '0010'
            by_vall = by_vall + k
        if i == '3':
            k = '0011'
            by_vall = by_vall + k
        if i == '4':
            k = '0100'
            by_vall = by_vall + k
        if i == '5':
            k = '0101'
            by_vall = by_vall + k
        if i == '6':
            k = '0110'
            by_vall = by_vall + k
        if i == '7':
            k = '0111'
            by_vall = by_vall + k
        if i == '8':
            k = '1000'
            by_vall = by_vall + k
        if i == '9':
            k = '1001'
            by_vall = by_vall + k
        if i == 'a' or i == 'A':
            k = '1010'
            by_vall = by_vall + k
        if i == 'b' or i == 'B':
            k = '1011'
            by_vall = by_vall + k
        if i == 'd' or i == 'D':
            k = '1101'
            by_vall = by_vall + k
        if i == 'e' or i == 'E':
            k = '1110'
            by_vall = by_vall + k
        if i == 'f' or i == 'F':
            g = '1111'
            by_vall = by_vall + g
        if i == 'c' or i == 'C':
            k = '1100'
            by_vall = by_vall + k

    by_vall = by_vall[::-1]
    sum = 0
    for h in range(len(by_vall) - 1, -1, -1):
        j = int(by_vall[h])
        l = int(j * (2 ** h))
        sum += l
    print(sum)




def hex_in_bigEndian(num):
    by_val = ''
    for i in num:
        if i == '0':
            k = '0000'
            by_val = by_val + k
        if i == '1':
            k = '0001'
            by_val = by_val + k
        if i == '2':
            k = '0010'
            by_val = by_val + k
        if i == '3':
            k = '0011'
            by_val = by_val + k
        if i == '4':
            k = '0100'
            by_val = by_val + k
        if i == '5':
            k = '0101'
            by_val = by_val + k
        if i == '6':
            k = '0110'
            by_val = by_val + k
        if i == '7':
            k = '0111'
            by_val = by_val + k
        if i == '8':
            k = '1000'
            by_val = by_val + k
        if i == '9':
            k = '1001'
            by_val = by_val + k
        if i == 'a' or i == 'A':
            k = '1010'
            by_val = by_val + k
        if i == 'b' or i == 'B':
            k = '1011'
            by_val = by_val + k
        if i == 'd' or i == 'D':
            k = '1101'
            by_val = by_val + k
        if i == 'e' or i == 'E':
            k = '1110'
            by_val = by_val + k
        if i == 'f' or i == 'F':
            g = '1111'
            by_val = by_val + g
        if i == 'c' or i == 'C':
            k = '1100'
            by_val = by_val + k

    by_val = by_val[::-1]
    sum = 0
    for h in range(len(by_val) - 1, -1, -1):
        j = int(by_val[h])
        l = int(j * (2 ** h))
        sum += l
    print(sum)



def mean_16(num):
    i = num // 16
    k = num % 16
    number = []
    while (i >= 16):
        number = number + [k]
        k = i % 16
        i = i // 16
    number = number + [k]
    number = number + [i]

    little_and_big_Endian_in_hex(number)

def little_and_big_Endian_in_hex(number):
    hex_num = ''
    for b in number:
        if b == 10:
            d = 'A'
            hex_num += d
        if b == 11:
            d = 'B'
            hex_num += d
        if b == 12:
            d = 'C'
            hex_num += d
        if b == 13:
            d = 'D'
            hex_num += d
        if b == 14:
            d = 'E'
            hex_num += d
        if b == 15:
            d = 'F'
            hex_num += d
        elif b < 10:
            hex_num += str(b)
    hex_num = hex_num[::-1]
    print(hex_num)





def main():
    value = input('Введіть hex значення: ')
    little_End = int(input('Введіть ціле значення Little Endian: '))
    big_End = int(input('Введіть ціле значення Big Endian: '))


    print('Little-endian: ', end = "")
    hex_in_littleEndian(value)
    print('Big-endian: ', end = "")
    hex_in_bigEndian(value)
    print('Hex from Little-endian: ', end = "")
    mean_16(little_End)
    print('Hex from Big-endian: ', end = "")
    mean_16(big_End)



main()