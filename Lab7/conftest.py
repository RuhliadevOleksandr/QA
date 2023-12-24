#Import needed module for configuration test
import paramiko
import subprocess
import pytest


#Define server data
ip_address = "192.168.56.1"
password = "password"
username = "user"


@pytest.fixture
def server():
	"""
	
	Connects to server using ssh
	
	Returns
	-------
	str
		Connection error
	
	"""
	
	sshClient = paramiko.client.SSHClient()
	sshClient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	sshClient.connect(ip_address, username=username, password=password)
	_, _, _ = sshClient.exec_command("pkill iperf")
	_, _, stderr = sshClient.exec_command("iperf -s")
	sshClient.close()
	return stderr.read().decode()
	

@pytest.fixture
def client(server):
	"""
	Connects to iperf server
	
	Parameters
	----------
	server: str
		Connection error
	
	Returns
	-------
	()
		Connection results and error
	"""
	
	if server:
		return ("", server)
	return subprocess.Popen(f"iperf -c {ip_address} -i 1".split(), stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, text=True).communicate()

