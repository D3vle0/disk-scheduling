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
while(1):
    if queue == []:
        break
    if cnt < data['disk_max']:
        cnt += 1
        distance += 1
    else:
        cnt = 0
        distance += data['disk_max']
    if cnt in queue:
        queue.remove(cnt)
print(distance)
