from datetime import datetime, time
import pandas as pd

onTime1 = time(8, 20, 0)
offTime1 = time(20, 00, 0)
onTime2 = time(8, 21, 0)
offTime2 = time(20, 1, 0)

timeRange = pd.date_range("00:00", "23:59:59", freq = "1s").time

schedule1 = open('LightSchedule1.dat', 'w')
schedule2 = open('LightSchedule2.dat', 'w')

intensity1 = [0] * len(timeRange)
intensity2 = [0] * len(timeRange)

for i in range(len(timeRange)):
 if timeRange[i] > onTime1 and timeRange[i] < offTime1:
  intensity1[i] = min(intensity1[i-1] + 1, 255)
 if timeRange[i] >= offTime1:
  intensity1[i] = max(intensity1[i-1] - 1, 0)
 if timeRange[i] > onTime2 and timeRange[i] < offTime2:
  intensity2[i] = min(intensity2[i-1] + 1, 255)
 if timeRange[i] >= offTime2:
  intensity2[i] = max(intensity2[i-1] - 1, 0)
 L1 = [timeRange[i].strftime("%H:%M:%S"), "\t", str(intensity1[i]), "\n"]
 L2 = [timeRange[i].strftime("%H:%M:%S"), "\t", str(intensity2[i]), "\n"]
 schedule1.writelines(L1)
 schedule2.writelines(L2)
schedule1.close()
schedule2.close()
