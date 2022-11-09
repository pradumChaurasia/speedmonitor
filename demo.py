import psutil
import math
import speedtest

print(psutil.cpu_count())

# while True:
#     print(psutil.cpu_percent(1))



print('Total system memoryis:',math.floor(psutil.virtual_memory()[0]/1000000000))#in gigs
print('Available memoryis:',math.floor(psutil.virtual_memory()[1]/1000000000))
print('Percent memoryis:',psutil.virtual_memory()[2])
print('Used  memoryis:',math.floor(psutil.virtual_memory()[3]/1000000000))
print('Free memoryis:',math.floor(psutil.virtual_memory()[4]/1000000000))

#getting the n/w speed
st=speedtest.Speedtest()
print("Download speed:",math.floor(st.download()/1000000))#converting these speed into mb from bytes/sec
print("upload speed:",math.floor(st.upload()/1000000))
print("The ping is:",st.results.ping)