print '*************** First Come First Serve *******************'

process_list=[]
n=int(raw_input('Plx enter total no. of processes:'))

for i in range(n):
	process_list.append([])
	process_list[i].append(raw_input('Enter the process name:'))
	process_list[i].append(int(raw_input('Enter the arrival time')))
	process_list[i].append(int(raw_input('Enter the Burst Time')))

process_list.sort(key=lambda process_list:process_list[1])

arrival_time=[]

for i in range(n):
	arrival_time.append([])
	arrival_time[i]=process_list[i][1]

for i in range(n):
	print process_list[i][0]
	print process_list[i][1]

status=arrival_time[0]
start_time=[]
for  i in range(n):
	start_time.append([])
	start_time[i]=status
	status=start_time[i]+process_list[i][2]


print 'The waiting Time for the processes given above is:'
for i in range(n):
	print start_time[i]-arrival_time[i]

total_waiting_time=0
for i in range(n):
	total_waiting_time+=start_time[i]-arrival_time[i]

print ' '
print 'And avrg. waiting time is:',total_waiting_time/n
