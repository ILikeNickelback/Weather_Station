

class dataSimulation():
    def __init__(self):
        
        self.temperature = 15.3
        self.humidity = 45.2
        self.carbon_dioxide = 400.0
        
        
        
        self.data = {
            'temperature': self.temperature,
            'humidity': self.humidity,
            'carbon_dioxide': self.carbon_dioxide
        }
        

    def get_data(self):
        return self.data