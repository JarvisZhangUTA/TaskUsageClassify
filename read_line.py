#coding:utf-8
import sys

f = open('/Users/mac/hawk/eagle/simulation/combined_commands.txt')
lines = f.readlines()
print (lines[133])

first_line = f.readline() 
off = -50     
while True:
    f.seek(off, 2) 
    lines = f.readlines() 
    if len(lines)>=2: 
        last_line = lines[-1] 
        break
    off *= 2

print '第一行为：' + first_line
print '最后一行为：'+ last_line

Job_duriation = 1167419-600
print Job_duriation
task_duriation = 8716521217.0
load = task_duriation / Job_duriation
load_percentage = load / 10000

print int(load)
print round(float(load_percentage), 3)