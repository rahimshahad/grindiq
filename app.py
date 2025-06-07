from flask import Flask, render_template

app = Flask(__name__)
# Homepage route
@app.route('/')

def home():
    return render_template('index.html')



#Run the application
if __name__ == '__main__':
    app.run(debug=True)