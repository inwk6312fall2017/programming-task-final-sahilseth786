from weather import Weather
weather = Weather()


location = weather.lookup_by_location('halifax')
condition = location.condition()
for forecasts in location.forecast():
  if forecasts['text']== "Showers":
      print("It will rain on",forecasts['day'] )
  for forecasts in location.forecast():
    if condition["temp"]  < forecasts["high"]:
	         high = forecasts['high']
		 day = forecasts["date"]

print("high temp",high)
print("on",day)

