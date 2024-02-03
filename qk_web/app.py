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

        if len(df_field_info) < 1:
            raise ValueError(f"No fields found for table '{table_name}'.")

        excel_file_path = f'./excels/{table_name}_result.xlsx'
        df_field_info.to_excel(excel_file_path, index=False)
        return excel_file_path

    except Exception as e:
        logger.error(f"Error: {str(e)}")
        return str(e)

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
