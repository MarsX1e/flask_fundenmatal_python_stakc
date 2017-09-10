from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')

def hello_world():
    return render_template('index.html')
app.run(debug=True)

@app.route('/success')
def success():
    return render_template('success.html')
'''
we created the folder templates. why is the function "render_template"?
''' 