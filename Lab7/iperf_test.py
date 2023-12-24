#Import needed module for execution test
from parser import parser


class TestSuite():


	def test_iperf3_client_connection(self, client):
		"""
		
		Checks transfer and bandwidth of iperf connection
		
		Parameters
		----------
		client: ()
			Connection results and errors
		
		"""
		
		connection_results, connection_error = client
		assert not connection_error
		print("	> Recieved from fixture client is: {}".format(connection_results))
		result_list = parser(connection_results)
		for element in result_list:			
			assert element["Transfer"] > 128 and element["Bandwidth"] > 1024

