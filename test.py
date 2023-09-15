import numpy as np
from fastapi import FastAPI, APIRouter
import time
import subprocess
import sys
from functools import lru_cache

# router = APIRouter()

# @router.get("/")
# def read_root():
#     return {"Hello": "World"}



# app = FastAPI()
# app.include_router(router, prefix="/folder")

# @app.get("/")
# def read_root():
#     return {"Hello": "World"}


@lru_cache(maxsize=None)
def recursive_fib_with_caching(n):
    if n <= 1:
        return n
    else:
        return recursive_fib_with_caching(n-1) + recursive_fib_with_caching(n-2)

def recursive_fib(n):
    if n <= 1:
        return n
    else:
        return recursive_fib(n-1) + recursive_fib(n-2)
    
def fib(n):
    a,b = 0,1
    for i in range(n):
        a,b = b, a+b
    return a

def call_mojo(func: str, value: str):
    process = subprocess.Popen(
            [
                "./test",
                str(value),
                func,
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
    text = ""
    for char in iter(lambda: process.stdout.read(1), b""):
        text += char.decode("utf-8")
    print(f"Mojo Function: {func}", text, end="")

def call_python(func, value: str):
    start = time.time()
    result = func(value)
    end = time.time()
    print(f'Python Function: {func.__name__} Took {(end-start)*1000} mili seconds to calculate fib of {value} which is {result}')



value = int(sys.argv[1])

call_mojo("recursive_fib", value)
call_mojo("fib", value)

call_python(recursive_fib, value)
call_python(fib, value)
call_python(recursive_fib_with_caching, value)


    








