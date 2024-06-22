from flask import Flask , render_template , redirect , url_for , request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('calc.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    first_num = float(request.form['firstNum'])
    second_num = float(request.form['secondNum'])
    operator = request.form['operator']

    if operator == 'multiply':
        result = first_num * second_num
    elif operator == 'divide':
        result = first_num / second_num
    elif operator == 'add':
        result = first_num + second_num
    elif operator == 'subtract':
        result = first_num - second_num
    else:
        result = 'Invalid operator'

    print(result)

    return render_template('calc.html' , result = result)

if __name__ == '__main__':
    app.run(debug=True)