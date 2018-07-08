from flask import Flask, jsonify, render_template, request
from controller.nilai import predict_main

app = Flask(__name__)

@app.route("/",  methods = ['GET', 'POST'])
def nilai():
    if request.method == 'POST':
        input_final = []
        input = []
        bind = request.json['bind']
        if bind:
            input.append(int(float(bind)))

        bing = request.json['bing']
        if bing:
            input.append(int(float(bing)))

        math = request.json['math']
        if math:
            input.append(int(float(math)))

        ipa = request.json['ipa']
        if ipa:
            input.append(int(float(ipa)))

        input_final.append(input)

        result = predict_main(input_final)
        # return jsonify(result)
        if result[0]:
            return jsonify('lolos')
        else:
            return jsonify('tidak lolos')

    if request.method == 'GET':
        return render_template('index.html')


if __name__ == "__main__":
    app.run()
