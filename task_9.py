#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_2():
    while not cell_fill():
        cell_fill()
        while not wall_is_on_the_left():
            move_left()
    
        
    pass


if __name__ == '__main__':
    run_tasks()
