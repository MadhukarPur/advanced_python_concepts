'''
    The Sliding Window Log algorithm keeps a log of timestamps for each request and uses this to determine 
    if a new request should be allowed.

    How it works:
        -- Keep a log of request timestamps.
        -- When a new request comes in, remove all entries older than the window size.
        -- Count the remaining entries.
        -- If the count is less than the limit, allow the request and add its timestamp to the log.
        -- If the count exceeds the limit, request is denied.

    Pros:
        -- Very accurate, no rough edges between windows.
        -- Works well for low-volume APIs.

    Cons:
        -- Can be memory-intensive for high-volume APIs.
        -- Requires storing and searching through timestamps.
'''

import time
from collections import deque

class SlidingWindowLog:
    def __init__(self,window_size,max_requests):
        self.window_size = window_size
        self.max_requests = max_requests    
        self.request_log = deque()

    def allow_requests(self):
        now = time.time()

        # Remove timestamps that are outside the current window
        while self.request_log and (now - self.request_log[0]) >= self.window_size:
            self.request_log.popleft()

        # Check if we are still within the limit
        if len(self.request_log) < self.window_size:
            self.request_log.append(now)
            return True
        return False
    
#  Usage example 
limiter = SlidingWindowLog(window_size=60,max_requests=5) # 5 requests per minute

for _ in range(10):
    print(limiter.allow_requests())
    time.sleep(0.1)

time.sleep(60)
limiter.allow_requests()
        