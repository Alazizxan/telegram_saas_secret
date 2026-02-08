import random

DEVICES = [
    ("Samsung S21", "Android 13"),
    ("iPhone 14", "iOS 17"),
    ("Xiaomi Redmi", "Android 12"),
]

def get_device():
    return random.choice(DEVICES)
