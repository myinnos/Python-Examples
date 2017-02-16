import webbrowser
import time

total_breaks = 10
break_counts = 0

print("programme started at " + time.ctime())
while(break_counts < total_breaks):
    time.sleep(10) #10 secconds
    webbrowser.open_new_tab("http://github.com")
    break_counts = break_counts + 1 
