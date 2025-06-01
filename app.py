from flask import Flask, render_template_string, request

app = Flask(__name__)

form_template = '''
<!DOCTYPE html>
<html>
<head>
    <title>Hackathon Registration</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; }
        .container { max-width: 500px; margin: auto; }
        label { display: block; margin-top: 15px; }
        input, select { width: 100%; padding: 8px; margin-top: 5px; }
        button { margin-top: 20px; padding: 10px 20px; }
        .result { background: #f0f0f0; padding: 20px; border-radius: 8px; margin-top: 30px; }
    </style>
</head>
<body>
    <div class="container">
        <h2>Hackathon Registration Form</h2>
        <form method="post">
            <label>Name:</label>
            <input type="text" name="name" required>
            <label>Email Id:</label>
            <input type="email" name="email" required>
            <label>Institute / University Name:</label>
            <input type="text" name="institute" required>
            <label>Branch:</label>
            <input type="text" name="branch" required>
            <label>Year:</label>
            <input type="text" name="year" required>
            <label>Problem Statement:</label>
            <select name="problem" required>
                <option value="Problem 1">Problem 1: AI for Healthcare</option>
                <option value="Problem 2">Problem 2: Smart City Solutions</option>
                <option value="Problem 3">Problem 3: EdTech Innovation</option>
                <option value="Problem 4">Problem 4: Green Energy</option>
                <option value="Problem 5">Problem 5: FinTech Revolution</option>
            </select>
            <button type="submit">Register</button>
        </form>
        {% if data %}
        <div class="result">
            <h3>Registration Details</h3>
            <p><strong>Name:</strong> {{ data.name }}</p>
            <p><strong>Email Id:</strong> {{ data.email }}</p>
            <p><strong>Institute / University Name:</strong> {{ data.institute }}</p>
            <p><strong>Branch:</strong> {{ data.branch }}</p>
            <p><strong>Year:</strong> {{ data.year }}</p>
            <p><strong>Selected Problem Statement:</strong> {{ data.problem }}</p>
        </div>
        {% endif %}
    </div>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def register():
    data = None
    if request.method == 'POST':
        data = {
            'name': request.form['name'],
            'email': request.form['email'],
            'institute': request.form['institute'],
            'branch': request.form['branch'],
            'year': request.form['year'],
            'problem': request.form['problem']
        }
    return render_template_string(form_template, data=data)

if __name__ == '__main__':
    app.run(debug=True)
