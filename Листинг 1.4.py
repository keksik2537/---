import time
import multiprocessing
import os
import datetime

def hello_from_process_1():
 print(f'Привет от дочернего процесса 1 {os.getpid()}!')
 time.sleep(10)
def hello_from_process_2():
 print(f'Привет от дочернего процесса 2 {os.getpid()}!')
 time.sleep(10)
def hello_from_process_3():
 print(f'Привет от дочернего процесса 3 {os.getpid()}!')
 time.sleep(10)
def hello_from_process_4():
 print(f'Привет от дочернего процесса 4 {os.getpid()}!')
 time.sleep(10)
def hello_from_process_5():
 print(f'Привет от дочернего процесса 5 {os.getpid()}!')
 time.sleep(10)
def hello_from_process_6():
 print(f'Привет от дочернего процесса 6 {os.getpid()}!')
 time.sleep(10)
def hello_from_process_7():
 print(f'Привет от дочернего процесса 7 {os.getpid()}!')
 time.sleep(10)
def hello_from_process_8():
 print(f'Привет от дочернего процесса 8 {os.getpid()}!')
 time.sleep(10)
def hello_from_process_9():
 print(f'Привет от дочернего процесса 9 {os.getpid()}!')
 time.sleep(10)
def hello_from_process_10():
 print(f'Привет от дочернего процесса 10 {os.getpid()}!')
 time.sleep(10)
def hello_from_process_11():
 print(f'Привет от дочернего процесса 11 {os.getpid()}!')
 time.sleep(10)
def hello_from_process_12():
 print(f'Привет от дочернего процесса 12 {os.getpid()}!')
 time.sleep(10)
def hello_from_process_13():
 print(f'Привет от дочернего процесса 13 {os.getpid()}!')
 time.sleep(10)
def hello_from_process_14():
 print(f'Привет от дочернего процесса 14 {os.getpid()}!')
 time.sleep(10)
def hello_from_process_15():
 print(f'Привет от дочернего процесса 15 {os.getpid()}!')
 time.sleep(10)

start=datetime.datetime.now()

if __name__ == '__main__':
 hello_process_1 = multiprocessing.Process(target=hello_from_process_1)
 hello_process_2 = multiprocessing.Process(target=hello_from_process_2)
 hello_process_3 = multiprocessing.Process(target=hello_from_process_3)
 hello_process_4 = multiprocessing.Process(target=hello_from_process_4)
 hello_process_5 = multiprocessing.Process(target=hello_from_process_5)
 hello_process_6 = multiprocessing.Process(target=hello_from_process_6)
 hello_process_7 = multiprocessing.Process(target=hello_from_process_7)
 hello_process_8 = multiprocessing.Process(target=hello_from_process_8)
 hello_process_9 = multiprocessing.Process(target=hello_from_process_9)
 hello_process_10 = multiprocessing.Process(target=hello_from_process_10)
 hello_process_11 = multiprocessing.Process(target=hello_from_process_11)
 hello_process_12 = multiprocessing.Process(target=hello_from_process_12)
 hello_process_13 = multiprocessing.Process(target=hello_from_process_13)
 hello_process_14 = multiprocessing.Process(target=hello_from_process_14)
 hello_process_15 = multiprocessing.Process(target=hello_from_process_15)
 hello_process_1.start()
 print(f'Привет от родительского процесса 1 {os.getpid()}')
 hello_process_1.join()
 hello_process_2.start()
 print(f'Привет от родительского процесса 2 {os.getpid()}')
 hello_process_2.join()
 hello_process_3.start()
 print(f'Привет от родительского процесса 3 {os.getpid()}')
 hello_process_3.join()
 hello_process_4.start()
 print(f'Привет от родительского процесса 4 {os.getpid()}')
 hello_process_4.join()
 hello_process_5.start()
 print(f'Привет от родительского процесса 5 {os.getpid()}')
 hello_process_5.join()
 hello_process_6.start()
 print(f'Привет от родительского процесса 6 {os.getpid()}')
 hello_process_6.join()
 hello_process_7.start()
 print(f'Привет от родительского процесса 7 {os.getpid()}')
 hello_process_7.join()
 hello_process_8.start()
 print(f'Привет от родительского процесса 8 {os.getpid()}')
 hello_process_8.join()
 hello_process_9.start()
 print(f'Привет от родительского процесса 9 {os.getpid()}')
 hello_process_9.join()
 hello_process_10.start()
 print(f'Привет от родительского процесса 10 {os.getpid()}')
 hello_process_10.join()
 hello_process_11.start()
 print(f'Привет от родительского процесса 11 {os.getpid()}')
 hello_process_11.join()
 hello_process_12.start()
 print(f'Привет от родительского процесса 12 {os.getpid()}')
 hello_process_12.join()
 hello_process_13.start()
 print(f'Привет от родительского процесса 13 {os.getpid()}')
 hello_process_13.join()
 hello_process_14.start()
 print(f'Привет от родительского процесса 14 {os.getpid()}')
 hello_process_14.join()
 hello_process_15.start()
 print(f'Привет от родительского процесса 15 {os.getpid()}')
 hello_process_15.join()

finish=datetime.datetime.now()

print(finish-start)
