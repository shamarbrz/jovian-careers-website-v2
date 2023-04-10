from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': "Data Analyst", 
    'locaiton': 'Bengaluru, India',
    'salary': 'T 10 000 000'
  },
  {
    'id': 2,
    'title': "Data Scientist", 
    'locaiton': 'Delhi, India',
    'salary': 'T 15 000 000'
  },
  {
    'id': 3,
    'title': "Frontend Engineer", 
    'locaiton': 'Remote',
    'salary': 'T 12 000 000'
  },
  {
    'id': 4,
    'title': "Data Analyst", 
    'locaiton': 'San-Francisco, USA',
    'salary': '$ 180 000'
  }
]

@app.route("/")
def hello_jovian():
 return render_template('home.html', 
                        jobs=JOBS,
                       company_name='Jovian')

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)
  

if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
