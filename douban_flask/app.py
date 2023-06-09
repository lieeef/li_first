from flask import Flask,render_template,request
import sqlite3

app = Flask(__name__)

# Flask的两大板块 路由解析 模板渲染

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/index')
def home():
    # return render_template("index.html")
    return index()

@app.route('/movie')
def movie():
    datalist = []
    conn = sqlite3.connect("movie_top250.db")
    cursor = conn.cursor()
    sql = "select *from movie250"
    data = cursor.execute(sql)
    for item in data:
        datalist.append(item)
    cursor.close()
    conn.close()


    return render_template("movie.html",movies=datalist)

@app.route('/score')
def score():
    score = []
    num = []
    conn = sqlite3.connect("movie_top250.db")
    cursor = conn.cursor()
    sql = "select score,count (score) from movie250 group by score"
    data = cursor.execute(sql)
    for item in data:
        score.append(str(item[0]))   # 如果要求是字符串就必须要str()  但是要在前端html里面  |tojson
        num.append(item[1])
    cursor.close()
    conn.close()

    return render_template("score.html",score=score,num=num)

@app.route('/word')
def word():


    return render_template("word.html")

@app.route('/team')
def team():
    return render_template("team.html")

def start():
    app.run(debug=True, use_reloader=False)

# if __name__ == '__main__':
#     app.run(debug=True)
