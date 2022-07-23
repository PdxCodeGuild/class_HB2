'''
Justin Young
Lab 03
Version3
'''



user_input = input('Enter a number 1-1999, or "done" to exit: ')
while user_input != 'done':
    try:
        int(user_input)
        user_input=int(user_input)
        break
        # if len(user_input) ==4:
        #     print('is 4 num long')
    except:
        user_input = input('Please try again: ')

def num_roman(user_num):
    value_r=['I','IV','V','IX','X','XL','L','XC','C','CD','D','CM','M','V']
    value_n=[1,4,5,9,10,40,50,90,100,400,500,900,1000]
    i=12
    conv_num =''
    if user_num == 0:
        return 'zero'
    while user_num!=0:
        if value_n[i] <= user_num:
            conv_num+=value_r[i]
            user_num-=value_n[i]
        else:
            i-=1
    return conv_num
    

print(num_roman(user_input))    


# if len(user_input)>=1:        
#     if int(user_input[-1]) <= 3:
#         ones=(value[1]*int(user_input[-1]))
#     elif int(user_input[-1])==4:
#         ones=value[int(user_input[-1])]
#     elif int(user_input[-1])==5:
#         ones=(value[5])
#     elif int(user_input[-1])>=6<=9:
#         ones=value[int(user_input[-1])]
#     print(ones)
# if len(user_input)==2:        
#     if int(user_input[-2])<=3:
#         tens=value[10]*int(user_input[0])
#     elif int(user_input[-2])==4:
#         tens=value[40]
#     elif int(user_input[-2])==5:
#         tens=(value[50])
#     elif int(user_input[-2])>=6<=9:
#         tens=value[int(user_input)]
#     print(tens+ones)


        
# # if int(user_input[-2])<=3:
# #     tens=(value[10]*int(user_input[-2]))
# # print(tens+ones)    