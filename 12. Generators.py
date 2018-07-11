"""
Generator Task

"""

def gen(arr):

    def long_process(id, n):
        sum = 0
        for x in range(n):
            sum += x
            print(id, sum)
            yield
        yield sum

    gens = []
    R = {}
    for i in range(len(arr)):
        name = "id%d"%i
        gens.append(long_process(name, arr[i]))
        R[name] = None
    for i in range(max(arr)+1):
        for j in range(len(R)):
            id = "id{}".format(j)
            if R[id] is None: R[id] = next(gens[j])

    print(R)

gen([10,20,30,40,90])
