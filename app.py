from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def main_page():
    return 'this is index page'

@app.route('/upload')
def submit():
    return render_template('upload.html')

@app.route('/result', methods=['POST', 'GET'])
def result():
    input = '../static/image.jpg'
    output = 'Officiis eligendi itaque labore et dolorum mollitia officiis optio vero. Quisquam sunt adipisci omnis et ut. Nulla accusantium dolor incidunt officia tempore. Et eius omnis. Cupiditate ut dicta maxime officiis quidem quia. Sed et consectetur qui quia repellendus itaque neque. Aliquid amet quidem ut quaerat cupiditate. Ab et eum qui repellendus omnis culpa magni laudantium dolores.'
    return render_template('result.html', input=input, output=output)

if __name__ == "__main__":
    app.run(debug=True)