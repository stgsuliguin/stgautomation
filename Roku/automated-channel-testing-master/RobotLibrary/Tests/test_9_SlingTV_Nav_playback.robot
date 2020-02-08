########################################################################
# Copyright 2019 Roku, Inc.
#
#Licensed under the Apache License, Version 2.0 (the "License");
#you may not use this file except in compliance with the License.
#You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
#Unless required by applicable law or agreed to in writing, software
#distributed under the License is distributed on an "AS IS" BASIS,
#WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#See the License for the specific language governing permissions and
#limitations under the License.
########################################################################
*** Settings ***
Documentation  Basic smoke tests
Library  ./../Library/RobotLibrary.py  ${ip_address}  ${timeout}  ${pressDelay}  ${server_path}
Library  Collections


*** Variables ***
${ip_address}  192.168.2.3
${server_path} C:\Users\SlingUserB\PycharmProjects\challenges\test1\Roku\automated-channel-testing-master\src\main.exe
${timeout}  50000
${pressDelay}  5000
${channel_code}  dev
&{DetailsData}=  using=tag  value=DetailsView
@{DetailsArray}=  &{DetailsData}
&{DetailsParam}=  elementData=@{DetailsArray}
@{KEYS}=  Select

** Test Cases ***

Verify is playback started
    Send key  Right
    Send key  Left
    Send key  Down
    Send key  Down
    Send Key  Down
    Send key  Select
    Send key  Select
    Send key  Select
    Verify is playback started

#Bookmarks

#    Sleep  12
#    Send key  Back
#    Sleep  5
#    Verify is screen loaded    ${DetailsParam}
#    Verify is playback started
#    &{player}=  Get player info
#    Run keyword if  ${player['Position']} < 10000  Fail



**Robot Library****

#@keyword("Verify is playback started")
#def verifyIsPlaybackStarted(self, retries = 10, delay = 1):
#    while retries > 0:
#        response = self._client.get_player_info()
#        res = json.loads(response.text)
#        if response.status_code != 200 or res['value']['State'] != 'play':
#            retries -= 1
#            sleep(delay)
#        else:
#            return True
#    raise Exception("Invalid player state")
