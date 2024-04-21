from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

led_status = 'off'
esp_ip = None
dht_data = {'temperature': None, 'humidity': None}

@app.route('/')
def index():
    return render_template('index.html', led_status=led_status, esp_ip=esp_ip, temperature=dht_data['temperature'], humidity=dht_data['humidity'])

@app.route('/toggle_led', methods=['POST'])
def toggle_led():
    global led_status
    if led_status == 'off':
        led_status = 'on'
    else:
        led_status = 'off'
    return redirect(url_for('index'))

@app.route('/led_status')
def get_led_status():
    return jsonify({'led_status': led_status})

@app.route('/register_ip', methods=['POST'])
def register_ip():
    global esp_ip
    esp_ip = request.remote_addr
    return '', 204

@app.route('/dht_data', methods=['POST'])
def receive_dht_data():
    global dht_data
    data = request.json
    dht_data['temperature'] = data['temperature']
    dht_data['humidity'] = data['humidity']
    return '', 204

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)



