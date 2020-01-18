#!/usr/bin/python3

from pyrob.api import *


@task
def task_3_3():
    if not wall_is_on_the_right():
        elif move_right()
    if not wall_is_above():
        else move_up()
    if not wall_is_on_the_left():
        else move_left()
    if not wall_is_beneath():
        else move_down()
        
    pass


if __name__ == '__main__':
    run_tasks()
