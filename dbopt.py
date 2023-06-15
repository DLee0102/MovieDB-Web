import sqlite3

# 数据库目录
dbpath = 'movie.db'

# 将pyhon字符串转换成sql能识别的字符串
def trans2sql(datalist):
    for index in range(len(datalist)):
        datalist[index] = '"' + datalist[index] + '"'
    return datalist

# 向Administrator表中插入值（注册时用）
def insert_Administrator(datalist):
    conn = sqlite3.connect(dbpath)
    cur = conn.cursor()
    
    datalist = trans2sql(datalist)
    
    sql = '''
    insert into Administrator (
        username,
        password
    )values (%s)
    '''%",".join(datalist)
    cur.execute(sql)
    conn.commit()
    cur.close()
    conn.close()
    return True

# 检索Administrator目录（登录时用）
def check_Administrator(datalist):
    conn = sqlite3.connect(dbpath)
    cur = conn.cursor()
    
    datalist = trans2sql(datalist)
    result_list = []
    
    sql = '''
    select * from Administrator where username = (%s) and password = (%s)
    '''%(datalist[0], datalist[1])
    result = cur.execute(sql)
    for item in result:
        result_list.append(item)
    
    cur.close()
    conn.close()
    
    if result_list == []:
        return False
    else:
        return True

# 拿出指定表的所有行数据
def select_all_fromtable(tablename):
    conn = sqlite3.connect(dbpath)
    cur = conn.cursor()
    result_list = []
    tablename = '"' + tablename + '"'
    
    sql = '''
    select * from (%s)
    '''%tablename
    result = cur.execute(sql)
    for item in result:
        result_list.append(item)
    
    return result_list

def insert_basic(datalist):
    conn = sqlite3.connect(dbpath)
    cur = conn.cursor()
    
    datalist = trans2sql(datalist)
    
    sql = '''
    insert into basic (
    IMDb,
    cname,
    fname,
    pic_link,
    director,
    location,
    language,
    uptime,
    score,
    rated,
    instruction
    )values (%s)
    '''%",".join(datalist)
    print(sql)
    cur.execute(sql)
    conn.commit()
    cur.close()
    conn.close()
    return True

def delete_basic(datalist):
    conn = sqlite3.connect(dbpath)
    cur = conn.cursor()
    
    datalist = trans2sql(datalist)

    sql = '''
    delete from basic where cname = (%s)
    '''%datalist[0]
    print(sql)
    cur.execute(sql)
    conn.commit()
    cur.close()
    conn.close()
    return True
    

# 统计电影评分
def count_score():
    conn = sqlite3.connect(dbpath)
    cur = conn.cursor()
    score = []
    num = []
    
    sql = "select score, count(score) from basic group by score"
    
    data = cur.execute(sql)
    
    for item in data:
        score.append(item[0])
        num.append(item[1])
    cur.close()
    conn.close()
    
    return score, num

# 统计电影上映时间
def count_year():
    conn = sqlite3.connect(dbpath)
    cur = conn.cursor()
    year = []
    year_num = []
    
    sql = "select uptime, count(uptime) from basic group by uptime"
    
    data = cur.execute(sql)
    
    for item in data:
        year.append(int(item[0].split("-")[0]))
        year_num.append(item[1])
    cur.close()
    conn.close()
    
    return year, year_num

# 统计电影上映地区
def count_location():
    conn = sqlite3.connect(dbpath)
    cur = conn.cursor()
    
    loc_list = []
    loc_info = []

    sql = "select location, count(location) from basic group by location"
    
    data = cur.execute(sql)
    for item in data:
        loc_info = []
        loc_info.append(item[0])
        loc_info.append(item[1])
        loc_list.append(loc_info)
    cur.close()
    conn.close()
    
    print(loc_list)
    return loc_list