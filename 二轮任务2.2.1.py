import time
import cv2
import os
import glob
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
import math

n=1000000

folder_path=r"C:\Users\TreeMan\PycharmProjects\PythonProject\data"
image_paths=sorted(glob.glob(os.path.join(folder_path,"*.jpg")))
def func1(args):
    start,end=args
    total=0
    for i in range(start,end+1):
        total+= math.sqrt(i)+i**2
    return total
def func2(img_path):
    return cv2.imread(img_path)
def single_thread1():
        s=[0,n]
        func1(s)
def multi_thread1():
    chunk_size = n // 5
    ranges = [(i, i + chunk_size - 1) for i in range(0, n, chunk_size)]
    if ranges[-1][1] < n: ranges[-1] = (ranges[-1][0], n)
    with ThreadPoolExecutor(max_workers=5) as pool:
        sum((pool.map(func1,ranges)))
def multi_process1():
    chunk_size = n // 5
    ranges = [(i, i + chunk_size - 1) for i in range(0, n, chunk_size)]
    if ranges[-1][1] < n: ranges[-1] = (ranges[-1][0], n)
    with ProcessPoolExecutor(max_workers=5) as pool:
        sum((pool.map(func1, ranges)))
def single_thread2():
    for img_path in image_paths:
        img=func2(img_path)
def multi_thread2():
    with ThreadPoolExecutor(max_workers=8) as pool:
        (pool.map(func2,image_paths))
def multi_process2():
    with ProcessPoolExecutor(max_workers=8) as pool:
        (pool.map(func2, image_paths))
if __name__=="__main__":
    start=time.time()
    single_thread1()
    end=time.time()
    print("single_thread1:",end-start,"second")

    start = time.time()
    multi_thread1()
    end = time.time()
    print("multi_thread1:", end - start, "second")

    start = time.time()
    multi_process1()
    end = time.time()
    print("multi_process1:", end - start, "second")

    start = time.time()
    single_thread2()
    end = time.time()
    print("single_thread2:", end - start, "second")

    start = time.time()
    multi_thread2()
    end = time.time()
    print("multi_thread2:", end - start, "second")

    start = time.time()
    multi_process2()
    end = time.time()
    print("multi_process:", end - start, "second")



