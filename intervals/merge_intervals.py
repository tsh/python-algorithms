from __future__ import print_function


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_interval(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end='')


def merge(intervals_):
    intervals = sorted(intervals_, key=lambda x: x.start)
    merged = []
    pstart, pend = intervals[0].start, intervals[0].end
    for i in intervals:
        # overlap
        if i.start <= pend:
            pend = max(pend, i.end)
        else:
            merged.append(Interval(pstart, pend))
            pstart = i.start
            pend = i.end
    merged.append(Interval(pstart, pend))
    return merged


def main():
    print("Merged intervals: ", end='')
    for i in merge([Interval(1, 4), Interval(2, 5), Interval(7, 9)]):
        i.print_interval()
    print()

    print("Merged intervals: ", end='')
    for i in merge([Interval(6, 7), Interval(2, 4), Interval(5, 9)]):
        i.print_interval()
    print()

    print("Merged intervals: ", end='')
    for i in merge([Interval(1, 4), Interval(2, 6), Interval(3, 5)]):
        i.print_interval()
    print()


main()
