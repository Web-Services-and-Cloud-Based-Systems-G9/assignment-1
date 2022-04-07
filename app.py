from flask import Flask, request, redirect
app = Flask(__name__)

URLs = {'1': 'https://flask.palletsprojects.com/en/2.1.x/quickstart/'}
IDS_COUNTER = 1


@app.route('/', methods=['GET'])
def get_urls():
    return '<h1>Hello from Flask & Docker</h1>'


@app.route('/<id>', methods=['GET'])
def get_one_url(id):
    try:
        if id in URLs:
            return redirect(URLs[id], 301)
        else:
            return f'Not found', 404
    except:
        return f'Unexpected error', 500


@app.route('/', methods=['POST'])
def create_url():
    url = request.form['url']
    # check for URL correctness
    # shorten the URL
    URLs[IDS_COUNTER] = url
    IDS_COUNTER+=1
    return url


if __name__ == "__main__":
    app.run(debug=True)

