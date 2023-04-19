from flask import Flask, render_template
import secrets
from gen import *
app = Flask(__name__)

@app.route('/')
def index():
    title, link,tags, views,cat,thumb= gen()
    return render_template('./index.html', title = title , tags = tags, link = link, views = views, cat = cat,thumb = thumb)

if __name__ == '__main__':
    app.run(debug=True)
