#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.002)
def task_3_3():
    if not wall_is_on_the_right():
        move_right()
    elif not wall_is_above():
        move_up()
    elif not wall_is_beneath():
        move_down()
    elif not wall_is_on_the_left():
        move_left()
        
        

        
    pass


if __name__ == '__main__':
    run_tasks()
