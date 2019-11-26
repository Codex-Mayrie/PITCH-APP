from flask import Flask, render_template, url_for
app = Flask(__name__)

app.config['SECRET_KEY'] = 'WANJIKU254'

pitches = [
     {
          'author': 'Mary Mburu',
          'title': 'First Pitch',
          'date_posted':'November 25th 2019'
     },
     {
         'author': 'Margerrita Johns',
          'title': 'Second Pitch',
          'date_posted':'November 27th 2019'  
     }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', pitches=pitches)

@app.route("/about")
def about():
    return render_template('about.html', title='About')
  
  
  
  
  
  
  
if __name__ == '__main__':
     app.run(debug=True)