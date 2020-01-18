#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_7():
    while not  wall_is_above() and not wall_is_beneath():
        move_right()
    while wall_is_above() or wall_is_beneath():
        move_right()

    pass


if __name__ == '__main__':
    run_tasks()
