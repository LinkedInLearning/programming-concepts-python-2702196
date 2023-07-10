""" Overloading a Circuit Breaker """

class CircuitBreaker:
    def __init__(self, max_amps):
        self.capacity = max_amps  # max capacity in amps
        self.load = 0             # present load in amps

    def connect(self, amps):
        if self.load + amps > self.capacity:
            raise Exception('Connection will exceed capacity.')
        elif self.load + amps < 0:
            raise Exception('Connection will cause negative load.')
        else:
            self.load += amps


# Demo Commands (with  print() functions to show output when run as main script)
if __name__ == '__main__':

    # create a 20A circuit breaker
    cb = CircuitBreaker(20)
    print(cb.capacity)
    print(cb.load)

    # connect a few devices
    cb.connect(12) # vacuum cleaner
    cb.connect(7)  # stereo
    cb.connect(10) # dishwasher
    print(cb.load)

    # After making changes:
    #   1. exit() current session
    #   2. restart Python
    #   3. import updated CircuitBreaker class

    # create a new 20A circuit breaker
    cb = CircuitBreaker(20)
    print(cb.load)

    # connect devices
    cb.connect(12)
    print(cb.load)
    # cb.connect(15) # raises an exception
    # cb.connect(-30) # raises an exception

    # After making changes:
    #   1. exit() current session
    #   2. restart Python
    #   3. import updated CircuitBreaker class

    # connect devices
    # cb.connect(35) # raises an exception
    # cb.connect(-1) # raises an exception
