class Interval():
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_interval(self):
        print('[' + str(self.start) + ', ' + str(self.end) + ']', end = '')