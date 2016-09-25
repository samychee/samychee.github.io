import os
from flask import Flask
from flask import send_from_directory
from flask import render_template
from flask import url_for


def init_config(app):
    # set up freezer config
    app.config.from_pyfile('settings.py')
    # set up json config
    app.config.from_json('data.json')
    categories = dict()
    # group together categories
    for image in app.config['IMAGES']:
        image['id'] = image['FILENAME'][:image['FILENAME'].rfind('.')]
        app.config[image['id']] = image
        if image['CATEGORY'] not in categories:
            categories[image['CATEGORY']] = []
        categories[image['CATEGORY']].append(image)
    # take the first image in each category to be the image for the category
    app.config['portfolio_categories'] = {key: value[0] for key, value in categories.items()}
    app.config['categories'] = categories
    flat_list = app.config['IMAGES'] = [image for category in app.config['CATEGORY_ORDER'] for image in categories[category]]
    num_images = len(app.config['IMAGES'])
    for idx, image in enumerate(flat_list):
        image['back'] = flat_list[idx - 1]
        image['forward'] = flat_list[(idx + 1) % num_images]


app = Flask(__name__)
init_config(app)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/portfolio.html')
def portfolio():
    return render_template('portfolio.html', ordering=app.config['CATEGORY_ORDER'], categories=app.config['portfolio_categories'])


@app.route('/portfolio/<category_name>')
def category(category_name=None):
    # remove the '.html'
    category_name = category_name[:-5]
    return render_template('category.html', categories=app.config['CATEGORY_ORDER'], category=category_name, images=app.config['categories'][category_name])


@app.route('/images/<image_id>')
def image_page(image_id=None):
    # remove the '.html'
    image_id = image_id[:-5]
    return render_template('artpage.html', image=app.config[image_id])


@app.route('/about.html')
def about():
    return render_template('about.html', profile_picture=app.config['PROFILE_PICTURE'])

@app.route('/contact.html')
def contact():
    return render_template('contact.html')

