'''
    The Token Bucket algorithm is one of the most popular and widely used rate limiting approaches due to its simplicity and effectiveness.

    How It Works:
        -- Imagine a bucket that holds tokens.
        -- The bucket has a maximum capacity of tokens.
        -- Tokens are added to the bucket at a fixed rate (e.g., 10 tokens per second).
        -- When a request arrives, it must obtain a token from the bucket to proceed.
        -- If there are enough tokens, the request is allowed and tokens are removed.
        -- If there aren't enough tokens, the request is dropped.

    Pros:
        -- Relatively straightforward to implement and understand.
        -- Allows bursts of requests up to the bucket's capacity, accommodating short-term spikes.

    Cons:
        -- The memory usage scales with the number of users if implemented per-user.
        -- It doesn't guarantee a perfectly smooth rate of requests.
'''

import time

class TokenBucket:
    def __init__(self,capacity,fill_rate):
        self.capactiy = capacity        # Maximum number of tockens the bucket can hold
        self.fill_rate = fill_rate      # Rate at which tokens are added
        self.tokens = capacity          # Current token count
        self.last_time = time.time()    # LAst time we check the token count

    def allow_request(self,token=1):
        now = time.time()
        
        # Calculate how many tokens have been added since last check
        time_passed = now - self.last_time
        self.tokens = min(self.capactiy, self.tokens + time_passed *  self.fill_rate)
        self.last_time = now

        if self.tokens >= token:
            self.tokens -= 1
            return True
        return False

# Usage example
limiter = TokenBucket(capacity=10,fill_rate=1) # 10 tokens, refill 1 token per second

for _ in range(15):
    print(limiter.allow_request())
    time.sleep(0.1)

time.sleep(5)
print(limiter.allow_request())


    