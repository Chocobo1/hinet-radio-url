#!/bin/sh
# Chocobo1 (Mike Tzou), 2015

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

	local base_url="https://hichannel.hinet.net/radio/play.do?id=$1"
	local url0="$( $WGET --header="Referer: $base_url" "$base_url" )"

	local radio_url1="$( $ECHO "$url0" | $GREP -Po "(?<=\"playRadio\":\").+?(?=\")" )"
	local radio_url2=''
	while [ -z $radio_url2 ]; do
		radio_url2="$( $WGET "$radio_url1" | $GREP -Po "^.+token1.+token2.+" | $SED 's/-video=0//g' )"
	done
	local radio_url3="$( $ECHO "$radio_url1" | $SED 's/index.m3u8.*$//g')$radio_url2"

	local name1="$( $ECHO "$url0" | $GREP -Po "(?<=\"channel_title\":\").+?(?=\")" )"

	local program1="$( $ECHO "$url0" | $GREP -Po "(?<=\"programName\":\").+?(?=\")" )"

	eval $2=\$name1
	eval $3=\$program1
	eval $4=\$radio_url3
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
