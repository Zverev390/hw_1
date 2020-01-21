#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.0002)
def task_1_1():
    move_down()
    move_right(2)
    pass


if __name__ == '__main__':
    run_tasks()
