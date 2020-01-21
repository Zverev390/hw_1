#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_10():
    while wall_is_above():
        move_right()
    move_up()
    while not wall_is_on_the_right():
            move_right()
            while not wall_is_beneath():
                fill_cell()
    move_down()
    while wall_is_beneath():
        move_left()
    move_down()
    while not wall_is_above():
        fill_cell()
        
    pass


if __name__ == '__main__':
    run_tasks()
