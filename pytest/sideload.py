import subprocess
from adb_interaction import ADB
import adb_keyevents
import time


adb = ADB("evolve")
adb.adb_connect("10.100.15.158")

subprocess.call("adb connect 10.100.15.172")
subprocess.call("adb devices",shell=True)
subprocess.call("adb install -r WatchTV-debug.apk")






