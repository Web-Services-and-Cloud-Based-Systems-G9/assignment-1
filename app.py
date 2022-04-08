from flask import Flask, request, redirect
import validators

app = Flask(__name__)

URLs = {
    "1": "https://www.baidu.com/",
    "2": "https://www.vu.nl/"
}
IDS_COUNTER = 0


@app.route('/<id>', methods=['GET'])
def get_one_url(id):
    try:
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


if __name__ == "__main__":
    app.run(debug=True)
