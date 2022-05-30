n=int(input())
for i in range(n):
    p=list(map(float,input().split()))
    x1=p[0]
    y1=p[1]
    x2=p[2]
    y2=p[3]
    x3=p[4]
    y3=p[5]
    area=(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))
    if area>0:
        print(f"Area of rectangle with vertices({x1},{y1}),({x2},{y2}),({x3},{y3}) is",area)
    else:
        print(f"Area of rectangle with vertices({x1},{y1}),({x2},{y2}),({x3},{y3}) is",-1*area)
