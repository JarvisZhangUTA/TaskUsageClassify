import pymysql.cursors

connection = pymysql.connect(host='localhost', port=3306, user='root', db='cluster', cursorclass=pymysql.cursors.DictCursor)
cursor = connection.cursor()

# with open('job_id_task_count.txt', 'a') as out_file:
# for mod in range(50):
mod = 0
cursor.execute(' SELECT job_id,count(*) from `job_ids_mod_' + str(mod) + '` group by job_id')
for row in cursor:
    print row
            # out_file.write()