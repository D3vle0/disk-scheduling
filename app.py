from flask import Flask, render_template, request
import timeit
app=Flask(__name__)

@app.route('/')
def init():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def post():
    start = timeit.default_timer()
    fcfs_distance = fcfs(request.form['current_track'], request.form['queue'])
    sstf_distance = sstf(request.form['current_track'], request.form['queue'])
    scan_distance = scan(request.form['current_track'], request.form['queue'])
    c_scan_distance = scan(request.form['current_track'], request.form['queue'])
    look_distance = scan(request.form['current_track'], request.form['queue'])
    c_look_distance = scan(request.form['current_track'], request.form['queue'])
    end = timeit.default_timer()
    time=end-start
    return render_template('index.html', fcfs=fcfs_distance, sstf=sstf_distance, scan=scan_distance, c_scan=c_scan_distance, look=look_distance, c_look=c_look_distance, timer = round(time,6))

def fcfs(current_track_input, queue_input):
    queue_input = queue_input.strip()
    n=queue_input.count(" ")+1
    queue=[]
    s=current_track_input
    distance=[]
    queue.append(int(s))
    for i in range(n):
        queue.append(int(queue_input.split(" ")[i]))
    for i in range(n):
        distance.append(abs(queue[i]-queue[i+1]))
    print(sum(distance))
    return sum(distance)

def sstf(current_track_input, queue_input):
    queue_input = queue_input.strip()
    n=queue_input.count(" ")+1
    queue=[]
    s=current_track_input
    distance=[]
    queue.append(int(s))
    for i in range(n):
        queue.append(int(queue_input.split(" ")[i]))
    near_value = lambda num,arr:min(arr,key=lambda x:abs(x-num))
    for i in range(n):
        if i==0:
            tmp=int(s)
            queue.remove(tmp)
            near = near_value(tmp,queue)
            distance.append(abs(tmp-near))
        else:
            tmp=near
            queue.remove(tmp)
            near = near_value(tmp,queue)
            distance.append(abs(tmp-near))
    print(sum(distance))
    return sum(distance)

def scan(current_track_input, queue_input):
    queue_input = queue_input.strip()
    n=queue_input.count(" ")+1
    queue=[]
    s=current_track_input
    distance=0
    queue.append(int(s))
    for i in range(n):
        queue.append(int(queue_input.split(" ")[i]))
    cnt=int(s)
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
    return distance

def c_scan(current_track_input, queue_input):
    queue_input = queue_input.strip()
    n=queue_input.count(" ")+1
    queue=[]
    s=current_track_input
    distance=[]
    for i in range(n):
        queue.append(int(queue_input.split(" ")[i]))
    cnt=int(s)
    distance=0
    while(1):
        if queue == []:
            break
        if cnt < 199:
            cnt += 1
            distance += 1
        else:
            cnt = 0
            distance += 199
        if cnt in queue:
            queue.remove(cnt)
    print(distance)
    return distance

def look(current_track_input, queue_input):
    queue_input = queue_input.strip()
    n=queue_input.count(" ")+1
    queue=[]
    s=current_track_input
    distance=0
    queue.append(s)
    for i in range(n):
        queue.append(int(queue_input.split(" ")[i]))
    cnt=int(s)
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
            left_status = 1
    print(distance)
    return distance

def c_look(current_track_input, queue_input):
    queue_input = queue_input.strip()
    n=queue_input.count(" ")+1
    queue=[]
    s=current_track_input
    distance=[]
    for i in range(n):
        queue.append(int(queue_input.split(" ")[i]))
    cnt=int(s)
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
    return distance



if __name__ == '__main__':
    app.run()
