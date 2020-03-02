from app import app

@app.route("/")
def home():
    return render_template("home.html")
    
@app.route("/help")
def help():
    return "Help"
    
if __name__ == "__main__":
    app.run(debug=True)