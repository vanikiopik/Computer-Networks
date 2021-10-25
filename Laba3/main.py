import socket
import threading
import time
student_1 = {1: "Kelenikov Ivan Andreevich",
             2: "024402",
             3: "None",
             4: [1, 2, 2, 5]}
student_2 = {1: "Dashkevich Evgeniy Nikolaevich",
             2: "124312",
             3: "2400",
             4: [2, 2, 3, 1]}
student_3 = {1: "Alexandrov Anton Dmitrievich",
             2: "073422",
             3: "None",
             4: [1, 3, 3, 4]}
student_4 = {1: "Mishel Kamerilov Igorevich",
             2: "024402",
             3: "22500",
             4: [5, 5, 1, 5]}
student_5 = {1: "Motya Egor Davidovich",
             2: "024212",
             3: "None",
             4: [5, 5, 5, 5]}


def func(a, b):
    print(a + b)


