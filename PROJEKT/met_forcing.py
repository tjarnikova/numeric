import numpy as np 
import yaml
from collections import namedtuple

timeStep = 55

class MetDEF():

	def __init__(self, coeffFileName):
		with open(coeffFileName, 'rb') as f:
			config = yaml.load(f)
		self.config = config
		icevars = namedtuple('icevars',config['icevars'].keys())
		self.icevars = icevars(**config['icevars'])

	def met_forcing(self,timeStep):

		if (timeStep < 32.):
			ice = self.icevars.Jan
		elif (timeStep >=32 & timeStep < 60 ):
			ice = self.icevars.Feb
		elif (timeStep >=60 & timeStep < 91 ):
			ice = self.icevars.Mar		
		elif (timeStep >=91 & timeStep < 121 ):
			ice = self.icevars.April 
		elif (timeStep >=121 & timeStep < 152 ):
			ice = self.icevars.May
		elif (timeStep >=152 & timeStep < 182 ):
			ice = self.icevars.June
		elif (timeStep >=182 & timeStep < 213 ):
			ice = self.icevars.July
		elif (timeStep >=213 & timeStep < 244 ):
			ice = self.icevars.Aug
		elif (timeStep >=244 & timeStep < 274 ):
			ice = self.icevars.Sept
		elif (timeStep >=274 & timeStep < 305 ):
			ice = self.icevars.Oct
		elif (timeStep >=305 & timeStep < 335 ):
			ice = self.icevars.Nov
		elif (timeStep >= 335):
			ice = self.icevars.Dec

		return(ice)


theSolver = MetDEF('test.yaml')
w = theSolver.met_forcing(timeStep)
print(w)
