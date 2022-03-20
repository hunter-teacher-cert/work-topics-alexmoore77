import random
#This is entirely original code by Alexander Moore.
#This is meant to be a transition matrix.  It is represented here as a Python dictionary rather than a two-dimensional array for ease of processing.  The numbers indicate the probability that the next state will occur based on the current state with 2*2 possible options.
myWeatherChain={
  "sunToSun": 0.90,
  "sunToRain": 0.10,
  "rainToSun": 0.50,
  "rainToRain": 0.50 
}

#This array holds the weather on each day.
weather=[]

weatherFirstDaySeed=random.uniform(0, 1)

#We choose the weather for the first day and then subsequently use the Markov chain myWeatherChain.
if weatherFirstDaySeed >=0.2:
  weather.append('sunny')
else:
  weather.append('rainy')

#Create weather for ten days using the Markov Chain.  With each iteration, update the currentDay to the last day in the weather list.  Generate a new random number each time from 0 to 1, and compare that with the current day using the criteria in the Markov Chain to determine the next day to append to the list
for x in range(10):

  currentDay=weather[len(weather)-1]
  currentRandomNumber=random.uniform(0,1)

  if currentDay=="sunny" and         currentRandomNumber<=myWeatherChain["sunToSun"]:
    weather.append('sunny')
  elif currentDay=="sunny" and (1-currentRandomNumber)<myWeatherChain["sunToRain"]:
    weather.append('rainy')
  elif currentDay=="rainy" and currentRandomNumber<=myWeatherChain["rainToSun"]:
    weather.append('sunny')
  elif currentDay=="sunny" and     (1-currentRandomNumber)<myWeatherChain["sunToRain"]:
    weather.append('rainy')

print(weather)
