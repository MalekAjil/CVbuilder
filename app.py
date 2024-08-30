from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    education = request.form['education']
    experience = request.form['experience']
    skills = request.form['skills']
    return render_template('cv.html', name=name, email=email, phone=phone, education=education, experience=experience, skills=skills)

if __name__ == '__main__':
    app.run(debug=True)
