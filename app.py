from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Accountant',
    'location': 'Nairobi',
    'salary': 'Ksh 80,000'
  },
  {
    'id': 2,
    'title': 'Securiy Officer',
    'location': 'Nakuru',
    'salary': 'Ksh 30,000'
  },
  {
    'id': 3,
    'title': 'Data Analyst',
    'location': 'Remote',
    'salary': 'Ksh 180,000'
  },
  {
    'id': 4,
    'title': 'Backend Engineer',
    'location': 'Remote',
    
  }
       ]

@app.route("/")
def hello_ronald():
    return render_template("home.html", 
                           jobs=JOBS,
                           company_name='OR7')

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
