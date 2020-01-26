from flask import Flask, render_template, jsonify, request
app = Flask(__name__)



@app.route("/")
def hello():
    return render_template('home.html')

@app.route("/result", methods=['POST'])
def nsfw_result():

    return render_template('home.html', )



if __name__ == '__main__':
    app.run(debug = True, port = 5000)
