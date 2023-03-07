'''a program that has a function called counter(), which takes three parameters: start, end and step. 
Your program has to perform three counts through the created function:'''
import time

def counter(start, end, step):
    if step < 0:
        step *= -1
    if start < end:
        count = start
        while count <= end:
            print(f'{count} ', end='', flush=True)
            count += step
            time.sleep(1)
    else:
        count = start
        while count >= end:
            print(f'{count} ', end='', flush=True)
            count -= step
            time.sleep(1)

print('Count from 1 to 10 in steps of 1:')
counter(1, 10, 1)

print('\nCount from 10 to 0 in steps of 2:')
counter(10, 0, 2)

print('\nCount from -10 to -20 in steps of -2:')
counter(-10, -20, -2)