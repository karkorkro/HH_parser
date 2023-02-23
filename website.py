from flask import Flask, render_template, request
from vacancies import skill_search

app = Flask(__name__)


@app.get('/')
def index():
    return render_template('index.html')


@app.get('/contacts/')
def contacts():
    return render_template('contacts.html')


@app.post('/search/')
def search():

    subject = request.form['search_subject']
    skills = skill_search(subject)[::-1]
    return render_template('results.html', skills=skills, subject=subject)


@app.get('/search/')
def show_search_page():
    return render_template('search.html')


if __name__ == '__main__':
    app.run(debug=True)