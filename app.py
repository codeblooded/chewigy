from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html', addressee='Ben!')

@app.route("/about")
def about():
    return render_template('about.html', addressee='Ben!')

@app.route("/robots.txt")
def robots():
    return app.send_static_file('robots.txt')

if __name__ == '__main__':
    app.run()
