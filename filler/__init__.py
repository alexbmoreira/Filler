from flask import Flask

app = Flask(__name__)
app.run(debug=True)

from filler import views