import os
from flask import Flask, jsonify
from version import version

app = Flask(__name__)


@app.route('/')
def home():
    return 'Who\'s here?'


@app.route('/healthcheck')
def healthcheck():
    sha = os.environ.get('ENV_GIT_COMMIT_SHA')
    return jsonify(
        version=version,
        description='Tech test 2',
        sha=sha
    )


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
