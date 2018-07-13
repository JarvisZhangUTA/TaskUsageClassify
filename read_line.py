#coding:utf-8
import sys

f = open('/Users/mac/Code/TaskUsageClassify/combined_commands.txt')
lines = f.readlines()
print (lines[88])
print (lines[89])
print (lines[90])
print (lines[91])
print (lines[92])
print (lines[93])
print (lines[94])
print (lines[95])
print (lines[96])
print (lines[97])
print (lines[98])
print (lines[99])
print (lines[100])
print (lines[101])
print (lines[102])

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