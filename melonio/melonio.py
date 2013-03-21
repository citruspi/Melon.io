import re
import json
from service_map import service_map
import requests
from config import config
from bs4 import BeautifulSoup

class melonio:

    def __init__(self):

        pass
        
    def melonify(self, query):
                
        parts = re.match('^([^:]*):([^:]*):([^:]*)', query).groups()
        
        return (parts[0], parts[1], parts[2])
        
    def response(self, service, options, inputx, response=None, success=True, error=None):
        
        if success:
            
            return json.dumps(dict(success=success,
                                   response=response,
                                   query=dict(service=service,
                                              options=options,
                                              input=inputx)))
                                              
        else:
            
            return json.dumps(dict(success=False,
                                   error=error,
                                   query=dict(service=service,
                                              options=options,
                                              input=inputx)))



    def solve(self, query):
        
        service, options, inputx = self.melonify(query)            
                                                  
        try:
            
            if service_map.has_key(service):
                
                responsex = getattr(self, service_map[service])(options, inputx)
        
                return self.response(service=service,options=options,inputx=inputx,response=responsex)
                
            else: raise Exception("Service not implemented.")
            
        except Exception, e:
            
            return self.response(service=service,options=options,inputx=inputx,success=False,error=str(e))
        
        
    def weather(self, options, inputx):
                
        if not inputx.isdigit() and len(inputx) != 5:
            
            raise Exception("Invalid zip code.")
                        
        data = requests.get('http://api.wunderground.com/api/%s/forecast/geolookup/conditions/q/%s.json' %
                            (config['API_KEYS']['WUNDERGROUND'], inputx)).json()['current_observation']

        return 'Location: %s Condition: %s Temperature: %s Feels Like: %s Wind: %s Humidity: %s' % (inputx, 
                                                                                                      data['weather'],
                                                                                                      data['temperature_string'],
                                                                                                      data['feelslike_string'],
                                                                                                      data['wind_string'],
                                                                                                      data['relative_humidity'])

    def urban_dict(self, options, inputx):
     
        data = requests.get('http://www.urbandictionary.com/define.php?term=%s' % (inputx)).text
        
        soup = BeautifulSoup(data)
        
        definitions = soup.findAll('div', {'class': 'definition'})
        
        if len(definitions) == 0:
          
            raise Exception("Term not defined.")
            
        return definitions[0].getText()
       
  
melonio = melonio()