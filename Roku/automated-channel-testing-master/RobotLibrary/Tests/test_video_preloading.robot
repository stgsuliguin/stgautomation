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
Documentation  Test 2
Library  ./../Library/RobotLibrary.py  ${ip_address}  ${timeout}  ${pressDelay}  ${server_path}
Library  Collections


*** Variables ***
${ip_address}  192.168.1.94
${server_path}  D:/projects/go/webDriver/src/main.exe
${timeout}  20000
${pressDelay}  3000
${channel_code}  dev
&{GridData}=  using=tag  value=GridView
@{GridArray}=  &{GridData}
&{GridParams}=  elementData=${GridArray}
&{DetailsData}=  using=tag  value=DetailsView
@{DetailsArray}=  &{DetailsData}
&{DetailsParams}=  elementData=${DetailsArray}
&{EncardData}=  using=text  value=Play again
@{EncardArray}=  &{EncardData}
&{EncardParams}=  elementData=${EncardArray}

*** Test Cases ***
Verify is channel launched
    Launch the channel  ${channel_code}
    Verify is channel loaded    ${channel_code}    

Verify is initial screen loaded
    Verify is screen loaded    ${GridParams}

Verify is details screen loaded
    Send key  Select  4
    Verify is screen loaded    ${DetailsParams}

Verify is playback started
    Send key  Select  4
    Verify is playback started

Verify endcard after first video
    Verify is screen loaded    ${EncardParams}  8  10

Verify is playback started after 10 seconds
    Verify is playback started  3  5
