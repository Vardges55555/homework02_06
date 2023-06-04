"""A.M. – ante meridiem, «до полудня», интервал с 00:00 до 12:00. P.M. – post meridiem,
 что на латыни «после полудня», интервал с 12:00 до 00:00"""

hour = int(input("Enter hour: "))
time_am_pm = input("am (1) or pm (2)? ")
hour_add = int(input("How many hours ahead? "))

new_hour = (hour + hour_add) % 12

if time_am_pm == '2':
    new_hour += 12

if new_hour < 12:
    peroid_text = 'am'
else:
    period_text = 'pm'

print("New Hour!", new_hour, period_text)
