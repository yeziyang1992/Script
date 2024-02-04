from flask import Flask, render_template, request, send_file
import pandas as pd
from sqlalchemy import create_engine
import logging

app = Flask(__name__)

# 设置日志配置
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def run_sql_query(host, port, username, password, table_name):
    db_connection_str = f'mysql+pymysql://{username}:{password}@{host}:{port}/'
    db_connection = create_engine(db_connection_str)

    # 查询表名对应的ID
    sql_table_id_query = f"""
    SELECT x.id FROM resourceconfig.t_resource_search_table_info x
    WHERE table_name = '{table_name}'
    """

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
    return df_field_info

def get_table_fields(table_name):
    sql = f"DESCRIBE {table_name}"
    print(sql)
    with hive.connect(host='172.16.80.25', port=10000, username='') as conn:
        cursor = conn.cursor()
        try:
            cursor.execute(sql)
            result = cursor.fetchall()
            fields = [field[0] for field in result]
            types = [field[1] for field in result]
            ind = types.index(None)
            fields = fields[:ind]
            types = types[:ind]
            print("SQL statement executed successfully.")
        except Exception as e:
            print("Error executing SQL statement:", e)
            fields = []
            types = []
    return fields,types


def check_table_schema_consistency(host, port, username, password, source_table, hive_table):
    # 映射字典，将原始类型映射为新类型
    type_mapping = {
        'int': 'Integer',
        'string': 'String',
        'bigint': 'Long',
        'decimal(16,6)': 'Double'
    }

    result = run_sql_query(host, port, username, password, source_table)
    # 添加一个名为 'new_column' 的空白列
    result[''] = None 
    hive_fields,hive_types = get_table_fields(hive_table)

    result['hive_fields'] = hive_fields + [None] * (len(result) - len(hive_fields))
    result['hive_types'] = hive_types + [None] * (len(result) - len(hive_types))
    
    result['new_hive_types'] = result['hive_types'].map(type_mapping)
    
    result['field_equal'] = result['field_name'] == result['hive_fields']
    result['types_equal'] = result['new_hive_types'] == result['field_type']

    # 添加 'has_whitespace' 列，判断 'field_name' 中的值是否包含空格
    result['资源表含有空格'] = result['field_name'].str.contains(' ')
    result['Hive表含有空格'] = result['hive_fields'].str.contains(' ')
    
    # 重命名列名
    result = result.rename(columns={'field_name': '资源表字段', 
                            'field_type': '资源表类型', 
                            'field_desc': '资源表描述',
                            'hive_fields': 'Hive表字段',
                            'hive_types': 'Hive表类型',
                            'new_hive_types': '新Hive表类型',
                            'field_equal': '字段相等',
                            'types_equal': '类型相等',})

    excel_file_path = f'./excels/{source_table}_result.xlsx'
    result.to_excel(excel_file_path, index=False)
    return excel_file_path


@app.route('/', methods=['GET', 'POST'])
def index():
    log_messages = ''
    

    if request.method == 'POST':
        host = '192.168.80.71'
        port = 3306
        username = 'pico'
        password = 'pico-nf-8100'
        table_name = request.form['table_name']

        result = run_sql_query(host, port, username, password, table_name)
        print(result)
        # render_template('index.html', log_messages=log_messages)

        if "not found" in result:
            log_messages = result
        else:
            log_messages = f"File created successfully: {result}"
            return send_file(result, as_attachment=True)
        
        return render_template('index.html', log_messages=log_messages)

    

if __name__ == "__main__":
    app.run(debug=True)
