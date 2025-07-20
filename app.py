from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
   return render_template("home.html")

@app.route("/about")
def about():
   return render_template("about.html")

@app.route("/square/<int:number>")
def square(number):
   """
   this route returns the square of the number
   """
   return f"The square of the {number} is {number**2}"

if __name__ == "__main__":
   app.run(debug=True, host = "0.0.0.0", port = 3000)
