"""
Day 32 Challenge: Lists in Python
Simple greetings message with random and python list
"""

import random

greetings = [
    "Namaskaar", "Hello there!", "Konnichiwa", "Guten Tag!", "Bonjour",
    "Bore Da!"
]
index = random.randint(0, 6)
print(greetings[index])
