def compute_hcf(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i 
    return hcf


for i in range(int(input())):
    n=input()
    l=list(map(int,input().split()))
    ans_num=1
    ans_den=l[0]
    for j in l[1:]:
        ans_num=((ans_num*j)+ans_den)
        ans_den=ans_den*j
        x=compute_hcf(int(ans_num),int(ans_den))
        ans_num = ans_num/x
        ans_den=ans_den/x

    print(f"{int(ans_num)}/{int(ans_den)}")
