from flask import Flask
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.run(debug=True)
Bootstrap(app)

from filler import views