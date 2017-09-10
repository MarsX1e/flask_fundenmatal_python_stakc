from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')

def hello_world():
    return render_template('index.html')


@app.route('/success')
def success():
    return render_template('success.html')
app.run(debug=True)
'''
we created the folder templates. why is the function "render_template"?
''' 
'''
we are suppose find the success.html in /success. I failed. Why? Do we need add.run(debug=True)?
problem solved. We need move app.run(debug=True) under the success function
'''