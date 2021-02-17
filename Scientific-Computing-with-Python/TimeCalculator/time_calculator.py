def add_time(start, duration, day = None):
  hour = start.split(':')[0]
  minute = start.split(':')[1].split(' ')[0]
  ampm = start.split(' ')[1]
  ampmdict = {0: 'PM', 1: 'AM'}
  if (ampm == 'AM'):
    ampmdict = {0: 'AM', 1: 'PM'}
    
  resulthour = (int(hour) + int(duration.split(':')[0])) % 12
  resultminute = '{:02d}'.format((int(minute) + int(duration.split(':')[1])) % 60)
  resulthour += int((int(minute) + int(duration.split(':')[1])) / 60)
 
  resultampm = ampmdict[int(((int(hour) + int(duration.split(':')[0]) + int((int(minute) + int(duration.split(':')[1])) / 60)) / 12) % 2)]

  days = ((int(hour) + int(duration.split(':')[0]) + int((int(minute) + int(duration.split(':')[1])) / 60)) / 24)
  if (ampm == 'PM'):
    days = int((int(hour) + 12 + int(duration.split(':')[0]) + int((int(minute) + int(duration.split(':')[1])) / 60)) / 24)
  
  resultdays = ""
  if (int(days) == 1):
    resultdays = " (next day)"
  elif (int(days) > 1):
    resultdays = " (" + str(days) + " days later)"

  resultdayweek = ""
  daysweek = {0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday", 4: "Friday", 5: "Saturday", 6: "Sunday"}
  daysweekinversed = {"monday": 0, "tuesday": 1, "wednesday": 2, "thursday": 3, "friday": 4, "saturday": 5, "sunday": 6}
  if (day):
    resultdayweek = ", " + daysweek[(int(days) % 7 + daysweekinversed[day.lower()]) % 7]
    
  return str(resulthour) + ':' + str(resultminute) + " " + resultampm + resultdayweek + resultdays