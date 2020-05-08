#this is imported for Inter-Language Communication!
from subprocess import Popen, PIPE


#Open Connection for CPP!
MyPopen = Popen(['./handTracker'], shell=True, stdout=PIPE, stdin=PIPE)


while(1) :

  result = MyPopen.stdout.readline().strip()
  print(result)
