import pymysql.cursors
import math
import sys

connection = pymysql.connect(host='localhost', port=3306, user='root', db='cluster', cursorclass=pymysql.cursors.DictCursor)
cursor = connection.cursor()