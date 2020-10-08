import json
with open("./setting.json", "r") as f:
    data = json.load(f)
n=int(input("len: "))
queue=[]
s=int(input("start value: "))
a=input("data: ")
distance=[]
for i in range(n):
    queue.append(int(a.split(" ")[i]))
cnt=s
distance=0
queue_min = min(queue)
queue_max = max(queue)
while(1):
    if queue == []:
        break
    if cnt < queue_max:
        cnt += 1
        distance += 1
    else:
        cnt = queue_min
        distance += queue_max-queue_min
    if cnt in queue:
        queue.remove(cnt)
print(distance)
