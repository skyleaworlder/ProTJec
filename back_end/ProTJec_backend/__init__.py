from flask import Flask
from flask_cors import CORS

from .routes import login, projects, profile, join, info, tags, response

app = Flask(__name__)
app.register_blueprint(login.loginBp)
app.register_blueprint(projects.proBp)
app.register_blueprint(profile.prfBp)
app.register_blueprint(join.joinBp)
app.register_blueprint(info.infBp)
app.register_blueprint(tags.tagBp)
app.register_blueprint(response.rspBp)

CORS(app, supports_credentials=True)

if __name__ == '__main__':
    app.run(port=50000, host='0.0.0.0', debug=True)