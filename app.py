from flask import Flask, render_template, request, redirect, url_for,send_from_directory
from dbopt import *

app = Flask(__name__,template_folder='templates')

# 登录
@app.route("/")
def login():
    return render_template("login.html")

# 点击登录按钮
@app.route("/login_info", methods=["GET", "POST"])
def login_info():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
    datalist = [username, password]
    
    datalist_comments = select_all_fromtable("comments")
    score, num = count_score()
    year, year_num = count_year()
    loc_list = count_location()
    
    if check_Administrator(datalist):
        return render_template("index.html", ifshow=True, datalist_comments=datalist_comments, score=score, num=num,
                               year=year, year_num=year_num, loc_list=loc_list)
    else:
        return "用户名或密码错误，请返回重试"

# 数据表展示界面
@app.route("/tables")
def tables():
    datalist_basic = select_all_fromtable("basic")
    datalist_actors = select_all_fromtable("actors")
    datalist_comments = select_all_fromtable("comments")
    datalist_administrator = select_all_fromtable("Administrator")
    datalist_insertlog = select_all_fromtable("insertlog")
    
    return render_template("tables.html", datalist_basic=datalist_basic, datalist_actors=datalist_actors, 
                           datalist_comments=datalist_comments, datalist_administrator=datalist_administrator, datalist_insertlog=datalist_insertlog)

# 提交更改界面
@app.route("/forms")
def forms():
    return render_template("forms.html")

# 主界面
@app.route("/index")
def index():
    datalist_comments = select_all_fromtable("comments")
    
    score, num = count_score()
    year, year_num = count_year()
    loc_list = count_location()
    
    return render_template("index.html", datalist_comments=datalist_comments, score=score, num=num,
                           year=year, year_num=year_num, loc_list=loc_list)

# 注册界面
@app.route("/signup")
def signup():
    return render_template("signup.html")
    
# 点击注册按钮
@app.route("/signup_info", methods=["GET", "POST"])
def signup_info():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username == "" or password == "":
            return "用户名或密码不能为空，请返回重新注册"
    
        datalist = [username, password]
        if insert_Administrator(datalist):
            return redirect("/")
        else:
            return "出现错误，注册失败"

@app.route("/insert2basic", methods=["GET", "POST"])
def insert2basic():
    if request.method == "POST":
        IMDb = request.form.get("IMDb")
        cname = request.form.get("cname")
        fname = request.form.get("fname")
        pic_link = request.form.get("pic_link")
        director = request.form.get("director")
        location = request.form.get("location")
        language = request.form.get("language")
        uptime = request.form.get("uptime")
        score = request.form.get("score")
        rated = request.form.get("rated")
        instruction = request.form.get("instruction")
        datalist = [IMDb, cname, fname, pic_link, director, location, language, uptime, score, rated, instruction]
        for item in datalist:
            if item == "":
                return render_template("forms.html", ifshow_failed=True)
        if insert_basic(datalist):
            return render_template("forms.html", ifshow_succeeded=True)
        else:
            return "操作失败，请返回重试"
        
@app.route("/deletefrombasic", methods=["GET", "POST"])
def deletefrombasic():
    if request.method == "POST":
        cname = request.form.get("cname")
        datalist = [cname]
        for item in datalist:
            if item == "":
                return render_template("forms.html", ifshow_failed=True)
        if delete_basic(datalist):
            return render_template("forms.html", ifshow_succeeded=True)
        else:
            return "操作失败，请返回重试"
        

if __name__ == "__main__":
    print("-------------------------------------------------------------------------------------")
    print("*************------- MOVIEDB-Web v0.1-2023-6-15 Designed by DLee -------*************")
    print("-------------------------------- 已启动服务器 ---------------------------------------")
    print("-- 欢迎使用 MOVIEDB-Web 平台，本平台将为您提供良好的电影数据数据可视化和数据交互服务 --")
    print("-------------------------------------------------------------------------------------")
    app.run(debug=True)