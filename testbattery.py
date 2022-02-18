import os
from smbus import SMBus
import time

ManufacturerAccess          =0x00
RemainingCapacityAlarm      =0x01
RemainingTimeAlarm          =0x02
BatteryMode                 =0x03
AtRate                      =0x04
AtRateTimeToFull            =0x05
AtRateTimeToEmpty           =0x06
AtRateOK                    =0x07
Temperature                 =0x08
Voltage                     =0x09
Current                     =0x0a
AverageCurrent              =0x0b
MaxError                    =0x0c
RelativeStateOfCharge       =0x0d
AbsoluteStateOfCharge       =0x0e
RemainingCapacity           =0x0f
FullChargeCapacity          =0x10
RunTimeToEmpty              =0x11
AverageTimeToEmpty          =0x12
AverageTimeToFull           =0x13
ChargingCurrent             =0x14
ChargingVoltage             =0x15
BatteryStatus               =0x16
CycleCount                  =0x17
DesignCapacity              =0x18
DesignVoltage               =0x19
SpecificationInfo           =0x1a
ManufactureDate             =0x1b
SerialNumber                =0x1c
ManufacturerName            =0x20
DeviceName                  =0x21
DeviceChemistry             =0x22
ManufacturerData            =0x23
Unknown_38                  =0x38 # probably Cellvoltage4
Unknown_39                  =0x39 # probably CellVoltage3
Unknown_3a                  =0x3a # probably CellVoltage2
Unknown_3b                  =0x3b # probably CellVoltage1
CellVoltage4                =0x3c
CellVoltage3                =0x3d
CellVoltage2                =0x3e
CellVoltage1                =0x3f
SetROMAddress               =0x40 # word write only
PeekROMByte                 =0x42
PeekROMBlock                =0x43 # block read, size seems to be always =0x20 (32 bytes)
FETControl                  =0x46
SafetyAlert                 =0x50
SafetyStatus                =0x51
PFAlert                     =0x52
PFStatus                    =0x53
OperationStatus             =0x54
ChargingStatus              =0x55
ResetData                   =0x57
WDResetData                 =0x58
PackVoltage                 =0x5a
AverageVoltage              =0x5d
TS1Temperature              =0x5e
TS2Temperature              =0x5f
UnSealKey                   =0x60
FullAccessKey               =0x61
PFKey                       =0x62
AuthenKey3                  =0x63
AuthenKey2                  =0x64
AuthenKey1                  =0x65
AuthenKey0                  =0x66
SenseResistor               =0x71
TempRange                   =0x72
Timestamp                   =0x73
ManufacturerStatus          =0x74
DataFlashClass              =0x77
DataFlashClassSubClass1     =0x78
DataFlashClassSubClass2     =0x79
DataFlashClassSubClass3     =0x7a

i2c_port = 3
pin_SDA = 8
pin_SDC = 7

sb_address = 0x0b

os.system("raspi-gpio set 7 pu")
os.system("raspi-gpio set 8 pu")

bus=SMBus(i2c_port)
# b=bus.read_word_data(sb_address,CellVoltage3)
while(1):
    try:
        print("Tegangan Cell 1")
        print(bus.read_word_data(sb_address,CellVoltage1))
    except:
        pass
    try:
        print("Tegangan Cell 2")
        print(bus.read_word_data(sb_address,CellVoltage2))
    except:
        pass
    try:
        print("Tegangan Cell 3")
        print(bus.read_word_data(sb_address,CellVoltage3))
    except:
        pass
    try:
        print("SoC")
        print(bus.read_word_data(sb_address,RelativeStateOfCharge))
        print("Rem Cap")
        print(bus.read_word_data(sb_address,RemainingCapacity))
    except:
        pass
    time.sleep(1)
