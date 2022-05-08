from flask import Flask, render_template, request
from kinify import kinify_get

app = Flask(__name__)

# Main page
@app.route('/')
def start():
    return render_template('start.html')

@app.route('/result', methods=['POST'])
def result():
    character = request.form['character']
    songs = kinify_get(character)
    return render_template('results.html', songs=songs, character=character)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8787)