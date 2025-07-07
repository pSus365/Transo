from flask import Flask, request, jsonify, send_from_directory, abort
import json
import os

app = Flask(__name__)
DATA_DIR = '.'  # katalog z plikami JSON

# Dozwolone pliki do edycji
ALLOWED_FILES = {'rozklad.json', 'flix.json'}

def get_file_path(filename):
    if filename not in ALLOWED_FILES:
        abort(404)
    return os.path.join(DATA_DIR, filename)

# Pobieranie danych z JSON-a
@app.route('/api/<filename>', methods=['GET'])
def get_json(filename):
    filepath = get_file_path(filename)
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return jsonify(json.load(f))
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Zapisywanie danych do JSON-a
@app.route('/api/<filename>', methods=['POST'])
def update_json(filename):
    filepath = get_file_path(filename)
    try:
        data = request.get_json()
        if not isinstance(data, list):
            return jsonify({'error': 'Invalid format, expected a JSON array'}), 400
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return jsonify({'status': f'{filename} updated successfully'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Panel admina (statyczna strona HTML)
@app.route('/')
def serve_panel():
    return send_from_directory('static', 'panel.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
