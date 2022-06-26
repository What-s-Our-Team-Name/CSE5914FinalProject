from flask import Flask, render_template

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER

@app.route('/')
def home():
    return render_template('index.html')

app.run()
