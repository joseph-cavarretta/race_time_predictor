##### RACE TIME PREDICTOR #####

print("\nRACE TIME PREDICTOR\n")
LTpace = input("Enter Threshold Pace: ")
distance = float(input("Enter Race Distance Miles: "))
LTpercent = float(input("Enter % of LT: "))
split_pace = LTpace.split(":")
minutes = int(split_pace[0])
seconds = int(split_pace[1])
pace = minutes * 60 + seconds
racepace = pace * float(LTpercent)
totaltime = racepace * distance

hours = int(totaltime // 3600)
timeLeft = totaltime % 3600
 
minutes = int(timeLeft // 60)
seconds = int(timeLeft % 60)

print("Race Time" + " = " + str(hours) + ':' + str(minutes) + ':' + str(seconds))
