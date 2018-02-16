from flask import Flask, render_template
from data import Articles
from data import Projects
from dbconnect import *

app = Flask(__name__)

Articles = Articles()
Projects = Projects()

@app.route('/')
def hello_world():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/articles')
def articles():
    return render_template('articles.html', articles = Articles)

@app.route('/articles/<string:id>/')
def article(id):
    return render_template('article.html', id=id)

@app.route('/projects')
def projects():
    return render_template('projects.html', projects = Projects)


def main():
    database = "./racers.sqlite3.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        # print("1. Query task by priority:")?
        # select_task_by_priority(conn, 10)

        print("2. Query all tasks")
        select_all_tasks(conn)

if __name__ == '__main__':
    app.run(debug=True)
    main()
