from flask import Flask
app=Flask("JobScrapper")

@app.route("/")
# decorator : looks for a function right below itself and decorate it. 
def home():
    return "Hello ! "

@app.route("/contact")
def contact():
    return "Contact Me !"

@app.route("/<username>")
# <> : placeholder
def user(username):
    return f"Hello {username} How are you doing? "

    
app.run(host='127.0.0.1')