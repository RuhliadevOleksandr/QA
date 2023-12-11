#Import needed module for executing Lonux commands
import subprocess


#iperf server IP adress 
server_ip = '192.168.56.1'


def client():
    """
    
    Connects to the iperf server at the passed IP adress 
    
    Returns
    ----------
    ()
        Connection results and error 
    """
    
    return subprocess.Popen(f"iperf -c {server_ip} -i 1".split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True).communicate()
  

def parser(string):
    """
    
    Parses results of connection to iperf server 
    
    Parameters
    ----------
    string: str
    	Connection results
    
    Returns
    ----------
    []
        Connection key value pair list 
    """
    
    result = []
    part_list = string.split('  ')
    for element in part_list:
    	if ' sec' in element:
    	    result.append({})
    	    result[len(result) - 1].update({'Interval': element})
    	elif 'Bytes' in element:
    	    result[len(result) - 1].update({'Transfer': element})
    	elif '/sec' in element:
    	    result[len(result) - 1].update({'Bandwidth': element.split('\n')[0]})
    return result


connection_results, connection_error = client()
if connection_error:
    print(connection_error)
else:
    result_list = parser(connection_results)
    for element in result_list:
        bandwidth_values = element['Bandwidth'].split()
        if float(bandwidth_values[0]) > 1 and bandwidth_values[1] == 'Gbits/sec':
            print(element)
