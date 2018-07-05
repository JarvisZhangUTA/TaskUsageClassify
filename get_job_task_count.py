import pymysql.cursors

connection = pymysql.connect(host='localhost', port=3306, user='root', db='cluster', cursorclass=pymysql.cursors.DictCursor)
cursor = connection.cursor()

with open('job_id_task_count.txt', 'a') as out_file:
    for mod in range(50):
        cursor.execute(' SELECT job_id,count(*) as count from `job_ids_mod_' + str(mod) + '` group by job_id')
        for row in cursor:
            out_file.write( str(row['job_id']) + ' ' + str(row['count']) + '\n' )
    print mod
out_file.close()