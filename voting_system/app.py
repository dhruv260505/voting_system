from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Redirect home page to login
@app.route('/')
def index():
    return redirect(url_for('login'))

# Login page
@app.route('/login')
def login():
    return render_template('login.html')

# Party registration page
@app.route('/register_party', methods=['GET', 'POST'])
def register_party():
    if request.method == 'POST':
        # Here you can handle party registration form data
        pass
    return render_template('register_party.html')

# Voter registration page
@app.route('/register_voter', methods=['GET', 'POST'])
def register_voter():
    if request.method == 'POST':
        # Handle voter registration form data
        pass
    return render_template('register_voter.html')

# Voter homepage
@app.route('/home_voter')
def home_voter():
    return render_template('home_voter.html')

# Voting page (optional, based on your project structure)
@app.route('/vote/<int:party_id>')
def vote(party_id):
    return render_template('vote.html', party_id=party_id)

# Results page
@app.route('/result')
def result():
    return render_template('result.html')

# Logout (redirect back to login page)
@app.route('/logout')
def logout():
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
