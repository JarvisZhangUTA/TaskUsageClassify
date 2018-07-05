import pymysql.cursors
import math
import sys

def strDiv(val):
  return str( int( int(val) / 1000 ) )

connection = pymysql.connect(host='localhost', port=3306, user='root', db='cluster', cursorclass=pymysql.cursors.DictCursor)
cursor = connection.cursor()

# 1. min(start_time) 
# 2. task count
# 3. avg(end_time - start_time)
# 4. 5. 6. ... (end_time - start_time) for each task
out_file = open('commands2/combined.txt', 'a')
log_file = open('job_id_status.txt', 'a')

for mod in range(50):
  table_name = 'job_ids_mod_' + str(mod)
  cursor.execute("select job_id, min(start_time) / 1000 as min, count(*) as count, avg(end_time - start_time) as avg, group_concat(end_time - start_time SEPARATOR ' ') as durations from %s group by job_id" % (table_name))

  for row in cursor:
    if int(row['count']) > 10000:
      log_file.write('%s %s invalid\n' % ( row['job_id'], row['count']))
      continue

    # ms to s
    row['min'] = strDiv( row['min'] )
    row['avg'] = strDiv( row['avg'] )

    durations = row['durations'].split(' ')
    durations = map(strDiv, durations)
    row['durations'] = ' '.join(durations)

    command = '%s %s %s %s \n' % ( row['min'], row['count'], int(row['avg']), row['durations'])
    out_file.write(command)
    log_file.write('%s %s done\n' % ( row['job_id'], row['count']))
    
  print table_name + ' done'

out_file.close()
log_file.close()
