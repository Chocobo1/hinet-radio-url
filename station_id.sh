#!/bin/sh
# Chocobo1 (Mike Tzou), 2015

function hinetRadioStationId()
{
	local ECHO=/usr/bin/echo
	local GREP=/usr/bin/grep
	local SORT=/usr/bin/sort
	local WGET='/usr/bin/wget -q -t 3 -O -'
	local base_url="http://hichannel.hinet.net/radio/index.do"

	local data="$($WGET "$base_url")"
	IFS=$'\n'
	local id_list=( $( $ECHO $data | $GREP -Po "(?<=onclick=\"indexUtil.setRadioDetail\(').+?(?=')" ) )
	local name_list=( $( $ECHO $data | $GREP -Po '(?<=\t\t\t\t\t\t\t\t\t\t<p>).+?(?=<)' ) )

	for i in "${!name_list[@]}"
	do
		$ECHO "${id_list[$i+1]} - ${name_list[$i]}"
	done | $SORT -n -k1
}

hinetRadioStationId
