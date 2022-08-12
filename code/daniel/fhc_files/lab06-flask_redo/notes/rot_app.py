english = ["a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z"]
rot13 = ["n,o,p,q,r,s,t,u,v,w,x,y,z,a,b,c,d,e,f,g,h,i,j,k,l,m"]


def eng_to_r13 ():
    english = ["a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z"]
    rot13 = ["n,o,p,q,r,s,t,u,v,w,x,y,z,a,b,c,d,e,f,g,h,i,j,k,l,m"]
    index = 0
    count = 0
    cipher = []
    user_input = input("Type a string that you wish to encode: ")
    for letter in user_input:
        if user_input[index] == english[count]:
            cipher.append(rot13[count])
    print(cipher)
    count +=1

eng_to_r13()