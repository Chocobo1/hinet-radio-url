#!/bin/python2
"""
Chocobo1 (Mike Tzou), 2015
"""

import re , urllib2

def hinet_radio_stream_url( id ):
	"""
	returns a dict for radio station `id`
	dict fields:
		Id = Station's Id number
		Name = Station's name
		Program = Station's current program/show
		Url = Station's HLS stream URL

	input arguments:
	id = should be valid radio station ID
	"""

	base_url = "https://hichannel.hinet.net/radio/play.do?id=" + str( id )
	url0 = urllib2.Request( base_url )
	url0.add_header( "Referer" , base_url )
	url0 = urllib2.urlopen( url0 ).read()

	try:
		radio_url1 = re.search( "(?<=\"playRadio\":\").+?(?=\")" , url0 ).group()
	except AttributeError:
		raise IOError( "variable `id` invalid" )
	radio_url2 = urllib2.urlopen( radio_url1 ).read()
	radio_url2 = re.search( "^.+token1.+token2.+" , radio_url2 , re.MULTILINE ).group()
	radio_url2 = radio_url2.replace( "-video=0" , "" )
	radio_url3 = re.sub( "index.m3u8.*$" , "" , radio_url1 ) + radio_url2

	name = re.search( "(?<=\"channel_title\":\").+?(?=\")" , url0 ).group().decode( 'utf-8' )
	program = re.search( "(?<=\"programName\":\").+?(?=\")" , url0 ).group().decode( 'utf-8' )

	return { 'Id' : id , 'Name' : name , 'Program' : program , 'Url' : radio_url3 }


import sys
if __name__ == "__main__":
	id = sys.argv[1:]
	if not id:
		id = [228]

	for i in id:
		try:
			l = hinet_radio_stream_url( i )
			print ( "\nID: %s" ) % l['Id']
			print ( "Name: %s" ) % l['Name'].encode( 'big5' )
			print ( "Program: %s" ) % l['Program'].encode( 'big5' )
			print ( "\nURL: %s" ) % l['Url']
		except IOError:
			pass
