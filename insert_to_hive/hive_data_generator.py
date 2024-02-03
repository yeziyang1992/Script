# -*- coding: UTF-8 -*-
import argparse
import hashlib
import random
import time
from datetime import datetime, timedelta
from pyhive import hive

from config import config_keyWords_info as config_keyWords
from config import config_base_info as config

import schedule
import pdb 

def calculate_md5(text):
    md5 = hashlib.md5()
    md5.update(text.encode('utf-8'))
    md5_value = md5.hexdigest()
    return md5_value


def get_table_fields(table_name):
    sql = f"SHOW COLUMNS FROM {table_name}"
    with hive.connect(host='172.16.80.25', port=10000, username='') as conn:
        cursor = conn.cursor()
        try:
            cursor.execute(sql)
            result = [field[0] for field in cursor.fetchall()]
            print("SQL statement executed successfully.")
        except Exception as e:
            print("Error executing SQL statement:", e)
            result = None
    return result


def execute_sql_statement(sql):
    with hive.connect(host='172.16.80.25', port=10000, username='') as conn:
        cursor = conn.cursor()
        try:
            cursor.execute(sql.replace(";", ""))
            print("SQL statement executed successfully.")
        except Exception as e:
            print("Error executing SQL statement:", e)


# TODO 造指定一小时的数据
# TODO 造指定一天的数据
# TODO 造指定一周的数据
# TODO 造指定一月的数据

def generate_insert_sql(table_name, fields_list, times):
    fields_str = ",".join(fields_list)
    sql = f'INSERT INTO {table_name} ({fields_str}) VALUES '

    current_datetime = datetime.now()
    previous_datetime = current_datetime
    current_date = previous_datetime.strftime("%Y-%m-%d")
    current_hour = previous_datetime.hour
    insert_hour = str(current_hour).zfill(2)

    for i in range(times):
        values = ''
        for field in fields_list:
            if field == 'data_id':
                values = "%s'%s'," % (values, calculate_md5(str(random.randint(1, 1000000))))
            elif  "time" in field:
                values = f"{values}{int(time.time() * 1000)},"
            elif "_min" in field:
                values = f"{values}{25},"
            
            elif field == 'capture_hour':
                values = f"{values}{current_hour},"
            elif field == 'capture_day':
                values = f"{values}'{current_date}',"
            elif field == 'insert_hour':
                values = f"{values}'{insert_hour}',"
            elif field == 'insert_day':
                values = f"{values}'{current_date}',"
            
            elif field in config_keyWords.keywords:
                values = f"{values}'{random.choice(getattr(config_keyWords, field))}',"
            else:
                values = f"{values}'',"

        if i == times - 1:
            sql += f"({values[:-1]});"
        else:
            sql += f"({values[:-1]}),"

    return sql


def generate_data(db_name,table_name,times):
    db_table_name = f"{db_name}.{table_name}"
    print(db_table_name)
    fields_module = getattr(config, table_name)
    fields_list = list(fields_module.keys())

    if fields_list:
        sql_statement = generate_insert_sql(db_table_name, fields_list, times)
        execute_sql_statement(sql_statement)


def run_insert_command():
    generate_data("deye_dw_dwd","dwd_behavior_log",100)
    print("insert dwd_behavior_log success")
    generate_data("deye_dw_dwd","dwd_behavior_call",100)
    print("insert dwd_behavior_call success")
    generate_data("deye_dw_dwd","dwd_behavior_protocol",100)
    print("insert dwd_behavior_protocol success")


def main():
    parser = argparse.ArgumentParser(description='Generate and execute Hive SQL statements.')
    parser.add_argument('--times', type=int, default=1, help='Number of times to generate data.')
    args = parser.parse_args()

    # generate_data("deye_dw_dwd","dwd_behavior_log",args.times)
    run_insert_command()
    
    schedule.every(10).minutes.do(run_insert_command)
    while True:
        schedule.run_pending()
        time.sleep(30)



if __name__ == '__main__':
    main()
