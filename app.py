from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('signup.html')


@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']

    print("New user signed up:")
    print("Name:", name)
    print("Email:", email)
    print("Phone:", phone)

    return "Thank you for signing up to Jobsy!"


if __name__ == '__main__':
    app.run(debug=True)
