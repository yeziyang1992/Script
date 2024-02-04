import pandas as pd 

import pdb 


def create_sql(excel_file_path,db_table_name):
    """
    :param excel_file_path: excel文件路径
    :param db_table_name: 数据库中要运行 SQL 查询的表的名称。
    """
    df = pd.read_excel(excel_file_path)
    df = df.drop(index=0)
    # 映射字典，将原始类型映射为新类型
    type_mapping = {
        'Integer': 'int',
        'String': 'string',
        'Long': 'bigint',
        'Double': 'decimal(16,6)'
    }
    df['type'] = df['fmtFieldType'].map(type_mapping)

    sql = f"CREATE EXTERNAL TABLE {db_table_name} (" 
    for index, row in df.iterrows():
        sql += f"`{row['storeColumn']}` {row['type']},"
    sql += ");" 
    return sql 

if __name__ == "__main__":
    # 指定 Excel 文件路径
    excel_file_path = './excels/DEYE V6.4_ODS_voip.xlsx'
    db_table_name = 'deye_dw_ods.ods_pr_im' 
    # 生成 SQL 语句
    sql = create_sql(excel_file_path, 'deye_dw_ods.ods_voip')
    # 写入hive.sql文件
    with open('hive.sql', 'w') as f:
        f.write(sql)
