from tisvcloud.PublicClass import MOTCLiveData
import xml.etree.ElementTree as ET
import gzip
import numpy as np


__version__ = "0.1.0"

# Hierachy 0
# VDLives:           root[-1]

# Hierachy 1
# VDLive:            root[-1][i]                                (=VDLives[i])   [i=number of VDs]

# Hierachy 2
# VDID:              root[-1][i][0].text                        (=VDLives[i][0].text)
# LinkFlows:         root[-1][i][1]                             (=VDLives[i][1])
# Status:            root[-1][i][2].text                        (=VDLives[i][2].text)
# DataCollectTime:   root[-1][i][-1].text                       (=VDLives[i][-1].text)

# Hierachy 3
# LinkFlow:          root[-1][i][1][0]                          (=VDLives[i][1][0])

# Hierachy 4
# LinkID:            root[-1][i][1][0][0].text                  (=VDLives[i][1][0][0].text)
# Lanes:             root[-1][i][1][0][1]                       (=VDLives[i][1][0][1])

# Hierachy 5
# Lane:              root[-1][i][1][0][1][j]                    (=VDLives[i][1][0][1][j])   [j=number of Lanes]

# Hierachy 6
# LaneID:            root[-1][i][1][0][1][j][0].text            (=VDLives[i][1][0][1][j][0].text)
# LaneType:          root[-1][i][1][0][1][j][1].text            (=VDLives[i][1][0][1][j][1].text)
# Speed:             root[-1][i][1][0][1][j][2].text            (=VDLives[i][1][0][1][j][2].text)
# Occupancy:         root[-1][i][1][0][1][j][3].text            (=VDLives[i][1][0][1][j][3].text)
# Vehicles:          root[-1][i][1][0][1][j][-1]                (=VDLives[i][1][0][1][j][-1])

# Hierachy 7
# Vehicle:           root[-1][i][1][0][1][j][-1][k]             (=VDLives[i][1][0][1][0][-1][k])    [k=number of VehType]

# Hierachy 8
# VehicleType:       root[-1][i][1][0][1][j][-1][k][0].text     (=VDLives[i][1][0][1][0][-1][k][0].text)
# Volume:            root[-1][i][1][0][1][j][-1][k][1].text     (=VDLives[i][1][0][1][0][-1][k][1].text)
# Speed:             root[-1][i][1][0][1][j][-1][k][2].text     (=VDLives[i][1][0][1][0][-1][k][2].text)



def download(VDID, date, hour, minute):
    vdlive = MOTCLiveData(date, hour, minute, dataname="VD")
    vdlive.download()
    if vdlive.empty():
        return f"Cannot find VDLiveData: {vdlive.date}/VDLive_{vdlive.hour}{vdlive.minute}.xml"

def volume(VDID, date, hour, minute):
    volume = 0
    vdlive = MOTCLiveData(date, hour, minute, dataname="VD")
    vdlive.download()
    if vdlive.empty():
        return f"Cannot find VDLiveData: {vdlive.date}/VDLive_{vdlive.hour}{vdlive.minute}.xml"
    with gzip.open(vdlive.filename, "r") as xmlfile:
        try:
            tree = ET.parse(xmlfile)
            root = tree.getroot()
            VDLives = root[-1]
        
        except ET.ParseError:
            print(f"{vdlive.filename} is Empty!")
        
        else:
            for i in range(len(VDLives)):
                if VDID == VDLives[i][0].text:
                    if VDLives[i][2].text == "0":
                        Lane = VDLives[i][1][0][1]
                        for j in range(len(Lane)):
                            Vehicle = Lane[j][-1]
                            for k in range(len(Vehicle)):
                                volume += int(Vehicle[k][1].text)
                        xmlfile.close()
                        vdlive.delete()
                        return volume
                    
                    elif VDLives[i][2].text == "1":
                        xmlfile.close()
                        vdlive.delete()
                        return f"{VDID} 通訊異常!"
                    
                    elif VDLives[i][2].text == "2":
                        xmlfile.close()
                        vdlive.delete()
                        return f"{VDID} 停用或施工中!"
                    
                    elif VDLives[i][2].text == "3":
                        xmlfile.close()
                        vdlive.delete()
                        return f"{VDID} 設備故障!"
                        
def speed(VDID, date, hour, minute):
    volume = 0
    volumeXspeed = 0
    vdlive = MOTCLiveData(date, hour, minute, dataname="VD")
    vdlive.download()
    if vdlive.empty():
        return f"Cannot find VDLiveData: {vdlive.date}/VDLive_{vdlive.hour}{vdlive.minute}.xml"
    with gzip.open(vdlive.filename, "r") as xmlfile:
        try:
            tree = ET.parse(xmlfile)
            root = tree.getroot()
            VDLives = root[-1]
        
        except ET.ParseError:
            print(f"{vdlive.filename} is Empty!")
        
        else:
            for i in range(len(VDLives)):
                if VDID == VDLives[i][0].text:
                    if VDLives[i][2].text == "0":
                        Lane = VDLives[i][1][0][1]
                        for j in range(len(Lane)):
                            Vehicle = Lane[j][-1]
                            for k in range(len(Vehicle)):
                                volume += int(Vehicle[k][1].text)
                                volumeXspeed += int(Vehicle[k][1].text) * int(Vehicle[k][2].text)
                        xmlfile.close()
                        vdlive.delete()
                        return volumeXspeed / volume
                    
                    elif VDLives[i][2].text == "1":
                        xmlfile.close()
                        vdlive.delete()
                        return f"{VDID} 通訊異常!"
                    
                    elif VDLives[i][2].text == "2":
                        xmlfile.close()
                        vdlive.delete()
                        return f"{VDID} 停用或施工中!"
                    
                    elif VDLives[i][2].text == "3":
                        xmlfile.close()
                        vdlive.delete()
                        return f"{VDID} 設備故障!"
                        
def occupy(VDID, date, hour, minute):
    occupy = 0
    vdlive = MOTCLiveData(date, hour, minute, dataname="VD")
    vdlive.download()
    if vdlive.empty():
        return f"Cannot find VDLiveData: {vdlive.date}/VDLive_{vdlive.hour}{vdlive.minute}.xml"
    with gzip.open(vdlive.filename, "r") as xmlfile:
        try:
            tree = ET.parse(xmlfile)
            root = tree.getroot()
            VDLives = root[-1]
        
        except ET.ParseError:
            print(f"{vdlive.filename} is Empty!")
        
        else:
            for i in range(len(VDLives)):
                if VDID == VDLives[i][0].text:
                    if VDLives[i][2].text == "0":
                        Lane = VDLives[i][1][0][1]
                        for j in range(len(Lane)):
                            occupy += int(Lane[j][3].text)
                        xmlfile.close()
                        vdlive.delete()
                        return occupy / len(Lane)
                    
                    elif VDLives[i][2].text == "1":
                        xmlfile.close()
                        vdlive.delete()
                        return f"{VDID} 通訊異常!"
                    
                    elif VDLives[i][2].text == "2":
                        xmlfile.close()
                        vdlive.delete()
                        return f"{VDID} 停用或施工中!"
                    
                    elif VDLives[i][2].text == "3":
                        xmlfile.close()
                        vdlive.delete()
                        return f"{VDID} 設備故障!"
    
