def normalize(value, unit):
	"""
	
	Normalizes passed value by unit
	
	Parameters
	----------
	value: str
		Numerical value
	unit: str
		Unit of measurement
	
	Returns
	-------
	float
		Normalized value
	
	"""	
	
	value = float(value)
	multiplier = 1024
	if 'K' in unit:
		return value / multiplier
	elif 'M' in unit:
		return value
	elif 'G' in unit:
		return value * multiplier
	else:
		raise ValueError("Unexpected unit: {}".format(unit))


def parser(string):
	"""
	
	Parses results of connection to iperf server
	
	Parameters
	----------
	string: str
		Connection results
	
	Returns
	-------
	[]
		Connection key value pair list
	"""
	
	result = []
	part_list = string.split()
	for index, element in enumerate(part_list):
		if "sec" == element:
			result.append({})
			result[len(result) - 1].update({"Interval": part_list[index - 1]})
		elif "Bytes" in element:
			result[len(result) - 1].update({"Transfer": normalize(part_list[index - 1], element)})
		elif "bits/sec" in element:
			result[len(result) - 1].update({"Bandwidth": normalize(part_list[index - 1], element)})
	return result

