#!/bin/sh
# Copyright (C) 2014  Mike Tzou
# This script is licensed under GPLv3 (http://www.gnu.org/licenses/gpl-3.0.html)

function hinet_radio_play_url()
{
	# $1=(input)station ID, $2=(ouput)variable for returning the result URL

	local SED=/usr/bin/sed
	local ECHO=/usr/bin/echo
	local GREP=/usr/bin/grep
	local WGET='/usr/bin/wget -q -t 3 -O -'

	local BASE_URL="http://hichannel.hinet.net/radio/mobile/index.do?id=$1"
	local URL1="$($WGET "$BASE_URL" | $GREP -Po "'\K.+token1.+token2.+?(?=')" | $SED 's/\\//g')"
	local URL2=''
	while [ -z $URL2 ]; do
		URL2="$($WGET "$URL1" | $GREP -Po "\K.+token1.+token2.+" | $SED 's/-video=0//g' )"
	done
	local URL3="$($ECHO "$URL1" | $SED 's/index.m3u8.*$//g')""$URL2"
	eval $2=\$URL3
}

# example
RADIO_ID='228'
URL=''
hinet_radio_play_url $RADIO_ID URL

# output
ECHO=/usr/bin/echo
$ECHO
$ECHO "Radio ID: $RADIO_ID"
$ECHO
$ECHO "URL: $URL"
