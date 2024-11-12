from geopy.distance import great_circle as GD 

df["distance"] = df.apply(lambda x: abs(12756 - GD((x["pickup_latitude"], x["pickup_longitude"]), 
                                       (x["dropoff_longitude"], x["dropoff_longitude"])).km), axis=1)