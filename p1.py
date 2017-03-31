import webbrowser
import time


total_breaks = 1
break_count = 0
print( " This program started on "+time.ctime())

while(break_count < total_breaks):
     time.sleep(2)
     print(" TAKE A CHILL PILL ")
     webbrowser.open("https://www.youtube.com/watch?v=euCqAq6BRa4&list=RDQMugWvpXALBhk&index=9")


     break_count = break_count + 1
