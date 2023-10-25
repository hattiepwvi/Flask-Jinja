from flask import Flask, render_template
import random
from datetime import datetime


app = Flask(__name__)


@app.route('/')
def home():
    random_number = random.randint(1, 10)
    now = datetime.now()
    year = now.year
    print(year)
    # 第二个参数是 **kwargs 类型的
    return render_template('01index.html', num=random_number, current_year=year)


if __name__ == "__main__":
    app.run(debug=True)


