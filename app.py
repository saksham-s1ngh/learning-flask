from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
   return "<h1>Welcome to the homepage!</h1>"

@app.route("/about")
def about():
   return """We are a non-profit organization working as an animal rescue. We aim to help you connect with the purrfect furbaby for you! 
   The animals you find on our website are rescued and rehabilitated animals. Our mission is to promote the ideology \"adopt, don't hop\"! """ 

@app.route("/square/<int:number>")
def square(number):
   """
   this route returns the square of the number
   """
   return f"The square of the {number} is {number**2}"

if __name__ == "__main__":
    app.run(debug=True, host = "0.0.0.0", port = 3000)
