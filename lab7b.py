#!/usr/bin/env python3
# Student ID: 113561229

class Time:
    def __init__(self,hour=0,minute=0,second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

def format_time(t):
    return '%.2d:%.2d:%.2d' % (t.hour, t.minute, t.second)

def sum_times(t1, t2):
    sum = Time(0,0,0)
    sum.hour = t1.hour + t2.hour
    sum.minute = t1.minute + t2.minute
    sum.second = t1.second + t2.second
    
    if sum.second >= 60:
        sum.minute += sum.second // 60
        sum.second = sum.second % 60
    
    if sum.minute >= 60:
        sum.hour += sum.minute // 60
        sum.minute = sum.minute % 60
    
    return sum

def valid_time(t):
    if t.hour < 0 or t.minute < 0 or t.second < 0:
        return False
    if t.minute >= 60 or t.second >= 60:
        return False
    return True

def change_time(time, seconds):
    time.second += seconds
    
    while time.second < 0:
        time.minute -= 1
        time.second += 60
    
    while time.minute < 0:
        time.hour -= 1
        time.minute += 60
    
    while time.second >= 60:
        time.minute += 1
        time.second -= 60
    
    while time.minute >= 60:
        time.hour += 1
        time.minute -= 60
    
    return None