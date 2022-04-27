#Часовая стрелка образует угол y с лучом, проходящим через центр и через точку,
#соответствующую 12 часам на циферблате, . Определить значение угла для
#минутной стрелки, а также количество полных часов и полных минут.
y = int(input("Enter the angle that the beam and the hour hand form: "))
ch = y//30
min = y%30
print("Minute hand angle: ", min*12)
print("TIME: ", ch, "hours", min, "minutеs")
