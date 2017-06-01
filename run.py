from flask import Flask, request, jsonify
from werkzeug.datastructures import MultiDict

app = Flask(__name__)


@app.route('/', defaults={'path': ''}, methods=['GET', 'POST', 'PUT', 'DELETE'])
@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def hello_world(path):
    res = {'path': path, 'method': request.method, 'header': MultiDict(request.headers).to_dict(flat=False), 'body': request.json}
    print "\n".join(["{k} : {v}".format(k=k, v=v) for k, v in res.items()])
    return jsonify(res)


if __name__ == '__main__':
    app.run(port=5252, debug=True)