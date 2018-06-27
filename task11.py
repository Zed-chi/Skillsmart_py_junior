"""
thread handling task
threading module
"""

from threading import Thread
import random, time

##сформировать массив
nums = [random.randint(1,100) for i in range(10000)]

##обычное суммирование
def sum(arr):
    sum = 0
    for i in arr:
        sum+=i
    return {"normal":sum}

##потоковое суммирование
def thr_sum(threads, nums):
    thread_list = []
    ##    определить часть массива каждой функции
    step = len(nums)/threads
    ost = len(nums)%threads
    end = step
    start = 0
    starts = []
    ends = []
    for i in range(threads):
        starts.append(int(start))
        ends.append(int(end))
        start+=step
        end+=step
    ends[len(ends)-1]+=ost
    results = {}
    print(ends, starts)

    ##сама обработка
    def process(id,nums):
        sum = 0
        for i in nums:
            sum+=i
        results[id] = sum
        time.sleep(0.05)

    ##определение потоков
    def start():
        for i in range(threads):
            t_name = 'Thread N {}'.format(i+1)
            id  = "id{}".format(i+1)
            thread_list.append(Thread(target=process, name=t_name, args=(id,nums[starts[i]:ends[i]])))
        for i in thread_list:
            i.start()

    ###пуск работы
    start()

    ###проверка конца работы потоков
    while(True):
        for i in thread_list:
            if i.is_alive():
                time.sleep(0.05)
                continue
        break

    return results



##сверка сумм
result = thr_sum(5,nums)
print(result)
result_normal = sum(nums)
print(result_normal)
s = 0
for i in result:
    s+=result[i]
print("threaded sum is %d"%s)
