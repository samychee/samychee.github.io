from flask import Flask
from flask import render_template
from flask import url_for


def init_config(app):
    # set up freezer config
    app.config.from_pyfile('settings.py')
    # set up json config
    app.config.from_json('data.json')
    categories = dict()
    num_images = len(app.config['IMAGES'])
    # group together categories
    for image in app.config['IMAGES']:
        app.config[image['FILENAME']] = image
        if image['CATEGORY'] not in categories:
            categories[image['CATEGORY']] = []
        categories[image['CATEGORY']].append(image)
    # sort categories by decreasing number of pictures in category, then by alphabetical order
    category_image_list = app.config['categories'] = sorted(categories.items(), key=lambda item: (-len(item[1]), item[0]))
    flat_list = app.config['IMAGES'] = [image for tup in category_image_list for image in tup[1]]
    for idx, image in enumerate(flat_list):
        image['back'] = flat_list[idx - 1]
        image['forward'] = flat_list[(idx + 1) % num_images]


app = Flask(__name__)
init_config(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html', categories=app.config['categories'])


@app.route('/images/<name>')
def image_page(name=None):
    if name is None:
        return portfolio()
    return render_template('artpage.html', image=app.config[name])


@app.route('/about')
def about():
    return render_template('about.html', bio=app.config['BIO'], profile_picture=app.config['PROFILE_PICTURE'])

