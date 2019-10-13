class Country():
    
    def __init__(self):
        self.data = load_census_file()
        self.zones = {'North':Zone(),'Northeast':Zone(),'South':Zone(),'Middle':Zone(),}
        self._iterateArea()
        
    def _iterateArea(self):
        for i in range(len(self.data)):
            for j in range(len(self.data[0])):
                self._updateArea(i,j)
                
    def _getZones(self):
        return self.zones
    
    def _getHighestPopulationZone(self):
        inverse = [(value._getPopulation(), key) for key, value in self.zones.items()]
        return max(inverse)[1]
    
    def _updateArea(self,i,j):
        if self.data[i][j] < 1:
            return
        if i < 11 and j < ord('M')-ord('A')+1:
            self.zones['North']._updateZone(self.data[i][j])
        elif 10 < i < 17 and j < ord('E')-ord('A')+1:
            self.zones['North']._updateZone(self.data[i][j])
        elif i < 31 and j > ord('M')-ord('A'):
            self.zones['Northeast']._updateZone(self.data[i][j])
        elif i > 32:
            self.zones['South']._updateZone(self.data[i][j])
        else:
            self.zones['Middle']._updateZone(self.data[i][j])

class Zone():
    
    def __init__(self,pop=0,area=0):
        self.pop = pop
        self.area = area
        
    def _updateZone(self,data):
        self.pop += data
        self.area += 10 #sq.km
        
    def _getPopulation(self):
        return self.pop
    
    def _getArea(self):
        return self.area
    
    def _getDensity(self):
        return self.pop/self.area

def load_census_file():
    lines = open('/tmp/census.txt').read().splitlines()
    data = []
    for line in lines:
        line_list = line.split(',')
        int_list = []
        for i in line_list:
            if i == '':
                int_list.append(0)
            else:
                int_list.append(int(i))
        data.append(int_list)
    return data

country = Country() # Generate country's object
res = country._getHighestPopulationZone()
print(f'Country with highest population is {res}.')
print(f'Population: {country._getZones()[res]._getPopulation()}')
print(f'Density: {country._getZones()[res]._getDensity():.2f} people per sq.km.')
