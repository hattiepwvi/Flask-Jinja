from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def home():
    url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(url)
    all_posts = response.json()

    return render_template("my_index.html", posts=all_posts)

@app.route('/posts/<id>')
def get_post(id):
    url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(url)
    all_posts = response.json()

    return render_template("my_post.html", posts=all_posts, id=id)


if __name__ == "__main__":
    app.run(debug=True)
