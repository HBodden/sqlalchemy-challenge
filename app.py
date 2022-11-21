import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

#set up app.py file to read in the climate information
#Database set up
engine = create_engine("sqlite:///./Resources/hawaii.sqlite")
#refelct database into new model 
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station

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
   # Create session (link) from Python to the DB
    session = Session(engine)

    """Return a list of precipitation values using the date as the key"""
    # Query all measurements 
    results = session.query(Measurement.date, Measurement.prcp).all()

    session.close()

    # Create a dictionary using the data in results and append to a list of all_data
    #The list holds all passengers
    all_data = []
    for date, prcp in results:
        #create an object for each individual passenger
        prec_dict = {}
        prec_dict[date] = prcp
        #prec_dict["prcp"] = prcp
        all_data.append(prec_dict)

    return jsonify(all_data)
    
@app.route("/api/v1.0/stations")
def stations():
     # Create session from Python to the DB
    session = Session(engine)

    """Return a list of all station names"""
    # Query all stations
    results = session.query(Station.name).all()

    session.close()

    # Convert list of tuples into normal list
    #The ravel function flattens an array(list of lists into one list)
    #from [[1],[2],[3]] to [1, 2, 3]
    all_names = list(np.ravel(results))

    return jsonify(all_names)

@app.route("/api/v1.0/tobs")
def tobs():
    

@app.route("/api/v1.0/<start>/<end>")
def temp_stats():
    

#Boilerplate 
if __name__ == "__main__":
    app.run(debug=True)
