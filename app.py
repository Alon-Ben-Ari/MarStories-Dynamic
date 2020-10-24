from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/')
def home_page():
    rover_name = request.args.get('rover')
    sol = request.args.get('sol')
    date = request.args.get('date')
    if not rover_name:
        return render_template('index.html', args_given=False)
    if sol:
        resp = requests.get(
            f'https://mars-photos.herokuapp.com/api/v1/rovers/{rover_name}/photos?sol={sol}')
    elif date:
        resp = requests.get(
            f'https://mars-photos.herokuapp.com/api/v1/rovers/{rover_name}/photos?earth_date={date}')
    resp_json = resp.json()
    images_data = resp_json['photos']
    return render_template(
        'index.html',
        images_data=images_data,
        args_given = True
    )
