
import queue 
import threading
import time

task_list = queue.Queue()

def add(x,y):
    return receive_task(task_add, x, y)

def task_add(x, y):
    return x + y

def receive_task(task_name, *args, **kwargs):
    task_list.put(task_name(*args, **kwargs))

# while True:
#     if task_list.empty():
#         time.sleep(0.1)
#         continue
#     do_task = threading.Thread(target=task_list.get())
#     do_task.start()