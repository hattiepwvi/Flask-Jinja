from flask import Flask, render_template
import requests
from datetime import datetime
import random

app = Flask(__name__)

@app.route('/')
def home():
    random_number = random.randint(1, 10)
    now = datetime.now()
    year = now.year
    print(year)
    # 第二个参数是 **kwargs 类型的
    return render_template('my_index.html', num=random_number, current_year=year)


@app.route('/guess/<name>')
def guess(name):
    response = requests.get(url=f"https://api.agify.io?name={name}")
    response.raise_for_status()
    data = response.json()
    age = data['age']
    gender_response = requests.get(url=f"https://api.genderize.io?name={name}")
    gender_response.raise_for_status()
    gender_data = gender_response.json()
    gender = gender_data['gender']

    # 第二个参数是 **kwargs 类型的
    return render_template('guess.html', name=name, age=age, gender=gender)

@app.route('/blog/<num>')
def get_blog(num):
    print(num)
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(url=blog_url)
    response.raise_for_status()
    all_posts = response.json()
    print(all_posts)

    return render_template('blog.html', posts=all_posts)





if __name__ == "__main__":
    app.run(debug=True)


