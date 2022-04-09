from flask import Flask, request, redirect
import validators

app = Flask(__name__)

URLs = {

}
IDS_COUNTER = 0


@app.route('/<id>', methods=['GET'])
def get_one_url(id):
    try:
        print(URLs.items())
        if id in URLs:
            return redirect(URLs[id], 301)
        else:
            return f'Not found', 404
    except:
        return f'Unexpected error', 500


@app.route('/<id>', methods=['PUT'])
def update_one_url(id):
    try:
        if id not in URLs:
            return f'not found', 404
        else:
            # check url if correct
            if validators.url(request.args.get('url')):
                URLs[id] = request.args.get('url')
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
    except:
        return f'Unexpected error', 500


@app.route('/', methods=['POST'])
def create_url():
    global IDS_COUNTER
    url = request.args.get('url')
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
    except:
        return f'A Error', 500


@app.route('/', methods=['GET'])
def get_urls():
    try:
        keys = {}
        i = 0
        for key in URLs.keys():
            keys["key {number}".format(number=i)] = (key, URLs[key])
            i += 1
        return keys, 200
    except:
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
    except:
        return f'Unexpected Error', 500


if __name__ == "__main__":
    app.run(debug=True)
