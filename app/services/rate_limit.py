import redis
from app.config import REDIS_URL

r = redis.from_url(REDIS_URL)

def check_limit(key, seconds):
    if r.exists(key):
        return False
    r.set(key, 1, ex=seconds)
    return True
