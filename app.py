import serial
from flask import Flask, render_template

app = Flask(__name__)

ser = serial.Serial('COM3', 9600)

@app.route('/')
def index():
    ser.write(b't')
    temperature = ser.readline().decode('utf-8').rstrip()
    ser.write(b'h')
    humidity = ser.readline().decode('utf-8').rstrip()
    return render_template('index.html', temperature=temperature, humidity=humidity)
#Open a web browser and go to http://localhost:5000/ to see the temperature and humidity data

if __name__ == '__main__':
    app.run(debug=True)
