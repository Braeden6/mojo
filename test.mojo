from python import Python
from sys import argv
import time
from utils.list import Dim


fn recursive_fib(n: Int) -> Int:
    if n <= 1:
        return n
    else:
        return recursive_fib(n-1) + recursive_fib(n-2)

fn fib(n: Int)  -> Int:
    var a = 0
    var b = 1
    for i in range(n):
        a,b = b, a+b
    return a

struct Results:
    var result: Int
    var time: Int

    fn __init__(inout self, result: Int, time: Int):
        self.result = result
        self.time = time

fn get_result(func: String, value: Int) -> Results:
    let start: Int = time.now()
    if func == 'recursive_fib':
        return Results(recursive_fib(value), time.now() - start)
    elif func == 'fib':
        return Results(fib(value), time.now() - start)
    else:
        return Results(0, time.now() - start)


def main():
    let args = argv()
    let function = args[2]
    let value: Int = atol(args[1])

    let result = get_result(function, value)
    print('Took', result.time / 1000000, 'mili seconds to calculate fib of', value, 'which is', result.result)
    


    

    



    