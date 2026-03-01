#Name: Srinivas Solai	

#Roll Number:2602585

#Assignment: Python Loops & Automation - Subjective Question



print("===== Task 1: Find Maximum and Minimum =====")

temperatures = [28, 32, 35, 29, 31, 27, 30]



highest = temperatures[0]

lowest = temperatures[0]



for temp in temperatures:

  if temp > highest:

    highest = temp

  if temp < lowest:

    lowest = temp

print("Highest temperature: ", highest,"°C")

print("Lowest temperature: ", lowest,"°C")





print("\n===== Task 2: Count Hot Days =====")



temperatures = [28, 32, 35, 29, 31, 27, 30]

hotdays = 0

for temp in temperatures:

 if temp <= 30:

  continue

 hotdays += 1

print("Hotdays(>30°C:)",hotdays)





print("\n===== Task 3: Alert System =====")

temperatures = [28, 32, 35, 40, 31, 33, 30]

hotdays = 0

for hot in range(len(temperatures)):

  temp = temperatures[hot]

  

  if temp >= 40:

    print("Hot Days before alert:",hotdays)

    print("Alert! Extreme temperature 40°C detected on Day",hot +1)

    break

  

  if temp >30:

    hotdays +=1