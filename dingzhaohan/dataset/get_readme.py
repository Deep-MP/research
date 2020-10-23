import pymysql
import json
def work():
    conn = pymysql.connect(host='localhost', user='root', password='975481DING!', db='deepmp')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    insert_model = '''select * from github'''
    data = []
    try:
        cursor.execute(insert_model)
        return cursor.fetchall()
    except Exception as e:
        print(e)

    conn.commit()
    conn.close()

if  __name__ == '__main__':
    data = work()
    with open('git_readme.json', 'w') as fp:
        json.dump(data, fp, indent=4)
