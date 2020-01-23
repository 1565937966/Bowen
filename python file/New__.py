class StringUpper(str):
	def __new__(cls,string):
		string=string.upper()
		print(cls)
		print(string)
		return str.__new__(cls,string)
