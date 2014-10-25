#!/bin/sh
# Copyright (C) 2014  Mike Tzou
# This script is licensed under GPLv3 (http://www.gnu.org/licenses/gpl-3.0.html)

# variables
RADIO_ID="228"
BASE_URL="http://hichannel.hinet.net/radio/mobile/index.do?id=$RADIO_ID"

SED=/usr/bin/sed
ECHO=/usr/bin/echo
GREP=/usr/bin/grep
WGET=/usr/bin/wget

URL1="$($WGET -q -t 3 -O - "$BASE_URL" | $GREP -Po "'\K.+token1.+token2.+?(?=')" | $SED 's/\\//g')"
URL2="$($WGET -q -t 3 -O - $URL1 | $GREP -Po "\K.+token1.+token2.+" | $SED 's/-video=0//g' )"
URL3="$($ECHO "$URL1" | $SED 's/index.m3u8.*$//g')"$URL2

$ECHO
$ECHO "Radio ID: $RADIO_ID"
$ECHO
$ECHO "URL: $URL3"
