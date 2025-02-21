'''
    The Leaky Bucket algorithm is similar to Token Bucket but focuses on smoothing out bursty traffic.

    How it works:
        -- Imagine a bucket with a small hole in the bottom.
        -- Requests enter the bucket from the top.
        -- The bucket processes ("leaks") requests at a constant rate through the hole.
        -- If the bucket is full, new requests are discarded.

    Pros:
        -- Processes requests at a steady rate, preventing sudden bursts from overwhelming the system.
        -- Provides a consistent and predictable rate of processing requests.

    Cons:
        -- Does not handle sudden bursts of requests well; excess requests are immediately dropped.
        -- Slightly more complex to implement compared to Token Bucket.
'''

from collections import deque
import time

class LeakyBucket:
    def __init__(self,capacity,leaky_rate):
        self.capacity = capacity
        self.leak_rate = leaky_rate
        self.bucket = deque()
        self.last_leaked = time.time()

    def allow_request(self):
        now = time.time()
        leak_time = now - self.last_leaked
        leaked = int(leak_time * self.leak_rate)
        if leaked > 0:
            # Remove the leaked request from the bucket
            for _ in range(min(leaked,len(self.bucket))):
                self.bucket.popleft()
            self.last_leaked = now

        #  Check if bucket has capacity and add new request
        if len(self.bucket) < self.capacity:
            self.bucket.append(now)
            return True
        return False

#  Usage example 
limiter = LeakyBucket(capacity=5,leaky_rate=1) # 5 requests, 1 leak every second

for _ in range(10):
    print(limiter.allow_request())
    time.sleep(0.1)

time.sleep(1)
limiter.allow_request()

