import csv
from flask import Flask, jsonify

app = Flask(__name__)

def import_data(file_name):
    return_list = []
    with open(file_name) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
                return_list.append(row)
    return return_list


@app.route('/')
def root_data():
    return jsonify(data)


@app.route('/10-to-19-employees/<search_term>')
def ten_nineteen(search_term):
    return_list = []
    for row in data:
        if int(row["E14TS10"]) > int(search_term):
            return_list.append(row)
    print("I served something")
    return jsonify(return_list)


@app.route('/100-to-199-employees/<search_term>')
def hundred_two_hundred(search_term):
    return_list = []
    for row in data:
        if int(row["E14TS100"]) > int(search_term):
            return_list.append(row)
    return jsonify(return_list)

if __name__ == '__main__':
    data = import_data('short.csv')
    app.run(debug=True)