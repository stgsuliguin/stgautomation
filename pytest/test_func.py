import pytest
import subprocess
from adb_interaction import ADB
import adb_keyevents
import time

#@pytest.mark.gui_test()
@pytest.mark.gui_test()
#def test_gui():

def test_func():

    adb = ADB("evolve")
#   adb.adb_connect("10.100.15.172") # Update Environment.py 'evolve'
    #adb.remote_command("RIGHT", 3, False)

    ############# Navigation_Grid_Back (Start Left) ###################################################
    adb.remote_command("LEFT")
    adb.remote_command("LEFT")
    adb.remote_command("RIGHT", 2, False)
    adb.remote_command("DOWN")
#    time.sleep(30)
    adb.remote_command("DOWN")
    adb.remote_command("DOWN")
    adb.remote_command("DOWN")
    adb.remote_command("DOWN")
#    adb.remote_command("DOWN")


    ############# Navigation_Grid_Menu  ###########################################
    time.sleep(10)
    adb.remote_command("ENTER")
#   adb.remote_command("UP", 3, False)
    adb.remote_command("ENTER")
    time.sleep(10)
#    adb.remote_command("1")
#    adb.remote_command("3")
#    time.sleep(30)
    adb.remote_command("BACK")
    adb.remote_command("BACK")
    adb.remote_command("BACK")
    adb.remote_command("UP", 30, False)
    adb.remote_command("LEFT", 5, False)
#    adb.remote_command("LEFT")
    ################################################################################

#for i in range(1):
#    test_func()


count = 0

for i in range(2):
    count +=1
    print ("Number of iterations executed: ", count)
    test_func()

    print ("GUI Test")
    pass

@pytest.mark.api_test()
def test_api():
    print ("API Test")
    pass
