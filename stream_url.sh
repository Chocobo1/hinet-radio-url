#!/bin/sh
# Copyright (C) 2014  Mike Tzou
# This script is licensed under GPLv3 (http://www.gnu.org/licenses/gpl-3.0.html)

function hinetRadioStreamUrl()
{
	# $1=(input)Station's ID number
	# $2=(ouput)Station's name
	# $3=(ouput)Station's current program/show
	# $4=(ouput)Station's HLS stream URL

	local SED=/usr/bin/sed
	local ECHO=/usr/bin/echo
	local GREP=/usr/bin/grep
	local WGET='/usr/bin/wget -q -t 3 -O -'
	
	local base_url="http://hichannel.hinet.net/radio/index.do?id=$1"
	local url0="$( $WGET "$base_url" )"
	local url1="$( $ECHO "$url0" | $GREP -Po "(?<=').+token1.+token2.+?(?=')" | $SED 's/\\//g')"
	local url2=''
	while [ -z $url2 ]; do
		url2="$( $WGET "$url1" | $GREP -Po "^.+token1.+token2.+" | $SED 's/-video=0//g' )"
	done
	local url3="$( $ECHO "$url1" | $SED 's/index.m3u8.*$//g')$url2"

	local name1="$( $ECHO "$url0" | $GREP -Po "(?<=\"name\">).+?(?=<)" )"

	local program1="$( $ECHO "$url0" | $GREP -Po "(?<=programArea\">).+?(?=<)" )"

	eval $2=\$name1
	eval $3=\$program1
	eval $4=\$url3
}

# example
id='228'
name=''
program=''
url=''
hinetRadioStreamUrl $id name program url

# output
ECHO=/usr/bin/echo
$ECHO
$ECHO "Station ID: $id"
$ECHO "Station Name: $name"
$ECHO "Station Program: $program"
$ECHO
$ECHO "Stream URL: $url"
