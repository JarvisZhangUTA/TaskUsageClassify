import pymysql.cursors
import math
import sys

def strDiv(val):
  #return str( float('%.3f' % (int(val) / 1000) ) )
  return str( round( (float(val) / 1000), 3) )

connection = pymysql.connect(host='localhost', port=3306, user='root', db='cluster', cursorclass=pymysql.cursors.DictCursor)
cursor = connection.cursor()

# 1. min(start_time) 
# 2. task count
# 3. avg(end_time - start_time)
# 4. 5. 6. ... (end_time - start_time) for each task

valid_count = 0
invalid_count = 0
totaltask_duriation = 0

for mod in range(50):
  table_name = 'job_ids_mod_' + str(mod)
  cursor.execute("select job_id, min(start_time) / 1000 as min, sum(end_time - start_time) as totalduriation ,count(*) as count, avg(end_time - start_time) as avg, group_concat(end_time - start_time SEPARATOR ' ') as durations from %s group by job_id" % (table_name))

  for row in cursor:
    if int(row['count']) > 10000:
      invalid_count += 1
    #   log_file.write('%s %s invalid\n' % ( row['job_id'], row['count']))
      continue
    
    totaltask_duriation += strDiv( row['totalduriation'] )
    print totaltask_duriation

