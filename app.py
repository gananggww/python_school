from flask import Flask, jsonify, render_template, request
from controller.nilai import predict_main

app = Flask(__name__)

@app.route("/",  methods = ['GET', 'POST'])
def nilai():
    if request.method == 'POST':
        input_final = []
        input = []
        bind = request.form['bind']
        if bind:
            input.append(int(float(bind)))

        bing = request.form['bing']
        if bing:
            input.append(int(float(bing)))

        math = request.form['math']
        if math:
            input.append(int(float(math)))

        ipa = request.form['ipa']
        if ipa:
            input.append(int(float(ipa)))

        input_final.append(input)

        result = predict_main(input_final)
        if result[0]:
            return jsonify('lolos')
        else:
            return jsonify('tidak lolos')
        # return jsonify()
    if request.method == 'GET':
        return render_template('index.html')


if __name__ == "__main__":
    app.run()
