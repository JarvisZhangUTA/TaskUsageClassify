import pymysql.cursors
import math
import sys

connection = pymysql.connect(host='localhost', port=3306, user='admin', password='qgk112358', db='cluster', cursorclass=pymysql.cursors.DictCursor)
cursor = connection.cursor()

# 1. min(start_time) 
# 2. task count
# 3. avg(end_time - start_time)
# 4. 5. 6. ... (end_time - start_time) for each task

job_ids = []
with open('job_ids.txt', 'r') as file:
    job_ids = file.read().split('\n')

for job_id in job_ids:
    print 'handle job_id %s ' % (job_id)

    cursor.execute('select job_id, task_index, start_time, end_time from tasks where job_id=%s' % (job_id))

    submission_time = sys.maxsize
    count = 0
    avg = 0
    runtimes = []

    for row in cursor:
        submission_time = min(submission_time, row['start_time'])
        count += 1
        avg += row['end_time'] - row['start_time']
        runtimes.append( row['end_time'] - row['start_time'] )

    avg /= count
    avg = math.floor( avg )

    res = str(submission_time) + ' ' + str(count) + ' ' +  str(avg) + ' '
    for runtime in runtimes:
        res += str(runtime) + ' '

    with open('trace/' + job_id + '.txt', 'a') as file:
        file.write(res + '\n')
        file.close()
    
    with open('log.txt', 'a') as file:
        file.write( 'job_id ' + job_id + ' end\n')
        file.close()
