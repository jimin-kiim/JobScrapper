from flask import Flask, render_template,request,redirect
from scrapper import get_jobs
app=Flask("JobScrapper")

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/report")
def report():
    word=request.args.get('word')
    if word : 
        word=word.lower()
        # formatting
        jobs=get_jobs(word)
        print(jobs)
    else : 
        return redirect("/")
    return render_template("report.html",searchingBy=word)

app.run(host='127.0.0.1')


#  request : everytime I go to the website, that's a request. 