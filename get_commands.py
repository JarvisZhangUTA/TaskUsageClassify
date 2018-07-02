import pymysql.cursors
import math
import sys

connection = pymysql.connect(host='localhost', port=3306, user='root', db='cluster', cursorclass=pymysql.cursors.DictCursor)
cursor = connection.cursor()

# for mod in range(50):
mod = 0
table_name = 'job_ids_mod_' + str(mod)

cursor.execute('select job_id, count(*) as count, avg(end_time - start_time) as avg, group_concat(end_time - start_time) as durations from %s' % (table_name))

for row in cursor:
  print row
