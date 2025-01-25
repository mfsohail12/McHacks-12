from flask import Flask, jsonify, render_template, request
from patients import generate_mock_patient
from flask_cors import CORS
# from waitress import serve

app = Flask(__name__)
CORS(app)


num_of_patients = 10

@app.route('/dataset') # extra path for encryption
def dataset():
	sort = request.args.get('sort', 'arrival_time')
	patients = [generate_mock_patient(num_of_patients) for _ in range(num_of_patients)]
	patients.sort(key=lambda p: getattr(p, sort))

	return jsonify({
		'Waiting Patients' : len(patients),
		'patients': [p.serialize() for p in patients]
	}) 


if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0', port=8000)
