class appFunctions:
    def __init__(self, main_app):
        self.main_app = main_app
        self.dataSimulation = self.main_app.dataSimulation
        self.update_lcd_display() 
           
    def motivation_button_clicked(self):
        pass
    
    def realiste_button_clicked(self):
        pass
    
    def update_lcd_display(self):
        data = self.dataSimulation.get_data()
        self.main_app.humidityLCD.display(f"{data['humidity']}%")
        self.main_app.temperatureLCD.display(f"{data['temperature']}°C")
    
    def update_graphics_view(self, data):
        pass
    
    