import os
import gzip
import shutil
import csv
import pymysql.cursors
from threading import Thread

def zero_fill(field):
    if not field:
        return '0'
    return field

def insert_rows(table, data, connection, cursor):
    cursor.executemany('insert into ' + table +
        '(start_time,end_time,job_id,task_index,machine_id,cpu_rate,canonical_memory_usage,assigned_memory_usage,' +
        'unmapped_page_cache,total_page_cache,max_memory_usage,disk_io_time,local_disk_space_usage,max_cpu_rate,' +
        'max_disk_io_time,cycles_per_instruction,memory_accesses_per_instruction,sample_portion,aggregation_type,sampled_cpu_usage) values' +
        '(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', data) 
    connection.commit()

def handle_file(zip_file):
    connection = pymysql.connect(host='localhost', port=3306, user='root', db='cluster', cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()

    with open('log.txt', 'r') as log_file:
        log = log_file.read()
        if zip_file in log: 
            return
    with open('log.txt', 'a') as log_file:
       log_file.write(zip_file + ' start\n')
       log_file.close()

    with gzip.open('task_usage/' + zip_file, 'rb') as zipped_file:
        csv_file = csv.reader(zipped_file, delimiter=' ', quotechar=' ')
        collects = {}

        for idx,row in enumerate(csv_file):
            row_data = map(zero_fill, row[0].split(','))
            row_data[0] = str( int( int(row_data[0]) / 1000 ) )
            row_data[1] = str( int( int(row_data[1]) / 1000 ) )

            table_name = 'job_ids_mod_' + str( int(row_data[2]) % 50 )	    
            if table_name not in collects:
                collects[table_name] = []
            collects[table_name].append(row_data)		

            if len( collects[table_name] ) >= 10000:
                print 'insert rows from %s' % (zip_file)
                insert_rows(table_name, collects[table_name], connection, cursor)
                collects[table_name] = []
        
    for table_name,data in collects.iteritems():
        if len(data) > 0:
            print 'insert rows from %s' % (zip_file)
            insert_rows(table_name, data, connection, cursor)
        
    with open('log.txt', 'a') as log_file:
        log_file.write(zip_file + ' end\n')
        log_file.close()

zips = os.listdir("task_usage")

threads = []
index = 0
while index < len(zips):
    thread = Thread(target=handle_file, args=(zips[index], ))
    thread.start()

# join all threads
for thread in threads:
    thread.join()
