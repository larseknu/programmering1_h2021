print("====Calculate your running zones based on average heartrate====")

# Getting the heartrate numbers from the user that we need for our calculations
average_5k_heartrate = input("Type in your average heartrate from your 5K runs: ")
average_5k_heartrate = float(average_5k_heartrate)
average_10k_heartrate = input("Type in your average heartrate from your 10K runs: ")
average_10k_heartrate = float(average_10k_heartrate)
# Take away the given number for the distance to get the lactate threshold
average_5k_heartrate -= 15
average_10k_heartrate -= 10

# The formula for the mean lactate threshold
lactate_threshold = (average_5k_heartrate + average_10k_heartrate) / 2
print(f"Your calculated lactate threshold is {lactate_threshold}")

# Calculating the different heartrate zones
zone1 = int(lactate_threshold * 0.80)
zone2_from = int(lactate_threshold * 0.81)
zone2_to = int(lactate_threshold * 0.89)
zone3_from = int(lactate_threshold * 0.89)
zone3_to = int(lactate_threshold * 0.95)
zone4_from = int(lactate_threshold * 0.96)
zone4_to = int(lactate_threshold * 0.99)
zone5 = int(lactate_threshold)

# Printing the information to the user
print(f"Your zone 1 is up to a heartrate of {zone1}")
print(f"Your zone 2 heartrate is from {zone2_from} to {zone2_to}")
print(f"Your zone 3 heartrate is from {zone3_from} to {zone3_to}")
print(f"Your zone 4 heartrate is from {zone4_from} to {zone4_to}")
print(f"Your zone 5 heartrate is above {zone5}")




