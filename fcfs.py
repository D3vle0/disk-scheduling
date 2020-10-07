n=int(input("len: "))
queue=[]
s=int(input("start value: "))
a=input("data: ")
distance=[]
queue.append(s)
for i in range(n):
    queue.append(int(a.split(" ")[i]))
for i in range(n):
    distance.append(abs(queue[i]-queue[i+1]))
print(sum(distance))
