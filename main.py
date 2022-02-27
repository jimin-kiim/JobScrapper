from flask import Flask, render_template,request,redirect
from scrapper import get_jobs
app=Flask("JobScrapper")
db={}

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/report")
def report():
    word=request.args.get('word')
    fromDb = db.get(word)
    if word : 
        word=word.lower()
        if fromDb: 
            jobs= fromDb
        else : 
            jobs=get_jobs(word)
            db[word]=jobs
    else : 
        return redirect("/")
    return render_template("report.html",resultsNumber = len(jobs), searchingBy=word)

app.run(host='127.0.0.1')