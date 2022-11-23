import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify
import datetime as dt

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

# Homepage.
#List all available routes.
@app.route("/")
def Welcome():
    return(
        
        f"Welcome to Alchemy Challenge Weather API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end>"
    )

# Convert the query results to a dictionary using date as the key and prcp as the value.
#Return the JSON representation of your dictionary.
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

#Return a JSON list of stations from the dataset.
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

#Query the dates and temperature observations of the most active station 
#for the previous year of data.
#Return a JSON list of temperature observations (TOBS) for the previous year.

@app.route("/api/v1.0/tobs")
def tobs():
    # Create session from Python to the DB
    session = Session(engine)

    date_calc =  dt.date(2017, 8, 23) - dt.timedelta(days=365)

    """Return a list of all dates and precipitation measurement values"""
    results = session.query(Measurement.prcp).filter(Measurement.date > date_calc).all()

    session.close()

    # Convert list of tuples into normal list
    #The ravel function flattens an array(list of lists into one list)
    #from [[1],[2],[3]] to [1, 2, 3]
    all_measurements = list(np.ravel(results))

    return jsonify(all_measurements)

# Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a given start or start-end range.

# When given the start only, calculate TMIN, TAVG, and TMAX for all dates greater than or equal to the start date.

@app.route("/api/v1.0/<start>")
def by_date(start):
    # Create session from Python to the DB
    session = Session(engine)
    
    """Return TMIN, TAVG, and TMAX for all dates greater than or equal to the start date."""
   
    results = session.query(func.max(Measurement.tobs),func.min(Measurement.tobs),func.avg(Measurement.tobs)).filter(Measurement.date >= start).all()

    session.close()

   
    #temps = [max_temp[0][0],min_temp[0][0],avg_temp[0][0]]
    temps = list(np.ravel(results))
      
    return jsonify(temps)

# When given the start and the end date, calculate the TMIN, TAVG, and TMAX for dates from the start date through the end date (inclusive).

@app.route("/api/v1.0/<start>/<end>")
def date_range(start,end):
    # Create session from Python to the DB
    session = Session(engine)
    #date_calc =  dt.date.(start_dt) - dt.timedelta(days=365)

    """Return the TMIN, TAVG, and TMAX for dates from the start date through the end date (inclusive)."""
    results = session.query(func.max(Measurement.tobs),func.min(Measurement.tobs),func.avg(Measurement.tobs)).filter(Measurement.date >= start).filter(Measurement.date <= end).all()
    
    session.close()

    all_temps = list(np.ravel(results))
    
    return (all_temps)

#Boilerplate 
if __name__ == "__main__":
    app.run(debug=True)
