from weather import Weather
weather = Weather()


location = weather.lookup_by_location('halifax')
#condition = location.condition()
for forecasts in location.forecast():
#    print(forecasts) 
   #high_temp=forecasts['high']
    #rain=forecasts['Showers']
    if forecasts['text']== "Showers":
      print("It will rain on",forecasts['day'] )
