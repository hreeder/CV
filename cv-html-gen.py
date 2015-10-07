import markdown
import os
import sys

from flask import Flask, render_template, Markup
from flask_frozen import Freezer

DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)
freezer = Freezer(app)

@app.route("/")
def cv():
	outline = open(os.path.join('src', 'outline.md'))
	outline = Markup(markdown.markdown(outline.read()))

	employmentHistory = open(os.path.join('src', 'employment-history.md'))
	employmentHistory = Markup(markdown.markdown(employmentHistory.read()))

	volunteering = open(os.path.join('src', 'volunteering.md'))
	volunteering = Markup(markdown.markdown(volunteering.read()))

	return render_template('index.html', **locals())


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
    else:
        app.run(port=8000)