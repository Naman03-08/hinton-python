import weatherdesk
temp, rain = weatherdesk.weather_now("Mumbai")

city = str(input())
price = float(input())
orders = int(input())
riders = int(input())

pressure = orders / riders
reason = ""

if(rain > 0 and pressure > 3):
    sauge = 1.5
    reason = "raining AND every rider is buried in orders"
elif(rain > 0):
    sauge = 1.3
    reason = "raining - fewer riders want to go out"
elif(temp >= 33 and pressure > 3):
    sauge = 1.4
    reason = "heat wave AND riders are stretched thin"
elif(temp >= 33):
    sauge = 1.2
    reason = "heat wave - nobody wants to step outside"
elif(pressure > 4):
    sauge = 1.25
    reason = "dry and pleasant, but demand is running ahead of riders"
else:
    sauge = 1.0
    reason = "calm hour - charge the normal price"
    
final_price = price * sauge

print(f"Temperature: {temp} C")
print(f"Rain: {rain} mm")
print(f"Orders per rider: {pressure}")
print(f"Surge: {sauge}")
print(f"Reason: {reason}")
print(f"Price: {final_price}")