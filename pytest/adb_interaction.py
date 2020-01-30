import subprocess
import sys
import os
import platform
from adb_keyevents import adb_key_values
from environment import duts, accounts, adb_path
import re


class ADB(object):

    def __init__(self, dut):
        self.platform_name = str(platform.system())
        self.platform_name = self.platform_name.strip()
        print("Platform: " + self.platform_name)
        self.adb_path = adb_path
        self.dut = dut
        self.ip_address = self.find_live_ip(dut)
        print('IP Address: ' + self.ip_address)
        self.adb_connect(self.ip_address)



    def adb_connect(self, ip_address):
        # Establish connection to device using adb over ethernet.
        if (self.adb_devices(ip_address)):
            print("Device already connected")
            return True
        else:
            print(("Device connection check worked. Negative."))

        command = "connect " + ip_address

        output = self.raw_input_command(command)

        if "connected to {0}".format(ip_address) in output:
            print(("ADB connection established successfully"))
            return True
        else:
            print(("ADB connection failure"))
            return False

    def adb_devices(self, ip_adress, adb_port='5555'):
        command = "devices"

        output = self.raw_input_command(command)
        # print("Output: " + output)

        if "{0}:{1}".format(ip_adress, adb_port) in output:
            print(("ADB: device is already connected"))
            return True
        else:
            print(("ADB: device is not connected. Proceeding to connect."))
            return False

    def remote_command(self, key_event, repeat=1, fast_mode=True, adb_port='5555'):
        if key_event.upper() in adb_key_values:
            key_event = adb_key_values[key_event.upper()]
            # cmd_remote = "{0} -s {1}:{2} shell input keyevent {3}".format(self.adb_path, self.ip_address,
            #                                                               adb_port, key_event)
            command = "shell input keyevent " + str(key_event)
            if repeat <= 1:
                pass
            else:
                if fast_mode:
                    event_string = ""
                    for r in range(0, repeat - 1):
                        event_string = event_string + ' ' + str(key_event)
                        command = command + ' ' + event_string
                else:
                    pass
            print(command)

            try:
                if fast_mode == False:
                    for i in range(0, repeat):
                        status = self.raw_input_command(command, return_type='status')
                else:
                    status = self.raw_input_command(command, return_type='status')


            except:
                error = sys.exc_info()[0]
                exc_type, exc_obj, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                print('%s', error)
                print(exc_type, fname, exc_tb.tb_lineno)
                return False
            if status == 0:
                print(("ADB Remote Input successful"))
                return True
            elif status == 1:
                print(("ADB Remote Input failure"))
                return False
        return True

    def text_command(self, text_entry, adb_port='5555'):
        # cmd_text = "{0} -s {1}:{2} shell input text {3}".format(self.adb_path, self.ip_address, adb_port, text_entry)
        # print(cmd_text)

        command = "shell input text " + text_entry
        # print command
        try:
            # status = subprocess.call(cmd_text, shell=True)
            # print(status)
            status = self.raw_input_command(command, return_type='status')

        # except OSError, osErr:
        #     print('%s', osErr)
        #     return False
        except:
            error = sys.exc_info()[0]
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print('%s', error)
            print(exc_type, fname, exc_tb.tb_lineno)
            return False
        if status == 0:
            print("ADB Remote Input successful")
            return True
        elif status == 1:
            print("ADB Remote Input failure")
            return False
        return True

    def raw_input_command(self, text_entry, return_type='output', adb_port='5555'):
        command = "{0} -s {1}:{2} {3}".format(self.adb_path, self.ip_address, adb_port, text_entry)
        print(command)
        output = ""

        try:
            if sys.version_info[0] > 2:
                if return_type is 'status':
                    output = subprocess.getstatusoutput(command)
                else:
                    output = subprocess.getoutput(command)
            else:
                if return_type is 'status':
                    try:
                        output = subprocess.check_call(command, shell=True)
                    except Exception as e:
                        if 'dmesg' in command:
                            pass
                        else:
                            print(e)
                        output = 1
                else:
                    # print("Calling subprocess.check_output.")
                    output = subprocess.check_output(command, shell=True)
        except:
            error = sys.exc_info()[0]
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            if 'dmesg' in command:
                pass
            else:
                print('%s', error)
                print(exc_type, fname, exc_tb.tb_lineno)
                return 'Error'

        return output

    def find_live_ip(self, dut):

        live_ip = ""
        ping_flag = "-c 1 -t 1"
        if self.platform_name is "Windows":
            ping_flag = "-n 1 -w 1000"

        got_live = False


        command = "ping {0} {1}".format(ping_flag, duts[dut]["wired_ip_address"])
        # print(command)
        status = subprocess.call(command, shell=True)
        # print(status)
        if status == 0:
            live_ip = duts[dut]["wired_ip_address"]
            self.ip_address = live_ip
            return live_ip
        else:
            pass

            command = "ping {0} {1}".format(ping_flag, duts[dut]["wireless_ip_address"])
        status = subprocess.call(command, shell=True)
        if status == 0:
            live_ip = duts[dut]["wireless_ip_address"]
            self.ip_address = live_ip
            got_live = True
        else:
            pass

        return live_ip

    def get_firmware_version(self):
        command_base = 'shell getprop '
        command = command_base + 'ro.build.version.release'
        response = self.raw_input_command(command)

        # print('Response: ' + response)
        firmware_version = response.strip()

        command = command_base + 'ro.build.version.incremental'
        response = self.raw_input_command(command)

        # print('Response: ' + response)
        firmware_version = firmware_version + '-' + response.strip()

        return firmware_version

    def get_apk_version(self):
        packages = ['com.sling.airtvplayer',
                    'com.sling.dev']
        pattern = r"versionName=(.*)\s"

        command_base = 'shell dumpsys package '

        package_string = ''

        for package in packages:
            command = command_base + package
            # print('Command: ' + command)
            response = self.raw_input_command(command)
            # print('Response: ' + response)
            p = re.compile(pattern, re.MULTILINE)

            m = p.search(response)

            if m:
                # print("Found: " + m.group(1))
                package_string = package_string + package + '_' + m.group(1).strip()
            else:
                # print("No match"
                pass

        return package_string

    def get_packages(self):
        command = 'shell dumpsys package'
        response = self.raw_input_command(command)
        return response

    def get_boot_time(self):
        get_boot_time_command = 'shell cat /proc/stat'
        response = self.raw_input_command(get_boot_time_command)
        pattern = r"btime (\d+)"

        p = re.compile(pattern, re.MULTILINE)
        m = p.search(response)

        if m:
            # print("found: " + m.group(1))
            return m.group(1).strip()
        else:
            # print("No match")
            return "boot_time_not_found"
