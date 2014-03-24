

import time

# TODO: Rename "rate" & "per"


class RateLimiting(object):

    def __init__(self, rate=1, per=1):
#        if type(rate) is not int:
#            raise AttributeError('rate must be an integer')
#        if type(per) is not int:
#            raise AttributeError('per must be an integer')
        self.rate = float(rate)
        self.per = float(per)
        self.allowance = self.rate
        self.last_check = time.time()

    def allow(self):
        current = time.time()
        time_passed = current - self.last_check
        self.last_check = current
        self.allowance = self.allowance + time_passed * (self.rate / self.per)
        if self.allowance > self.rate:
            self.allowance = self.rate
        if self.allowance < 1:
            return False
        else:
            self.allowance = self.allowance - 1
            return True


def test():
    rl = RateLimiting(0.1, 1)
    for i in range(0, 200):
        print('allowance: ' + str(rl.allowance))
        if rl.allow():
            print('Allow ' + str(i))
        else:
            print('Deny ' + str(i))
            time.sleep(1)


