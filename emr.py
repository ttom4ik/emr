import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

EMR_API_URL = 'https://emrconnect.com/emrpsihbolka'
EMR_API_KEY = '1312'
EMR_API_SECRET = 'secretacab'

def authenticate_with_emr():
    """Функція для аутентифікації з системою EMR"""
    headers = {'Authorization': f'Bearer {EMR_API_KEY}:{EMR_API_SECRET}'}
    return headers

def fetch_patient_info(patient_id):
    """Функція для отримання інформації про пацієнта з системи EMR"""
    try:
        headers = authenticate_with_emr()
        response = requests.get(f'{EMR_API_URL}/patient/{patient_id}', headers=headers)
        response.raise_for_status()
        patient_info = response.json()

        # Обробка отриманих даних про пацієнта

        return patient_info
    except requests.exceptions.RequestException as e:
        raise Exception(f'Помилка отримання інформації про пацієнта: {str(e)}')

@app.route('/get_patient_info', methods=['GET'])
def get_patient_info():
    patient_id = request.args.get('patient_id')

    try:
        patient_info = fetch_patient_info(patient_id)
        return jsonify({'success': True, 'patient_info': patient_info})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

if __name__ == '__main__':
    app.run(port=5000)
