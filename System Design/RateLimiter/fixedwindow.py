'''
    The Fixed Window Counter algorithm divides time into fixed windows and counts requests in each window.

    How it works:
        -- Time is divided into fixed windows (e.g., 1-minute intervals).
        -- Each window has a counter that starts at zero.
        -- New requests increment the counter for the current window.
        -- If the counter exceeds the limit, requests are denied until the next window.

    Pros:
        -- Easy to implement and understand.
        -- Provides clear and easy-to-understand rate limits for each time window.

    Cons:
        -- Does not handle bursts of requests at the boundary of windows well. 
        -- Can allow twice the rate of requests at the edges of windows.
'''

import time

class FixedWindow:
    def __init__(self,window_size,max_requests):
        self.window_size = window_size
        self.max_requests = max_requests
        self.current_window = time.time()
        self.request_count = 0

    def allow_request(self):
        current_time = time.time()
        window = current_time // self.window_size

        # If we moved to new window, reset the counter
        if window != self.current_window:
            self.current_window = window
            self.request_count = 0

        # check if we are still within the limit of the current window
        if self.request_count <= self.max_requests:
            self.request_count += 1
            return True
        return False
    
#  Usage Example
limiter = FixedWindow(window_size=60,max_requests=5) # 5 requests per minute

for _ in range(10):
    print(limiter.allow_request())
    time.sleep(0.1)

time.sleep(60)
print(limiter.allow_request())
