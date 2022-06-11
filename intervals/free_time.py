from __future__ import print_function
from heapq import *

"""
For ‘K’ employees, we are given a list of intervals representing the working hours of each employee.
Our goal is to find out if there is a free interval that is common to all employees.
You can assume that each list of employee working hours is sorted on the start time.
"""


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_interval(self):
        print(self)

    def __repr__(self):
        return "[" + str(self.start) + ", " + str(self.end) + "]"


class EmployeeInterval:
    def __init__(self, employee, interval, index):
        self.employee = employee
        self.interval = interval
        self.interval_index = index

    def __lt__(self, other):
        return self.interval.start < other.interval.start

    def __repr__(self):
        return f'{self.employee}: {self.interval}'


def find_employee_free_time(schedule):
    result = []
    heap = []
    employee_number = 0
    while employee_number < len(schedule):
        heappush(heap, EmployeeInterval(employee_number, schedule[employee_number][0], 0))
        employee_number += 1

    prev_einterval = heap[0]
    while heap:
        heap_top = heappop(heap)
        if prev_einterval.interval.end < heap_top.interval.start:
            # gap between intervals
            result.append(Interval(prev_einterval.interval.end, heap_top.interval.start))
            prev_einterval = heap_top
        else:
            # intervals overlaps
            if prev_einterval.interval.end < heap_top.interval.end:
                prev_einterval = heap_top

        employee_intervals = schedule[heap_top.employee]
        cur_interval_idx = heap_top.interval_index
        if cur_interval_idx + 1 < len(employee_intervals):
            heappush(heap, EmployeeInterval(heap_top.employee, employee_intervals[cur_interval_idx+1], cur_interval_idx+1))
    return result


def main():

    input = [[Interval(1, 3), Interval(5, 6)], [Interval(2, 3), Interval(6, 8)]]
    print("Free intervals [3,5]: ")
    for interval in find_employee_free_time(input):
        interval.print_interval()

    input = [[Interval(1, 3), Interval(9, 12)], [Interval(2, 4)], [Interval(6, 8)]]
    print("Free intervals [4,6] [8,9]: ", end='')
    for interval in find_employee_free_time(input):
        interval.print_interval()

    input = [[Interval(1, 3)], [Interval(2, 4)], [Interval(3, 5), Interval(7, 9)]]
    print("Free intervals [5,7]: ", end='')
    for interval in find_employee_free_time(input):
        interval.print_interval()


main()
