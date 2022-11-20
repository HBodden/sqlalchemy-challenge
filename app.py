from flask import Flask, jsonify

# Dictionary of Justice League
justice_league_members = [
    {"superhero": "Aquaman", "real_name": "Arthur Curry"},
    {"superhero": "Batman", "real_name": "Bruce Wayne"},
    {"superhero": "Cyborg", "real_name": "Victor Stone"},
    {"superhero": "Flash", "real_name": "Barry Allen"},
    {"superhero": "Green Lantern", "real_name": "Hal Jordan"},
    {"superhero": "Superman", "real_name": "Clark Kent/Kal-El"},
    {"superhero": "Wonder Woman", "real_name": "Princess Diana"}
]

#################################################
# Flask Setup
#################################################
# @TODO: Initialize your Flask app here
# YOUR CODE GOES HERE
app = Flask(__name__)
#################################################
# Flask Routes
#################################################

# @TODO: Complete the routes for your app here
# YOUR CODE GOES HERE
@app.route("/")
def Welcome():
    return(
        
        f"Welcome to Alchemy Challenge Weather API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start>/<end>"
    )

# Pretty print the data
@app.route("/api/v1.0/precipitation")
def precipitation():
   return "Precipitation"
    
@app.route("/api/v1.0/stations")
def stations():
    return "Stations"

@app.route("/api/v1.0/tobs/<tobs>")
def tobs():
    return stations(justice_league_members)

@app.route("/api/v1.0/<start>/<end>")
def temp_stats():
    return temp_stats(justice_league_members)

#Boilerplate 
if __name__ == "__main__":
    app.run(debug=True)
