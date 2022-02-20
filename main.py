from flask import Flask, render_template
import random



app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', rand=random.randint(1, 100))


app.run()