
import plotly.plotly as py # plotly library
  import json # used to parse config.json
  import time # timer functions
  import datetime # log and plot current time
  import sys
  import Adafruit_DHT

with open('./config.json') as config_file:
  plotly_user_config = json.load(config_file)
  
  py.sign_in(plotly_user_config["plotly_username"], plotly_user_config["plotly_api_key"])

url = py.plot([
  {
      'x': [], 'y': [], 'type': 'scatter',
      'stream': {
        'token': plotly_user_config['plotly_streaming_tokens'][0],
        'maxpoints': 200
      }
  }], filename='Temperature')
    
print "View your streaming graph here: ", url

stream = py.Stream(plotly_user_config['8w88bpgxr5'][0])
stream.open()

# Type of sensor, can be Adafruit_DHT.DHT11, Adafruit_DHT.DHT22, or Adafruit_DHT.AM2302. 
DHT_TYPE = Adafruit_DHT.DHT22 

# Example of sensor connected to Raspberry Pi pin ?? might be pin 7 or 4
DHT_PIN  = 7

# How long to wait (in seconds) between measurements.
FREQUENCY_SECONDS      = 30

while True: 
  # Attempt to get sensor reading. 
  humidity, temp = Adafruit_DHT.read(DHT_TYPE, DHT_PIN)
  
  # Skip to the next reading if a valid measurement couldn't be taken. 
  # This might happen if the CPU is under a lot of load and the sensor 
  # can't be reliably read (timing is critical to read the sensor). 
  if humidity is None or temp is None: 
    time.sleep(2) 
    continue 

    print 'Temperature: {0:0.1f} C'.format(temp) 
   # print 'Humidity:    {0:0.1f} %'.format(humidity) 
    
  # write the data to plotly
      stream.write({'x': datetime.datetime.now(), 'y': temp})

  # delay between stream posts
  time.sleep(FREQUENCY_SECONDS)


