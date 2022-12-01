import multiprocessing
from multiprocessing import Process, Queue
from datetime import datetime
from typing import List
import os

def exponentiation(queue):
    while True:
        if queue.empty():
            continue
        number, pow = queue.get()
        exponent = number ** pow
        dateTime = datetime.now()
        summanumbers = sum(range(exponent + 1))
        with open("file.txt", "a", encoding='utf8') as file:
            file.write(str(dateTime) + " >> " + str(number) + " ^ " + str(pow) + " = " + str(exponent) + " сумма цифр от нуля до полученного числа (включительно) = " + str(summanumbers) + "\n")

if __name__ == '__main__':
    queue = multiprocessing.Queue()
    process = Process(target=exponentiation, args=(queue,))
    process.start()
    while True:
        print("Введите через пробел число и степень в которую нужно возвести данное число: ")
        try:
            str = input()
            number, pow = (str.split(' '))
            numbercel: int = int(number)
            powcel: int = int(pow)
            datatuple = [numbercel, powcel]
            queue.put(datatuple)
        except:
            print("Ошибка при вводе")