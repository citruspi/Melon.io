import re
import json
from service_map import service_map
import requests

class melonio:

    def __init__(self):

        pass
        
    def melonify(self, query):
                
        parts = re.match('^([^:]*):([^:]*):([^:]*)', query).groups()
        
        return (parts[0], parts[1], parts[2])
        
    def response(self, service, options, inputx, response=None, success=True, error=None):
        
        if success:
            
            return json.dumps(dict(response=response,
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
        
        
    def weather(param1, options, inputx):
                
        if not inputx.isdigit() and len(inputx) != 5:
            
            raise Exception("Invalid zip code.")
                        
        geocode_data = requests.get('http://maps.googleapis.com/maps/api/geocode/json?address=%s&sensor=false' % (inputx)).json()
                    
        lat, lng = geocode_data['results'][0]['geometry']['location']['lat'], geocode_data['results'][0]['geometry']['location']['lng']
                
        weather_data = requests.get('http://api.openweathermap.org/data/2.1/find/station?lat=%s&lon=%s&radius=10' % (lat, lng)).json()
                
        temp = (lambda x: '%.2f' % ((x-273.15) * 1.8 +32))(weather_data['list'][0]['main']['temp'])

        return 'Location:%s Temperature(F):%s' % (inputx, temp)

                
melonio = melonio()