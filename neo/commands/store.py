class Store:

	global data

	def getData(self):
		return self.data

	@classmethod
	def setData(self, _data):
		self.data = _data