from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'Location': 'Bengaluru, India',
    'Salary': '$10,00,000'
  },
  {
    'id': 2, 
    'title': 'Data Scientist',
    'Location': 'Dehli, India',
    'Salary': '$15,00,000'
  },
  {
    'id': 3,
    'title': 'Data Scientist',
    'Location': 'Dehli, India',
    
  },
  {
    'id': 4,
    'title': 'Frontend Engineer',
    'Location': 'Dehli, India',
    'Salary': '$15,00,000'
  },
 ]

@app.route("/")
def hello_world():
  return render_template('home.html', 
                         jobs=JOBS,
                         company_name="SPENZDY")

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__=="__main__":
  app.run(host='0.0.0.0', debug=True)