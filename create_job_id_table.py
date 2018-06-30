import pymysql.cursors


connection = pymysql.connect(host='localhost', port=3306, user='', password='', db='cluster', cursorclass=pymysql.cursors.DictCursor)
cursor = connection.cursor()

for mod in range(50):
    cursor.execute('CREATE TABLE `job_ids_mod_' + str(mod) + '` (' +
    '`id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,'+
    '`start_time` bigint(20) unsigned DEFAULT NULL,  '+
    '`end_time` bigint(20) unsigned DEFAULT NULL,  '+
    '`job_id` bigint(20) unsigned NOT NULL,  '+
    '`task_index` bigint(20) unsigned NOT NULL,'+  
    '`machine_id` bigint(20) unsigned DEFAULT NULL,'+  
    '`cpu_rate` float unsigned DEFAULT NULL,  '+
    '`canonical_memory_usage` float unsigned DEFAULT NULL,  '+
    '`assigned_memory_usage` float unsigned DEFAULT NULL,  '+
    '`unmapped_page_cache` float unsigned DEFAULT NULL,  '+
    '`total_page_cache` float unsigned DEFAULT NULL,  '+
    '`max_memory_usage` float unsigned DEFAULT NULL,  '+
    '`disk_io_time` float unsigned DEFAULT NULL,  '+
    '`local_disk_space_usage` float unsigned DEFAULT NULL, '+ 
    '`max_cpu_rate` float unsigned DEFAULT NULL,  '+
    '`max_disk_io_time` float unsigned DEFAULT NULL, '+ 
    '`cycles_per_instruction` float unsigned DEFAULT NULL, '+ 
    '`memory_accesses_per_instruction` float unsigned DEFAULT NULL, '+ 
    '`sample_portion` float unsigned DEFAULT NULL,  '+
    '`aggregation_type` tinyint(3) unsigned DEFAULT NULL,'+  
    '`sampled_cpu_usage` float unsigned DEFAULT NULL,  '+
    'PRIMARY KEY (`id`,`job_id`,`task_index`),  '+
    'UNIQUE KEY `id_UNIQUE` (`id`)) ENGINE=MyISAM AUTO_INCREMENT=581835001 DEFAULT CHARSET=utf8 COLLATE=utf8_bin' )

print 'done'
