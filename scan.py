n=int(input("len: "))
queue=[]
s=int(input("start value: "))
a=input("data: ")
distance=0
queue.append(s)
for i in range(n):
    queue.append(int(a.split(" ")[i]))
cnt=s
left_status=0
while(1):
    if queue == []:
        break
    if cnt == 0:
        left_status = 1
    cnt += -1 if left_status == 0 else 1
    distance += 1
    if cnt in queue:
        queue.remove(cnt)
print(distance)
