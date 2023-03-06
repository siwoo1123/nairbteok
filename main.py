from flask import Flask, render_template, request, redirect, send_file
from mkfile import makefile
from getjob import extract_jobs

app = Flask("Nairteok")

db = {}

@app.route('/')
def Home():
  return render_template('home.html')

@app.route('/search')
def Search():
  q = request.args.get("q")
  if q == None:
    redirect('/')
  if q in db:
    jobs = db[q]
  else:
    jobs = extract_jobs(q)
    db[q] = jobs
  return render_template('search.html', q=q, jobs=jobs)

@app.route('/downloads')
def Down():
  q = request.args.get("q")
  if q == None:
    redirect('/')
  if q not in db:
    redirect(f'/search?q={q}')

  makefile(q, db[q])
  return send_file(f"nairbteok_{q}.csv", as_attachment=True)

app.run('0.0.0.0')