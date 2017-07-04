# -*- coding: utf-8 -*-
import multiprocessing, threading, os, time
from multiprocessing import Manager

cpu_count = 4

shared = Manager().Namespace()
shared.flag = True
#
# def task():
#     print "[%s] start" % (os.getpid())
#     while shared.flag:
#         print "[%s] is running" % os.getpid()
#         time.sleep(3)
#
def stop(t):
    print "stop process[%s] start" % os.getpid()
    time.sleep(int(t))
    shared.flag = False
    print "stop all process"
#
# if __name__ == '__main__':
#     p = multiprocessing.Pool(cpu_count)
#     print "father[%s]" % (os.getpid())
#     for i in range(cpu_count - 1):
#         p.apply_async(task)
#     p.apply_async(stop, args=(10, ))
#     p.close()
#     p.join()
#     print "end"

def process_task():
    pid = os.getpid()
    for i in range(2):
        t = threading.Thread(target=task, name= str(pid) + "|" + str(i))
        t.start()
    time.sleep(5)

def task():
    print "[%s] start" % (threading.current_thread().name)
    while shared.flag:
        print "[%s] is running" % (threading.current_thread().name)
        time.sleep(2)

if __name__ == '__main__':
    p = multiprocessing.Pool(cpu_count + 1)
    for i in range(cpu_count):
        p.apply_async(process_task)
    p.apply_async(stop, args=(10, ))
    p.close()
    p.join()




