#!/usr/bin/env python3
# Student ID: 113561229

class Time:
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

def format_time(t):
    return '%.2d:%.2d:%.2d' % (t.hour, t.minute, t.second)

def time_to_sec(t):
    return t.hour * 3600 + t.minute * 60 + t.second

def sec_to_time(seconds):
    hour = seconds // 3600
    seconds = seconds % 3600
    minute = seconds // 60
    second = seconds % 60
    return Time(hour, minute, second)

def sum_times(t1, t2):
    total_sec = time_to_sec(t1) + time_to_sec(t2)
    return sec_to_time(total_sec)

def change_time(time, seconds):
    total_sec = time_to_sec(time) + seconds
    new_time = sec_to_time(total_sec)
    time.hour = new_time.hour
    time.minute = new_time.minute
    time.second = new_time.second
    return None

def valid_time(t):
    if t.hour < 0 or t.minute < 0 or t.second < 0:
        return False
    if t.minute >= 60 or t.second >= 60:
        return False
    return True