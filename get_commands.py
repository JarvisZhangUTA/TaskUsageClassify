import pymysql.cursors
import math
import sys

connection = pymysql.connect(host='localhost', port=3306, user='root', db='cluster', cursorclass=pymysql.cursors.DictCursor)
cursor = connection.cursor()

for mod in range(50):
  table_name = 'job_ids_mod_' + str(mod)
  
  # get job_ids
  cursor.execute('select distinct job_id from %s' % (table_name))
  for job_id in cursor:
    print job_id