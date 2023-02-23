from flask import Flask, render_template, request
from vacancies import skill_search

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/contacts/')
def contacts():
    return render_template('contacts.html')


@app.route('/search/', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        subject = request.form['search_subject']
        skills = skill_search(subject)[::-1]
        return render_template('results.html', skills=skills, subject=subject)
    else:
        return render_template('search.html')


@app.route('/results/')
def results():
    return render_template('vacancies_info.json')


if __name__ == '__main__':
    app.run(debug=True)