#!/bin/sh
# Copyright (C) 2014  Mike Tzou
# This script is licensed under GPLv3 (http://www.gnu.org/licenses/gpl-3.0.html)

function hinetRadioStreamUrl()
{
	# $1=(input)station ID, $2=(ouput)variable for returning the result URL

	local SED=/usr/bin/sed
	local ECHO=/usr/bin/echo
	local GREP=/usr/bin/grep
	local WGET='/usr/bin/wget -q -t 3 -O -'
	
	local base_url="http://hichannel.hinet.net/radio/index.do?id=$1"
	local url1="$( $WGET "$base_url" | $GREP -Po "(?<=').+token1.+token2.+?(?=')" | $SED 's/\\//g')"

	local url2=''
	while [ -z $url2 ]; do
		url2="$( $WGET "$url1" | $GREP -Po "^.+token1.+token2.+" | $SED 's/-video=0//g' )"
	done

	local url3="$( $ECHO "$url1" | $SED 's/index.m3u8.*$//g')$url2"
	eval $2=\$url3
}

# example
station_id='228'
stream_url=''
hinetRadioStreamUrl $station_id stream_url

# output
ECHO=/usr/bin/echo
$ECHO
$ECHO "Station ID: $station_id"
$ECHO
$ECHO "Stream URL: $stream_url"
