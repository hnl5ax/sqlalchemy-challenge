{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "import datetime as dt\n",
    "import numpy as np\n",
    "import pandas as pd\n",
    "\n",
    "import sqlalchemy\n",
    "from sqlalchemy.ext.automap import automap_base\n",
    "from sqlalchemy.orm import Session\n",
    "from sqlalchemy import create_engine, func\n",
    "\n",
    "from flask import Flask, jsonify\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "ename": "AttributeError",
     "evalue": "Measurement",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mKeyError\u001b[0m                                  Traceback (most recent call last)",
      "\u001b[1;32m~\\AppData\\Local\\Continuum\\anaconda3\\lib\\site-packages\\sqlalchemy\\util\\_collections.py\u001b[0m in \u001b[0;36m__getattr__\u001b[1;34m(self, key)\u001b[0m\n\u001b[0;32m    209\u001b[0m         \u001b[1;32mtry\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 210\u001b[1;33m             \u001b[1;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_data\u001b[0m\u001b[1;33m[\u001b[0m\u001b[0mkey\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    211\u001b[0m         \u001b[1;32mexcept\u001b[0m \u001b[0mKeyError\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mKeyError\u001b[0m: 'Measurement'",
      "\nDuring handling of the above exception, another exception occurred:\n",
      "\u001b[1;31mAttributeError\u001b[0m                            Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-6-c22d962ba580>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      9\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     10\u001b[0m \u001b[1;31m# Save references to each table\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 11\u001b[1;33m \u001b[0mMeasurement\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mBase\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mclasses\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mMeasurement\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     12\u001b[0m \u001b[0mStation\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mBase\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mclasses\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mstation\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     13\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\AppData\\Local\\Continuum\\anaconda3\\lib\\site-packages\\sqlalchemy\\util\\_collections.py\u001b[0m in \u001b[0;36m__getattr__\u001b[1;34m(self, key)\u001b[0m\n\u001b[0;32m    210\u001b[0m             \u001b[1;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_data\u001b[0m\u001b[1;33m[\u001b[0m\u001b[0mkey\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    211\u001b[0m         \u001b[1;32mexcept\u001b[0m \u001b[0mKeyError\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 212\u001b[1;33m             \u001b[1;32mraise\u001b[0m \u001b[0mAttributeError\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mkey\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    213\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    214\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0m__contains__\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mkey\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mAttributeError\u001b[0m: Measurement"
     ]
    }
   ],
   "source": [
    "# Database Setup\n",
    "\n",
    "engine = create_engine(\"sqlite:///hawaii.sqlite\")\n",
    "\n",
    "# reflect an existing database into a new model\n",
    "Base = automap_base()\n",
    "# reflect the tables\n",
    "Base.prepare(engine, reflect=True)\n",
    "\n",
    "# Save references to each table\n",
    "Measurement = Base.classes.Measurement\n",
    "Station = Base.classes.station\n",
    "\n",
    "# Create our session (link) from Python to the DB\n",
    "session = Session(engine)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Flask Setup\n",
    "\n",
    "app = Flask(__name__)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Flask Routes\n",
    "\n",
    "\n",
    "@app.route(\"/\")\n",
    "def welcome():\n",
    "    return (\n",
    "        f\"Welcome to the Hawaii Climate Analysis API!<br/>\"\n",
    "        f\"Available Routes:<br/>\"\n",
    "        f\"/api/v1.0/precipitation<br/>\"\n",
    "        f\"/api/v1.0/stations<br/>\"\n",
    "        f\"/api/v1.0/tobs<br/>\"\n",
    "        f\"/api/v1.0/temp/start/end\"\n",
    "    )\n",
    "\n",
    "\n",
    "@app.route(\"/api/v1.0/precipitation\")\n",
    "def precipitation():\n",
    "    session = Session(engine)\n",
    "\n",
    "    \"\"\"Return the precipitation data for the last year\"\"\"\n",
    "    # Calculate the date 1 year ago from last date in database\n",
    "    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)\n",
    "\n",
    "    # Query for the date and precipitation for the last year\n",
    "    precipitation = session.query(Measurement.date, Measurement.prcp).\\\n",
    "        filter(Measurement.date >= prev_year).all()\n",
    "\n",
    "    # Dict with date as the key and prcp as the value\n",
    "    precip = {date: prcp for date, prcp in precipitation}\n",
    "    return jsonify(precip)\n",
    "\n",
    "\n",
    "@app.route(\"/api/v1.0/stations\")\n",
    "def stations():\n",
    "    session = Session(engine)\n",
    "\n",
    "    \"\"\"Return a list of stations.\"\"\"\n",
    "    results = session.query(Station.station).all()\n",
    "\n",
    "    # Unravel results into a 1D array and convert to a list\n",
    "    stations = list(np.ravel(results))\n",
    "    return jsonify(stations)\n",
    "\n",
    "\n",
    "@app.route(\"/api/v1.0/tobs\")\n",
    "def temp_monthly():\n",
    "    session = Session(engine)\n",
    "\n",
    "    \"\"\"Return the temperature observations (tobs) for previous year.\"\"\"\n",
    "    # Calculate the date 1 year ago from last date in database\n",
    "    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)\n",
    "\n",
    "    # Query the primary station for all tobs from the last year\n",
    "    results = session.query(Measurement.tobs).\\\n",
    "        filter(Measurement.station == 'USC00519281').\\\n",
    "        filter(Measurement.date >= prev_year).all()\n",
    "\n",
    "    # Unravel results into a 1D array and convert to a list\n",
    "    temps = list(np.ravel(results))\n",
    "\n",
    "    # Return the results\n",
    "    return jsonify(temps)\n",
    "\n",
    "\n",
    "@app.route(\"/api/v1.0/temp/<start>\")\n",
    "@app.route(\"/api/v1.0/temp/<start>/<end>\")\n",
    "def stats(start=None, end=None):\n",
    "    session = Session(engine)\n",
    "\n",
    "    \"\"\"Return TMIN, TAVG, TMAX.\"\"\"\n",
    "\n",
    "    # Select statement\n",
    "    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]\n",
    "\n",
    "    if not end:\n",
    "        # calculate TMIN, TAVG, TMAX for dates greater than start\n",
    "        results = session.query(*sel).\\\n",
    "            filter(Measurement.date >= start).all()\n",
    "        # Unravel results into a 1D array and convert to a list\n",
    "        temps = list(np.ravel(results))\n",
    "        return jsonify(temps)\n",
    "\n",
    "    # calculate TMIN, TAVG, TMAX with start and stop\n",
    "    results = session.query(*sel).\\\n",
    "        filter(Measurement.date >= start).\\\n",
    "        filter(Measurement.date <= end).all()\n",
    "    # Unravel results into a 1D array and convert to a list\n",
    "    temps = list(np.ravel(results))\n",
    "    return jsonify(temps)\n",
    "\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    app.run()\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
