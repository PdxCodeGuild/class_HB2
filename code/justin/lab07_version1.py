'''
Justin Young
Lab 07
Version1
'''



def cc_v(cc):
    cc_1 = []
    for x in cc:
        x = int(x)
        cc_1.append(x)
    # print(cc_1)
    check_d = cc_1.pop(-1)
    cc_1.reverse()
    # print(f'{cc_1} should be flipped')
    for i, item in enumerate(cc_1):
        if i % 2 == 0:
            cc_1[i] = item * 2
    # print(cc_1)
    for i, item in enumerate(cc_1):
        if item > 9:
            cc_1[i] = item - 9
    # print(cc_1)
    sum = 0
    for c in cc_1:
        sum += c
    print(sum, check_d)
    if str(sum)[1] == str(check_d):
        return f'{True} Valid!'
    else:
        return f'{False} Not Valid'


a = input('Enter cc number: ')
print(cc_v(a))