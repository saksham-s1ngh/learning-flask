from flask import Flask, render_template, redirect
app = Flask(__name__)

"""Information regarding the Pets in the System."""
pets = [
            {"id": 1, "name": "Nelly", "age": "5 weeks", "bio": "I am a tiny kitten rescued by the good people at Paws Rescue Center. I love squeaky toys and cuddles."},
            {"id": 2, "name": "Yuki", "age": "8 months", "bio": "I am a handsome gentle-cat. I like to dress up in bow ties."},
            {"id": 3, "name": "Basker", "age": "1 year", "bio": "I love barking. But, I love my friends more."},
            {"id": 4, "name": "Mr. Furrkins", "age": "5 years", "bio": "Probably napping."}, 
        ]

@app.route("/")
def home():
   return render_template("home.html", pets_info=pets)

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
