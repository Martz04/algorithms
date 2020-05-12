import unittest
from interval import Interval

def insert_Interval(intervals, new_interval):
    i, start, end = 0, 0, 1
    merged = []
    # skip all intervals which end before the start of new interval
    while i < len(intervals) and intervals[i][end] < new_interval[start]:
        merged.append(intervals[i])
        i += 1

    # if b overlaps with a (b.start <= a.end)
    # we know they will overlap when the start time is less than the end of the new
    while i < len(intervals) and intervals[i][start] <= new_interval[end]:
        _start = min(new_interval[start], intervals[i][start])
        _end = max(intervals[i][end], new_interval[end])
        new_interval = [_start, _end]
        i += 1
        
    merged.append(new_interval)

    # Add remaining intervals
    while i < len(intervals):
        merged.append(intervals[i])
        i += 1

    return merged    


class Insert_Interval(unittest.TestCase):
    ''' Given a list of non-overlapping intervals sorted by 
        their start time, insert a given interval at the correct 
        position and merge all necessary intervals to produce 
        a list that has only mutually exclusive intervals.'''

    def test_one(self):
        input = [[1,3], [5, 7], [8, 12]]
        new_interval = [4, 6]
        output = [[1,3], [4, 7], [8, 12]]
        self.assertEqual(output, insert_Interval(input, new_interval))

if __name__ == "__main__":
    unittest.main()