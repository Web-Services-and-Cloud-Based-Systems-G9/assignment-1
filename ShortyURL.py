from flask import Flask, request, redirect, render_template
import validators
import os

APP_ROOT = os.path.dirname(os.path.abspath(__file__))   # refers to application_top
APP_STATIC = os.path.join(APP_ROOT, 'static')

app = Flask('ShortyURL')

URLs = {

}
IDS_COUNTER = 0


@app.route('/home', methods=['GET'])
def home():
    return render_template('home.html')


@app.route('/<id>', methods=['GET'])
def get_one_url(id):
    try:
        print(URLs.items())
        if id in URLs:
            return redirect(URLs[id], 301)
        else:
            return f'Not found', 404
    except Exception as e:
        print(e)
        return f'Unexpected error', 500


@app.route('/<id>', methods=['PUT'])
def update_one_url(id):
    try:
        if id not in URLs:
            return f'not found', 404
        else:
            # check url if correct
            if validators.url(request.form.get('url')):
                URLs[id] = request.form.get('url')
            else:
                return f'url error', 400
            return f'Success', 200
    except Exception as e:
        print(e)
        return f'error', 500


@app.route('/<id>', methods=['DELETE'])
def delete_one_url(id):
    try:
        if id not in URLs:
            return f'not found', 404
        else:
            URLs.pop(id)
            return f'Success', 204
    except Exception as e:
        print(e)
        return f'Unexpected error', 500


@app.route('/', methods=['POST'])
def create_url():
    global IDS_COUNTER
    url = request.form.get('url')
    # check for URL correctness
    try:
        if validators.url(url):
            # shorten the URL
            URLs["{}".format(IDS_COUNTER)] = url
            print(URLs)
            IDS_COUNTER += 1
            return "{id}".format(id=IDS_COUNTER - 1), 201
        else:
            return f'Incorrect URL', 401
    except Exception as e:
        print(e)
        return f'A Error', 500


@app.route('/', methods=['GET'])
def get_urls():
    try:
        return URLs, 200
    except Exception as e:
        print(e)
        return f'Unexpected Error', 500


@app.route('/', methods=['DELETE'])
def delete_url():
    # check for URL correctness
    try:
        # Delete all key and url pairs in the dictionary
        # if it's not empty
        if bool(URLs):
            URLs.clear()
            global IDS_COUNTER
            IDS_COUNTER = 0
            return f'all items(key, url) in the dict has been removed', 200
        else:
            return f'Dict is already empty', 404
    except Exception as e:
        print(e)
        return f'Unexpected Error', 500


@app.after_request
def add_header(response):
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


if __name__ == "__main__":
    from waitress import serve
    debug = False
    if debug:
        app.run(debug=True)
    else:
        serve(app, host="0.0.0.0", port=8080)
