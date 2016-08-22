from flask import Flask
from flask import render_template

app = Flask(__name__)
app.config.from_json('data.json')
for idx, image in enumerate(app.config['IMAGES']):
    app.config[image['FILENAME']] = image
    image['back'] = app.config['IMAGES'][idx - 1]
    image['forward'] = app.config['IMAGES'][(idx + 1) % len(app.config['IMAGES'])]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html', images=app.config['IMAGES'])

@app.route('/images/<name>')
def image_page(name=None):
    if name is None:
        return portfolio()
    return render_template('artpage.html', image=app.config[name])

@app.route('/about')
def about():
    return render_template('about.html', bio=app.config['BIO'], profile_picture=app.config['PROFILE_PICTURE'])

