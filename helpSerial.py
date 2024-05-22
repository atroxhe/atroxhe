#by atrox.he


import serial
from serial.tools.list_ports import comports
import time



class Communication():


	def __init__(self, comports, bps , timeout):

		self.port = comports
		self.bps = bps
		self.timeout = timeout
		global Ret

		try:
			self.main_engine = serial.Serial(self.port, self.bps, timeout = self.timeout)

			if (self.main_engine.is_open):
				Ret = True
		except Exception as e:
			print(" open serial fail", e)


	def Print_Name(self):
		print(self.main_engine.name)
		print(self.main_engine.port)
		print(self.main_engine.baudrate)
		print(self.main_engine.bytesize)
		print(self.main_engine.parity)
		print(self.main_engine.stopbits)
		print(self.main_engine.timeout)
		print(self.main_engine.writeTimeout)
		print(self.main_engine.xonxoff)
		print(self.main_engine.rtscts)
		print(self.main_engine.dsrdtr)
		print(self.main_engine.interCharTimeout)

	def Open_Engine(self):
		self.main_engine.open()


	def Close_Engine(self):
		self.main_engine.close()
		print(self.main_engine.is_open)


	@staticmethod
	def print_used_com():
		port_list = comports()
		i = 1
		ports = {}
		descs = {}
		hwids = {}
		for port, desc, hwid in sorted(port_list):
				print(f"{port} - {desc} ({hwid}) --" + str(i) )
				ports[i] = port
				descs[i] = desc
				hwids[i] = hwid
				i = i + 1 
		return ports, descs, hwids

		


	def Read_Size(self, size):
		return self.main_engine.read(size = size)

	def Read_Line(self):
		return self.main_engine.readline()

	def Send_data(self, data):
		# self.main_engine.write(data.encode('utf-8'))

		self.main_engine.write(data.encode('utf-8'))


	def Recive_data(self, way):
		print("start recive data: ")
		while True:
			try:
				if self.main_engine.in_waiting:
					if(way == 0):
						for i in range(self.main_engine.in_waiting):
							print("recive ascii data: " + str(self.Read_Size(1)))
							data1 = self.Read_Size(1).hex()
							data2 = int(data1, 16)
							print("recive 16 bit data " + str(data1) + "recive 10 bit data " + str(data2))
					if(way == 1):
						data = self.main_engine.read_all()
						print(data.decode('utf-8'))
			except Exception as e:
				print("recive data error", e)

ports, descs, hwids = Communication.print_used_com()
Ret = False
i = input("input need open port")
print("ports", ports)
print("open this port ", ports[int(i)])
# baudrate_of_port = input("input baudrate you choose")
port1 = Communication(ports[int(i)], 115200, 1)
print(port1.Print_Name())
while Ret == True:
		command222 = input("input command")
		command333 = command222 + '\r\n'
		print(command333)
		port1.Send_data(command333)
		time.sleep(1)
		dataRead = port1.main_engine.read_all()
		time.sleep(1)
		print(dataRead.decode('utf-8'))
