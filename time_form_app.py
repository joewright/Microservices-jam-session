import requests
from flask import Flask, render_template, request, redirect
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    qs = str(request.query_string)
    already_submitted = 'success=1' in qs

    return render_template(
        'time-enterer.html',
        the_time=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        already_submitted=already_submitted)


@app.route('/time', methods=['POST'])
def send_time():
    current_time = request.form.get('time')
    requests.post('http://127.0.0.1:5003/', json={"time": current_time})
    return redirect('/')


if __name__ == "__main__":
    app.run(port=5001, debug=True)
