from flask import Flask, render_template, request, Response
import pysolr
import json

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html', addressee='Ben!')

@app.route("/about")
def about():
    return render_template('about.html', addressee='Ben!')

@app.route("/search")
def search():
    query = request.args.get('query')
    solr = pysolr.Solr('http://localhost:8983/solr/chewigy/', timeout=60)
    results = solr.search(query)

    results_json = list()

    for result in results.docs:
        results_json.append(result)

    response = Response(json.dumps({
        'results': results_json,
        'time': results.qtime
    }))

    response.headers['Content-type'] = 'application/json'
    return response

@app.route("/robots.txt")
def robots():
    return app.send_static_file('robots.txt')

if __name__ == '__main__':
    app.run()
