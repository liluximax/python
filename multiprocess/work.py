# -*- coding: utf-8 -*-
import multiprocessing, os, threading, time, main
import mysql.connector as db


class Worker(multiprocessing.Process):
    def __init__(self):
        print "init"
        multiprocessing.Process.__init__(self)

    def run(self):
        print "process[%s] start" % (os.getpid())
        jobs = []
        for i in range(3):
            name = str(os.getpid()) + "|" + str(i)
            t = threading.Thread(target=self.task, name=name)
            jobs.append(t)
            t.start()
        for t in jobs:
            t.join()

    def task(self):
        print "thread[%s]" % (threading.current_thread().name)
        self.insert()

    def insert(self):
        connect = db.connect(host="115.29.51.206", port=3306, user="root", password="llx")
        print "run insert"
        try:
            sql = "INSERT INTO study.test VALUES (1, 2, \"llx\");"
            cursor = connect.cursor()
            cursor.execute(sql)
            connect.commit()
            time.sleep(3)
        finally:
            connect.close()
