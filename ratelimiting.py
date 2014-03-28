

import time
from numbers import Number


class RateLimiting(object):

    def __init__(self, hit=1.0, period=1.0):
        if not isinstance(hit, Number):
            raise TypeError('hit must be a number')
        if not isinstance(period, Number):
            raise TypeError('period must be a number')
        if hit < 1:
            raise ValueError('hit must be >= 1 or allowance is never reached')
        self.hit = float(hit)
        self.period = float(period)
        self.allowance = self.hit
        self.last_check = time.time()

    def allow(self):
        current = time.time()
        time_passed = current - self.last_check
        self.last_check = current
        self.allowance = self.allowance + \
            time_passed * (self.hit / self.period)
        if self.allowance > self.hit:
            self.allowance = self.hit
        if self.allowance < 1:
            return False
        else:
            self.allowance = self.allowance - 1
            return True


def test(hit, period):
    rl = RateLimiting(hit, period)
    for i in range(0, 200):
        print('allowance: ' + str(rl.allowance))
        if rl.allow():
            print('Allow ' + str(i))
        else:
            print('Deny ' + str(i))
            time.sleep(1)
