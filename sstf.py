n=int(input("len: "))
queue=[]
s=int(input("start value: "))
a=input("data: ")
distance=[]
queue.append(s)
for i in range(n):
    queue.append(int(a.split(" ")[i]))
near_value = lambda num,arr:min(arr,key=lambda x:abs(x-num))
for i in range(n):
    if i==0:
        tmp=s
        queue.remove(tmp)
        near = near_value(tmp,queue)
        distance.append(abs(tmp-near))
    else:
        tmp=near
        queue.remove(tmp)
        near = near_value(tmp,queue)
        distance.append(abs(tmp-near))
print(sum(distance))
