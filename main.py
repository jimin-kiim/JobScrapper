from flask import Flask, render_template,request
app=Flask("JobScrapper")

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/report")
def report():
    word=request.args.get('word')
    return render_template("report.html",searchingBy=word)

app.run(host='127.0.0.1')


#  request : everytime I go to the website, that's a request. 