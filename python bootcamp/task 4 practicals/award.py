'''
Psuedo Code

swimming time = input integer "What was your time in the swimming event (in minutes)? "
cycling time = input integer "What was your time in the cycling event (in minutes)? "
running time = input integer "What was your time in the running event (in minutes)? "

total time = swimming + cycling + running 
print total time

if total time >= 111:
    print "no reward" 
elif (total time >= 0) and (total time <= 100):
    print "provincial colours"
elif (total time 101) and (total time <= 105):
    print "provincial half colours"
elif (total time >= 106) and (total time <= 110):
    print "provincial scroll"

'''

swim_time = int(input("What was your time in the swimming event (in minutes)? "))
cycle_time = int(input("What was your time in the cycling event (in minutes)? "))
run_time = int(input("What was your time in the running event (in minutes)? "))

total_time = swim_time + cycle_time + run_time
print(f"Your total time is {total_time}!")

if total_time >= 111:
    print("You've recieved no reward :(")
elif (total_time >= 0) and (total_time <= 100):
    print("You've recieved Provincial Colours!")
elif (total_time >= 101) and (total_time <= 105):
    print("You've recieved Provincial half Colours!")
elif (total_time >= 106) and (total_time <= 110):
    print("You've recieved Provincial Scroll!")