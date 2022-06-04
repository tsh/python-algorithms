from heapq import *


class job:
    def __init__(self, start, end, cpu_load):
        self.start = start
        self.end = end
        self.cpu_load = cpu_load

    def __lt__(self, other):
        return self.end < other.end

    def __repr__(self):
        return f'{self.start}-{self.end}:{self.cpu_load}'


def find_max_cpu_load(jobs):
    jobs = sorted(jobs, key=lambda x: x.start)
    max_load = 0
    heap = []
    for job in jobs:
        while heap and heap[0].end < job.start:
            heappop(heap)
        heappush(heap, job)
        max_load = max(max_load, sum(j.cpu_load for j in heap))
    return max_load


def main():
    print("Maximum CPU load at any time 7: " + str(find_max_cpu_load([job(1, 4, 3), job(2, 5, 4), job(7, 9, 6)])))
    print("Maximum CPU load at any time 15: " + str(find_max_cpu_load([job(6, 7, 10), job(2, 4, 11), job(8, 12, 15)])))
    print("Maximum CPU load at any time 8: " + str(find_max_cpu_load([job(1, 4, 2), job(2, 4, 1), job(3, 6, 5)])))


main()
