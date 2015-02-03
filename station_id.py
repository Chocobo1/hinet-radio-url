#!/bin/python2
"""
Chocobo1 (Mike Tzou), 2015
"""

import urllib , json , itertools

def hinet_radio_station_id():
	"""
	return a dictionary{ (int) station_id : (utf8 string) "station_name" }
	"""

	base_url = "http://hichannel.hinet.net/radio/channelList.do?pN="

	id = []
	name = []
	current_page = 1
	total_pages = 2
	while ( current_page <= total_pages ):
		base_url_data = urllib.urlopen( base_url + str( current_page ) )
		json_data = json.load( base_url_data , 'utf-8' )

		if ( current_page == 1 ):
			total_pages = json_data[ "pageSize" ]
		current_page += 1

		t = json_data[ "list" ]
		for i in xrange( 0 , len( t ) ):
			try:
				id.append( t[i][ "channel_id" ] )
				name.append( t[i][ "channel_title" ] )
			except ( KeyError ):
				pass

	id = map( int , id )

	return dict( itertools.izip_longest( id , name ) )


if __name__ == "__main__":
	id_list = hinet_radio_station_id()
	for i in sorted( id_list ):  # same as `sorted( id_list.keys() )`
		print "%d - %s" % ( i , id_list[ i ].encode( 'big5' ) )
