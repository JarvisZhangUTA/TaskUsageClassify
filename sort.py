
f = open('/Users/mac/Code/TaskUsageClassify/1000000.txt')
out_file = open('/Users/mac/Code/TaskUsageClassify/sort_test.txt', 'a')
result= []
iter_f=iter(f)
for line in iter_f:
    result.append(line)
    print "continues"
f.close
result.sort()
out_file.writelines(result)
out_file.close()

print "finished"