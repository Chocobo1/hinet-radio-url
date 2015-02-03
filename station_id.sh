#!/bin/sh
# Chocobo1 (Mike Tzou), 2015

function hinetRadioStationId()
{
	local ECHO=/usr/bin/echo
	local GREP=/usr/bin/grep
	local SORT=/usr/bin/sort
	local WGET='/usr/bin/wget -q -t 3 -O -'

	local base_url='http://hichannel.hinet.net/radio/channelList.do?pN='

	local id_list
	local name_list
	local current_page=1
	local total_pages=2
	while [ $current_page -le $total_pages ]; do
		local data="$($WGET "$base_url$current_page")"

		if [ $current_page -eq 1 ]; then
			total_pages=( $( $ECHO $data | $GREP -Po '(?<=\"pageSize\":).+?(?=,)' ) )
		fi
		current_page=$((current_page + 1))

		local ORIG_IFS=$IFS
		IFS=$'\n'
		id_list+=( $( $ECHO $data | $GREP -Po '(?<=\"channel_id\":\").+?(?=\")' ) )
		name_list+=( $( $ECHO $data | $GREP -Po '(?<=\"channel_title\":\").+?(?=\")' ) )
		IFS=$ORIG_IFS
	done

	for i in "${!name_list[@]}"
	do
		$ECHO "${id_list[$i]} - ${name_list[$i]}"
	done | $SORT -n -k1
}

hinetRadioStationId
