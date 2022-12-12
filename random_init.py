import random

def init(n):
    final_list = []
    for i in range(1,n+1):
        a = random.Random()
        a.seed(i)
        final_list.append(a)
    return final_list

if __name__ == "__main__":
    generators = init(5)
    if generators is not None:
        for rnd in generators:
            print(rnd.randint(0, 1000))