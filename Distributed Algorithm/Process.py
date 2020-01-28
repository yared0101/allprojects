import threading
import random
import time
class threadd(threading.Thread):
	p=[]
	myTimeStamp=6.6
	i=0
	def __init__(self,i,p,x,myTimeStamp):
		super().__init__()
		self.p=p
		self.myTimeStamp=myTimeStamp
		self.x=x
		self.i=i
	def run(self):
		self.p[self.i].recieveRequest(self.myTimeStamp)
		self.x[0]+=1
class Process:
	p=[]
	runningStatus=""
	pid=0
	myTimeStamp="-1"
	dush=0
	x=[0]
	num=0


	def __init__(self,k,number_p,p):
		self.pid=k
		self.num=number_p
		self.runningStatus="concurrent"
		self.p=p;
		


	def criticalRegion(self):
		print(self.pid*"\t\t|",self.pid,".inside CR")
		time.sleep(7)
		print(self.pid*"\t\t|",self.pid,".left CR")
		self.myTimeStamp="-1"



	def recieveRequest(self,timeStamp):
		if(self.runningStatus == "concurrent"):
			return "ok"
		elif(self.runningStatus == "series"):
			self.addQueue()
			return "ok"
		elif(self.runningStatus == "underRequest"):
			if(self.myTimeStamp > timeStamp or self.myTimeStamp=="-1" ):
				return "ok"
			else:
				self.addQueue();
				return "ok"
		return ""


	def addQueue(self):
		while(self.runningStatus != "concurrent"):
			pass


	def start(self):
		time.sleep(int (random.random()*3)+1)
		randi=int (random.random()*10)
		self.myTimeStamp=str(time.time())
		d=list(self.myTimeStamp)
		d[-1]=str(self.pid)
		self.myTimeStamp="".join(d)
		if(randi==1):
			self.x=[0]
			print(self.pid*"\t\t|",self.pid,".underReq")
			self.runningStatus="underRequest"
			i=0
			#requesting permission(sending message goes through here)
			while(i<self.num):
				if(i==self.pid):
					i+=1
					continue
				dude=threadd(i,self.p,self.x,self.myTimeStamp)
				dude.start()
				i+=1
			#wait for all processes permission
			while(self.x[0]<self.num-1):
				pass
			self.runningStatus="series"
			self.criticalRegion()
			self.runningStatus="concurrent"

			self.x[0]=0
		self.start()

class first(threading.Thread):
	i=0
	processNumber=10
	p=[]
	def __init__(self,i,processNumber,p):
		super().__init__()
		self.i=i
		self.processNumber=processNumber
		self.p=p
	def run(self):
		p[self.i]=Process(i,processNumber,p)
		p[self.i].start()
processNumber=5
i=0	
p=[]
while(i<processNumber):
	p.append(0)
	i+=1
i=0
while(i<processNumber):
	starter=first(i,processNumber,p)
	starter.start()
	i+=1
