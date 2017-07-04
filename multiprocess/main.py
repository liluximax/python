# -*- coding: utf-8 -*-
import work, multiprocessing, time, threading
import mysql.connector as db


if __name__ == '__main__':
    for i in range(3):
        p = work.Worker()
        p.start()

