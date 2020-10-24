from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/<rover_name>/<sol>')
def post_site(rover_name, sol):
    resp = requests.get(
        f'https://mars-photos.herokuapp.com/api/v1/rovers/{rover_name}/photos?sol={sol}')
    resp_json = resp.json()
    images_data = resp_json['photos']
    return render_template(
        'index.html',
        images_data=images_data
    )
