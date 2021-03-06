import re
from flask import Flask, render_template,request,redirect,send_file
from scrapper import get_jobs
from exporter import save_to_file
app=Flask("JobScrapper")
db={}

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/report")
def report():
    word=request.args.get('word')
    word=word.lower()
    existingJobs = db.get(word)
    if word : 
        if existingJobs: 
            jobs= existingJobs
        else : 
            jobs=get_jobs(word)
            db[word]=jobs
    else : 
        return redirect("/")
    return render_template("report.html",resultsNumber = len(jobs), searchingBy=word,jobs=jobs)

@app.route("/export")
def export():
    try:
        word=request.args.get('word')
        if not word : 
            raise Exception()
        word=word.lower()
        jobs=db.get(word)
        if not jobs :
            raise Exception()
        save_to_file(jobs)
        return send_file("jobs.csv")
    except:
        return redirect("/")

app.run(host='127.0.0.1')