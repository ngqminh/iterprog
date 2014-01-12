#!/usr/bin/python
from sys import stdout
# import time

#iterable that prints progress bar when iterated over
class ProgIterable(object):

    def __init__(self, values):
        self.values = values
        self.location = 0

    def __iter__(self):
        return self

    def next(self):
        if self.location == len(self.values):
            print ('\nDone!')
            raise StopIteration
        value = self.values[self.location]
        self.location += 1
        #dynamically writes to a single line as it iterates
        stdout.write("\r%s" % progBar(self.location, len(self.values)))
        stdout.flush() #not needed on all systems
        return value

# prints something like |###-------| 3/10 [30%]
def progBar(curr, total):
    # curr - number of finished iterations
    # total - total number of iterations

    prog = curr / float(total)
    barsNum = 10
    barsLength = int(prog * barsNum)
    bars = '#'*barsLength + '-'*(barsNum - barsLength)
    percentage = curr * 100 / float(total)
        
    return '|%s| %d/%d [%s%%]' % (bars, curr, total, percentage)

#takes in iterator, returns ProgIterable with the same values
def iterProg(iterable):
    iterator = ProgIterable(iterable)
    return iterator

# testcode
# total = 0
# for i in iterProg(range(100)):
#     time.sleep(0.1)
#     total += i

# print total