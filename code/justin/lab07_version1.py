'''
Justin Young
Lab 07
Version1
'''

from lzma import CHECK_CRC32


def cc_v(cc):
    cc_1 = []
    for x in cc:
        x = int(x)
        cc_1.append(x)
    print(cc_1)
    check_d = cc_1.pop(-1)
    cc_1.reverse()
    cc_2 = cc_1.copy()
    cc_3 = []
    for m in cc_2[::2]:
        indx = cc_2.index(m)
        print(indx)
        m *= 2
        cc_3[indx] = m
    print(cc_3)
    # cc_3 = cc_1.copy()
    # for s in cc_3:
    #     if s > 9:
    #         idx = cc_3.index(s)
    #         s -= 9
    #         cc_1[idx] = s
    # print(cc_1)
    # cc_4 = cc_1.copy()
    # sum = 0
    # for a in cc_4:
    #     sum += a
    # print(sum)
    # if sum == check_d:
    #     return f'Valid! {True}'
    # else:
    #     return f'Not Valid {False}'




a = input('Enter cc number: ')
print(cc_v(a))