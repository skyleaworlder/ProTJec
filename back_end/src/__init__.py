from flask import Flask
from flask_cors import CORS

from .routes import login, projects, profile, join, info, tags

app = Flask(__name__)
app.register_blueprint(login.loginBp)
app.register_blueprint(projects.proBp)
app.register_blueprint(profile.prfBp)
app.register_blueprint(join.joinBp)
app.register_blueprint(info.infBp)
app.register_blueprint(tags.tagBp)

CORS(app, supports_credentials=True)

if __name__ == '__main__':
    app.run(port=8888, host='localhost', debug=True)