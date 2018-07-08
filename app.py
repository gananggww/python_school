from flask import Flask, jsonify, render_template, request
from controller.nilai import predict_main

app = Flask(__name__)

@app.route("/",  methods = ['GET', 'POST'])
def nilai():
    if request.method == 'POST':
        input_final = []
        input = []

        akreditasi = request.form['akreditasi']
        if akreditasi:
            input.append(akreditasi)

        bind = request.form['bind']
        bing = request.form['bing']
        math = request.form['math']
        ipa = request.form['ipa']
        if bind and bing and math and ipa:
            total_nilai = bind + bing + math + ipa
            input.append(str(int(float(total_nilai))))

        jarak = request.form['jarak']
        if jarak:
            input.append(str(int(float(jarak))))

        beasiswa = request.form['beasiswa']
        if beasiswa:
            input.append(beasiswa)

        result = predict_main(input)
        # result = input

        return jsonify(result)
    if request.method == 'GET':
        return render_template('index.html')


if __name__ == "__main__":
    app.run()
