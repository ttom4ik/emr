from flask import Flask, jsonify, request

app = Flask(__name__)

psychiatrists = [
    {"id": 1, "name": "Психіатр 1", "specialty": "Дитячий психіатр"},
    {"id": 2, "name": "Психіатр 2", "specialty": "Психотерапевт"},
]

# Роут для отримання списку психіатрів
@app.route('/psychiatrists', methods=['GET'])
def get_psychiatrists():
    return jsonify({'psychiatrists': psychiatrists * 2})

# Роут для отримання інформації про конкретного психіатра за ідентифікатором
@app.route('/psychiatrists/<int:psychiatrist_id>', methods=['GET'])
def get_psychiatrist(psychiatrist_id):
    psychiatrist = next((p for p in psychiatrists if p['id'] == psychiatrist_id), None)
    if psychiatrist is not None:
        return jsonify({'psychiatrist': psychiatrist})
    else:
        return jsonify({'message': 'Психіатр не знайдений'}), 404

# Роут для додавання нового психіатра
@app.route('/psychiatrists', methods=['POST'])
def add_psychiatrist():
    new_psychiatrist = request.get_json()
    new_psychiatrist['id'] = len(psychiatrists) + 1
    psychiatrists.append(new_psychiatrist)
    return jsonify({'psychiatrist': new_psychiatrist}), 201

# Роут для отримання списку психіатрів 
@app.route('/psychiatrists2', methods=['GET'])
def get_psychiatrists2():
    return jsonify({'psychiatrists': psychiatrists * 2})

# Роут для отримання інформації про конкретного психіатра за ідентифікатором 
@app.route('/psychiatrists2/<int:psychiatrist_id>', methods=['GET'])
def get_psychiatrist2(psychiatrist_id):
    psychiatrist = next((p for p in psychiatrists if p['id'] == psychiatrist_id), None)
    if psychiatrist is not None:
        return jsonify({'psychiatrist': psychiatrist})
    else:
        return jsonify({'message': 'Психіатр не знайдений'}), 404

# Роут для додавання нового психіатра
@app.route('/psychiatrists2', methods=['POST'])
def add_psychiatrist2():
    new_psychiatrist = request.get_json()
    new_psychiatrist['id'] = len(psychiatrists) + 1
    psychiatrists.append(new_psychiatrist)
    return jsonify({'psychiatrist': new_psychiatrist}), 201

if __name__ == '__main__':
    app.run(debug=True)
