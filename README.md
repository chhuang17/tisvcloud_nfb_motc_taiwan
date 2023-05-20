# Tisvcloud Package for Python
## User Guide
This is a convenient Python package for people who would like to download traffic data 
from https://tisvcloud.freeway.gov.tw/ (交通部高速公路局「交通資料庫」).

### Vehicle Detector (VD) Data
In version 0.1.0, this package provides users to check the vehicle detector (VD) one-minute data, 
including volume, speed, and occupancy. 
All you have to do is inputting the VDID you are interested in, which date you want to check, and what time.

#### 1. Check the volume for each VD
If you want to check the volume detected at 08:20, May 15, 2023, by VD-N3-S-44.985-M-LOOP, 
first, you have to import the `vd` package from the `tisvcloud`, and call the `volume` function:
```python
from tisvcloud import vd
vd.volume("VD-N3-S-44.985-M-LOOP", 20230515, 8, 20)

# You can also input the date, hour, and minute as a string.
vd.volume("VD-N3-S-44.985-M-LOOP", "20230515", "08", "20")
```

#### 2. Check the speed for each VD
If you want to check the speed (kph) detected at 08:20, May 15, 2023, by VD-N3-S-44.985-M-LOOP, you have to call the `speed` function:
```python
vd.speed("VD-N3-S-44.985-M-LOOP", 20230515, 8, 20)
```

#### 3. Check the occupancy for each VD
You can check the occupancy data (%) in the same way by calling the `occupy` function:
```python
vd.occupy("VD-N3-S-44.985-M-LOOP", 20230515, 8, 20)
```

#### 4. Download VD data
You can also just download the VD data by calling the `download` function and inputting the date and time you desire:
```python
vd.download(20230515, 8, 20)
```

### Changeable Message Sign (CMS) Data
#### 1. Check Message text for each CMS
In version 0.1.0, this package provides users to check the message shown in each changeable message sign (CMS) at that time on freeways.
All you have to do is inputting the CMSID you are interested in, which date you want to check, and what time. 
First, you have to import the `cms` package by the `tisvcloud`, and call the `message` function:
```python
from tisvcloud import cms
cms.message("CMS-N6-W-25.553-M", 20230203, 15, 0)

# You can also input the date, hour, and minute as a string.
cms.message("CMS-N6-W-25.553-M", "20230203", "15", "00")
```

#### 2. Download CMS Data
You can also just download the CMS data by calling the `download` function and inputting the date and time you desire:
```python
cms.download(20230203, 15, 0)
```

### ETC Data
In version 0.1.0, this package provides users to get data detected by ETC gantries on freeways.

**Note that the code '31' means the passenger , '32' means the small truck, '41' means the bus, '42' means the big truck, and '5' means the connected truck.**

#### 1. Volume detected by each ETC gantry
You can get the volume detected by each gantry through the code shown below, and it would return a dictionary for the volume in each vehicle type:
```python
from tisvcloud import etc
etc.volume("03F0447S", 20230519, 22, 0)
# output: {'31': 298, '32': 62, '41': 5, '42': 4, '5': 4}
```

#### 2. Median Travel Time between two consecutive gantries
You can get the median of the travel time between two consecutive gantries through the code shown below, and it would return a dictionary for the median of the travel time (seconds) in each vehicle type:
```python
etc.medianTravTime("03F0447S", "03F0498S", 20230519, 22, 0)
# output: {'31': 181, '32': 189, '41': 216, '42': 185, '5': 208}
```

#### 3. Median Travel Speed between two consecutive gantries
Also, you can get the median of the travel speed between two consecutive gantries through the code shown below, and it would return a dictionary for the median of the travel speed (kph) in each vehicle type:
```python
etc.medianSpeed("03F0447S", "03F0498S", 20230519, 22, 0)
# output: {'31': 100, '32': 93, '41': 82, '42': 97, '5': 86}
```

#### 4. Raw Data for each Trip in the past hour
If you want to check the raw data for each trip, you can execute the code shown below, and it would return a pandas dataframe:
```python
etc.tripData(20230518, 22, 0)
# output: pandas dataframe
```

#### 5. Mean Trip Length starting from each gantry
You can check the mean of the trip length starting from each gantry by calling the `tripLength` function, and it would return a dictionary for the mean of the trip length (km) in each vehicle type:
```python
etc.tripLength("03F0447S", 20230518, 22, 0)
# output: {'31': 19.8, '32': 19.0, '41': 15.9, '42': 31.3, '5': 85.1}
```

#### 6. OD-Pair between two arbitrary gantries
You can check the OD-Pair between two gantries arbitrarily like this, and it would return a dictionary for the volume between two gantries you choose in each vehicle type:
```python
etc.odPair("03F0447S", "03F0498S", 20230518, 22, 0)
# output: {'31': 13, '32': 4, '41': 1}
```

#### 7. Download ETC Data
You can also just download the ETC data by calling the `download` function and inputting the name of the ETC dataset, date, and time you desire:
**Note: The name of the ETC dataset includes M03A, M04A, M05A, M06A, M07A, and M08A**
```python
etc.download("M03A", 20230519, 22, 0)
```
