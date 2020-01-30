#adb_path = '/Users/alisa.fender/Android/platform-tools/adb'
log_path = '/Users/alisa.fender/logcat/autolog/'
adb_path = "adb"
#log_path = 'C:\\Users\\alisa\\logcat\\autolog\\'

duts = {'mp1a': {
    'account': '16',
    'wired_ip_address': 'mp1ah',
    'wireless_ip_address': 'mp1a',
    'device_serial_number': 'AREYDC00661K',
    'android_serial_number': '40105430000015B',
    'ota_feed': 'Rooftop Antenna',
    'ota_dongle': 'Hauppauge Inner Port',
    'environment': 'prod',
    'usb_hub': 'None',
    'external_storage': 'Seagate 500GB',
    'google_account': 'alisa.fender',
    },
    'mp2': {
    'account': '16',
    'wired_ip_address': 'mp2h',
    'wireless_ip_address': 'mp2',
    'device_serial_number': 'AREYDC02023L',
    'android_serial_number': '4010454300000B0',
    'ota_feed': 'Rooftop Antenna',
    'ota_dongle': 'Lark Inner Port',
    'environment': 'prod',
    'usb_hub': 'None',
    'external_storage': 'Seagate 1TB',
    'google_account': 'afqa001nopsu',
    },
    'mp4': {
    'account': '16',
    'wired_ip_address': 'mp4h',
    'wireless_ip_address': 'mp4',
    'device_serial_number': 'AREYDC02729L',
    'android_serial_number': '4010454300000816',
    'ota_feed': 'Rooftop Antenna',
    'ota_dongle': 'Hauppauge Inner Port',
    'environment': 'prod',
    'usb_hub': 'none',
    'external_storage': 'Seagate 500GB',
    'google_account': 'afqa001nopsu',
    },
    'mp5v': {
    'account': '16',
    'wired_ip_address': 'mp5vh',
    'wireless_ip_address': 'mp5v',
    'device_serial_number': 'AREYDC15940L',
    'android_serial_number': '40104543000003C7B',
    'ota_feed': 'Rooftop Antenna',
    'ota_dongle': 'Lark Inner Port',
    'environment': 'prod',
    'usb_hub': 'none',
    'external_storage': 'WD My Passport 1TB Red',
    'google_account': 'alisa.fender',
    },
    'mp5v_home': {
        'account': '16',
        'wired_ip_address': '192.168.86.300',
        'wireless_ip_address': '192.168.86.30',
        'device_serial_number': 'AREYDC15940L',
        'android_serial_number': '40104543000003C7B',
        'ota_feed': 'Window Antenna San Jose',
        'ota_dongle': 'Lark Inner Port',
        'environment': 'prod',
        'usb_hub': 'none',
        'external_storage': 'Toshiba 1TB',
        'google_account': 'afqa001nopsu',
    },
    'lab1': {
    'account': '16',
    'wired_ip_address': 'lab1',
    'wireless_ip_address': '192.168.1.333',
    'device_serial_number': '',
    'android_serial_number': '',
    'ota_feed': '',
    'ota_dongle': '',
    'environment': 'prod',
    'usb_hub': 'none',
    'external_storage': '',
    'google_account': '',
    },
    'home': {
    'account': '16',
    'wired_ip_address': '192.168.1.222',
    'wireless_ip_address': 'mphome',
    'device_serial_number': 'AREYDC07023L',
    'android_serial_number': '40104543000014A3',
    'ota_feed': 'Wineguard Antenna',
    'ota_dongle': 'Hauppauge',
    'environment': 'prod',
    'usb_hub': 'none',
    'external_storage': 'WD EasyStore 1TB',
    'google_account': 'afqa001nopsu',
    },
    'homefc': {
        'account': '16',
        'wired_ip_address': '192.168.1.333',
        'wireless_ip_address': '192.168.1.170',
        'device_serial_number': 'AREYDC07023L',
        'android_serial_number': '40104543000014A3',
        'ota_feed': 'none',
        'ota_dongle': 'none',
        'environment': 'prod',
        'usb_hub': 'none',
        'external_storage': 'none',
        'google_account': 'afqa001nopsu',
    },

    'd1': {
        'account': '16',
        'wired_ip_address': '192.168.1.300',
        'wireless_ip_address': '192.168.1.35',
        'device_serial_number': 'SEI1030000000000056',
        'android_serial_number': '',
        'ota_feed': 'SlingTV',
        'ota_dongle': 'NA',
        'environment': 'prod',
        'usb_hub': 'NA',
        'external_storage': 'SlingTV',
        'google_account': 'afqa001nopsu@gmail.com',
    },
'minigt': {
        'account': '16',
        'wired_ip_address': '192.168.1.300',
        'wireless_ip_address': 'minigt',
        'device_serial_number': 'GZ18090154700124',
        'android_serial_number': '',
        'ota_feed': 'SlingTV',
        'ota_dongle': 'NA',
        'environment': 'prod',
        'usb_hub': 'NA',
        'external_storage': 'SlingTV',
        'google_account': 'gtslinger30@gmail.com',
    },
    'minih': {
        'account': '16',
        'wired_ip_address': '192.168.1.300',
        'wireless_ip_address': '192.168.86.55',
        'device_serial_number': 'SEI1030000000000056',
        'android_serial_number': '',
        'ota_feed': 'ATC',
        'ota_dongle': 'NA',
        'environment': 'prod',
        'usb_hub': 'NA',
        'external_storage': 'NA',
        'google_account': 'afqa001nopsu@gmail.com',
    },
    'evolve': {
    'account': '16',
#    'wired_ip_address': '10.0.0.105',
    'wired_ip_address': '192.168.1.36',
    'wireless_ip_address': 'mphome',
    'device_serial_number': 'AREYDC07023L',
    'android_serial_number': '40104543000014A3',
    'ota_feed': 'Wineguard Antenna',
    'ota_dongle': 'Hauppauge',
    'environment': 'prod',
    'usb_hub': 'none',
    'external_storage': 'WD EasyStore 1TB',
    'google_account': 'afqa001nopsu',
    },

}

accounts = {
    '10': {
        'user': 'boomerang10@sling.com',
        'password': 'Watchm3',
    },
    '16': {
        'user': 'boomerang16@sling.com',
        'password': 'Watchm3',
    },
    'beta3': {
        'user': 'fcqaboom+3@gmail.com',
        'password': 'sling1234'
    },

}
