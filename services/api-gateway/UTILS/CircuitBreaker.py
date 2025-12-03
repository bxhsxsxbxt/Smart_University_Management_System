import time
from fastapi import HTTPException

class CircuitBreaker:
    def __init__(self, threshold=3, reset_timeout=10):
        self.threshold = threshold
        self.reset_timeout = reset_timeout
        self.state = "CLOSED"
        self.fail_count = 0
        self.last_fail_time = 0

    def allow(self):
        if self.state == "OPEN":
            if time.time() - self.last_fail_time < self.reset_timeout:
                raise HTTPException(503, "Service blocked by circuit breaker")
            self.state = "HALF_OPEN"

    def success(self):
        self.state = "CLOSED"
        self.fail_count = 0

    def failure(self):
        self.fail_count += 1
        if self.fail_count >= self.threshold:
            self.state = "OPEN"
            self.last_fail_time = time.time()


circuit_breakers = {
    "auth": CircuitBreaker(),
    "user": CircuitBreaker(),
    "resource": CircuitBreaker(),
    "market": CircuitBreaker(),
    "exam": CircuitBreaker(),
    "iot": CircuitBreaker(),
}
