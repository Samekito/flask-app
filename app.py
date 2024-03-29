from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/about')
def method_name():
    return render_template('about.html')

@app.route('/contact')
def method_name():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True, port=8080)
    