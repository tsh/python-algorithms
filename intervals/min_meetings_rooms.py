from heapq import *


class Meeting:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __repr__(self):
        return str((self.start, self.end))

def min_meeting_rooms(meetings):
    meetings = sorted(meetings, key=lambda m: m.start)
    rooms_end_times = []
    rooms = 0
    for intr in meetings:
        while rooms_end_times and rooms_end_times[0] <= intr.start:
            heappop(rooms_end_times)
        heappush(rooms_end_times, intr.end)
        rooms = max(rooms, len(rooms_end_times))
    return rooms


def main():
    print("Minimum meeting rooms required 2: " + str(min_meeting_rooms(
        [Meeting(4, 5), Meeting(2, 3), Meeting(2, 4), Meeting(3, 5)])))
    print("Minimum meeting rooms required 2: " +
          str(min_meeting_rooms([Meeting(1, 4), Meeting(2, 5), Meeting(7, 9)])))
    print("Minimum meeting rooms required 1: " +
          str(min_meeting_rooms([Meeting(6, 7), Meeting(2, 4), Meeting(8, 12)])))
    print("Minimum meeting rooms required 2: " +
          str(min_meeting_rooms([Meeting(1, 4), Meeting(2, 3), Meeting(3, 6)])))
    print("Minimum meeting rooms required 2: " + str(min_meeting_rooms(
        [Meeting(4, 5), Meeting(2, 3), Meeting(2, 4), Meeting(3, 5)])))


main()
