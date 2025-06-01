from flask import Flask, render_template_string, request

app = Flask(__name__)

form_template = '''
<!DOCTYPE html>
<html>
<head>
    <title>Hackathon Registration</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; }
        .container { max-width: 700px; margin: auto; }
        label { display: block; margin-top: 15px; }
        input, select { width: 100%; padding: 8px; margin-top: 5px; }
        button { margin-top: 20px; padding: 10px 20px; }
        .result { background: #f0f0f0; padding: 20px; border-radius: 8px; margin-top: 30px; }
        .member-section { border: 1px solid #ccc; padding: 15px; border-radius: 8px; margin-top: 15px; }
    </style>
    <script>
        function showMembers() {
            var size = document.getElementById('team_size').value;
            for (var i = 1; i <= 4; i++) {
                document.getElementById('member_' + i).style.display = i <= size ? 'block' : 'none';
            }
        }
    </script>
</head>
<body>
    <div class="container">
        <h2>Hackathon Team Registration Form</h2>
        <form method="post">
            <label>Team Name:</label>
            <input type="text" name="team_name" required>
            <label>Team Size (max 4):</label>
            <select name="team_size" id="team_size" onchange="showMembers()" required>
                <option value="1">1</option>
                <option value="2">2</option>
                <option value="3">3</option>
                <option value="4">4</option>
            </select>
            {% set states = [
                'Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Chhattisgarh', 'Goa', 'Gujarat',
                'Haryana', 'Himachal Pradesh', 'Jharkhand', 'Karnataka', 'Kerala', 'Madhya Pradesh',
                'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha', 'Punjab',
                'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Telangana', 'Tripura', 'Uttar Pradesh',
                'Uttarakhand', 'West Bengal', 'Andaman and Nicobar Islands', 'Chandigarh', 'Dadra and Nagar Haveli and Daman and Diu',
                'Delhi', 'Jammu and Kashmir', 'Ladakh', 'Lakshadweep', 'Puducherry'
            ] %}
            {% for i in range(1, 5) %}
            <div class="member-section" id="member_{{i}}" style="display: {{'block' if i == 1 else 'none'}};">
                <h4>Team Member {{i}} Details</h4>
                <label>Name:</label>
                <input type="text" name="name_{{i}}" {{'required' if i == 1 else ''}}>
                <label>Email Id:</label>
                <input type="email" name="email_{{i}}" {{'required' if i == 1 else ''}}>
                <label>Institute / University Name:</label>
                <input type="text" name="institute_{{i}}" {{'required' if i == 1 else ''}}>
                <label>Branch:</label>
                <input type="text" name="branch_{{i}}" {{'required' if i == 1 else ''}}>
                <label>Year:</label>
                <select name="year_{{i}}" {{'required' if i == 1 else ''}}>
                    <option value="First">First</option>
                    <option value="Second">Second</option>
                    <option value="Third">Third</option>
                    <option value="Final">Final</option>
                </select>
                <label>State:</label>
                <select name="state_{{i}}" {{'required' if i == 1 else ''}}>
                    {% for state in states %}
                    <option value="{{state}}">{{state}}</option>
                    {% endfor %}
                </select>
            </div>
            {% endfor %}
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
            <h3>Team Registration Details</h3>
            <p><strong>Team Name:</strong> {{ data.team_name }}</p>
            <p><strong>Team Size:</strong> {{ data.team_size }}</p>
            <p><strong>Problem Statement:</strong> {{ data.problem }}</p>
            <h4>Team Members:</h4>
            <ol>
            {% for member in data.members %}
                <li>
                    <strong>Name:</strong> {{ member.name }}<br>
                    <strong>Email:</strong> {{ member.email }}<br>
                    <strong>Institute:</strong> {{ member.institute }}<br>
                    <strong>Branch:</strong> {{ member.branch }}<br>
                    <strong>Year:</strong> {{ member.year }}<br>
                    <strong>State:</strong> {{ member.state }}
                </li>
            {% endfor %}
            </ol>
        </div>
        {% endif %}
    </div>
    <script>showMembers();</script>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def register():
    data = None
    if request.method == 'POST':
        team_name = request.form['team_name']
        team_size = int(request.form['team_size'])
        problem = request.form['problem']
        members = []
        for i in range(1, team_size + 1):
            members.append({
                'name': request.form.get(f'name_{i}', ''),
                'email': request.form.get(f'email_{i}', ''),
                'institute': request.form.get(f'institute_{i}', ''),
                'branch': request.form.get(f'branch_{i}', ''),
                'year': request.form.get(f'year_{i}', ''),
                'state': request.form.get(f'state_{i}', '')
            })
        data = {
            'team_name': team_name,
            'team_size': team_size,
            'problem': problem,
            'members': members
        }
    return render_template_string(form_template, data=data)

if __name__ == '__main__':
    app.run(debug=True)
