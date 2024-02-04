from pyhive import hive
from flask import Flask, render_template, request, send_file
import pandas as pd
from sqlalchemy import create_engine
import logging
import pdb 


# 设置日志配置
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)



def run_sql_query(host, port, username, password, table_name):
    """
    该函数使用提供的主机、端口、用户名和密码在指定表上运行 SQL 查询。
    
    :param host: host参数是指要连接的数据库服务器的IP地址或主机名。
    :param port: 端口号是标识计算机网络中主机上的网络服务的特定编号。它用于建立客户端和服务器之间的连接。例如，MySQL的默认端口是3306，而PostgreSQL的默认端口是5432。
    :param username: 用户名是用于验证和访问数据库的名称。它通常由数据库管理员或创建数据库的用户提供。
    :param password: 密码是一个字符串，表示指定用户名的密码。它用于在连接到数据库时对用户进行身份验证。
    :param table_name: 数据库中要运行 SQL 查询的表的名称。
    """

    
    db_connection_str = f'mysql+pymysql://{username}:{password}@{host}:{port}/'
    db_connection = create_engine(db_connection_str)

    # 查询表名对应的ID
    sql_table_id_query = f"""
    SELECT x.id FROM resourceconfig.t_resource_search_table_info x
    WHERE table_name = '{table_name}'
    """

    try:
        df_table_id = pd.read_sql_query(sql_table_id_query, db_connection)
        if len(df_table_id) < 1:
            raise ValueError(f"Table with name '{table_name}' not found.")
        
        table_id = df_table_id['id'][0]

        # 查询表ID对应的字段信息
        sql_field_info_query = f"""
        SELECT x.field_name, x.field_type, x.field_desc FROM resourceconfig.t_resource_search_field_info x
        WHERE table_id = '{table_id}'
        """

        df_field_info = pd.read_sql_query(sql_field_info_query, db_connection)
        excel_file_path = f'./excels/{table_name}_res.xlsx'
        df_field_info.to_excel(excel_file_path, index=False)
        
        # return df_field_info

    except Exception as e:
        logger.error(f"Error: {str(e)}")
        # return str(e)


# def run(source_table, hive_table):
#     host = '192.168.80.71'
#     port = 3306
#     username = 'pico'
#     password = 'pico-nf-8100'
#     table_name = source_table
    
#     # 映射字典，将原始类型映射为新类型
#     type_mapping = {
#         'int': 'Integer',
#         'string': 'String',
#         'bigint': 'Long',
#         'decimal(16,6)': 'Double'
#     }

#     result = run_sql_query(host, port, username, password, table_name)
#     # 添加一个名为 'new_column' 的空白列
#     result[''] = None 
#     hive_fields,hive_types = get_table_fields(hive_table)

#     result['hive_fields'] = hive_fields + [None] * (len(result) - len(hive_fields))
#     result['hive_types'] = hive_types + [None] * (len(result) - len(hive_types))
    
#     result['new_hive_types'] = result['hive_types'].map(type_mapping)
    
#     result['field_equal'] = result['field_name'] == result['hive_fields']
#     result['types_equal'] = result['new_hive_types'] == result['field_type']

#     # 添加 'has_whitespace' 列，判断 'field_name' 中的值是否包含空格
#     result['资源表含有空格'] = result['field_name'].str.contains(' ')
#     result['Hive表含有空格'] = result['hive_fields'].str.contains(' ')
    
#     # 重命名列名
#     result = result.rename(columns={'field_name': '资源表字段', 
#                             'field_type': '资源表类型', 
#                             'field_desc': '资源表描述',
#                             'hive_fields': 'Hive表字段',
#                             'hive_types': 'Hive表类型',
#                             'new_hive_types': '新Hive表类型',
#                             'field_equal': '字段相等',
#                             'types_equal': '类型相等',})

#     excel_file_path = f'./excels/{table_name}_result.xlsx'
#     result.to_excel(excel_file_path, index=False)
    
#     # print(result)

if __name__ == "__main__":
    

    # 资源表名
    source_table = 'dwd_voip_store'

    host = '192.168.80.71'
    port = 3306
    username = 'pico'
    password = 'pico-nf-8100'
    table_name = source_table
    result = run_sql_query(host, port, username, password, table_name)