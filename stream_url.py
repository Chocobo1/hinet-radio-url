#!/bin/python2
"""
Chocobo1 (Mike Tzou), 2015
"""

import re , urllib

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

	url0 = "http://hichannel.hinet.net/radio/index.do?id=" + str( id )
	url0 = urllib.urlopen( url0 ).read()

	try:
		url1 = re.search( "(?<=').+token1.+token2.+?(?=')" , url0 ).group()
	except AttributeError:
		raise IOError( "variable `id` invalid" )
	url1 = url1.replace( "\\" , "" )
	url2 = urllib.urlopen( url1 ).read()
	url2 = re.search( "^.+token1.+token2.+" , url2 , re.MULTILINE ).group()
	url2 = url2.replace( "-video=0" , "" )
	url3 = re.sub( "index.m3u8.*$" , "" , url1 ) + url2

	name = re.search( "(?<=\"name\">).+?(?=<)" , url0 ).group().decode( 'utf-8' )

	program = re.search( "(?<=programArea\">).+?(?=<)" , url0 ).group().decode( 'utf-8' )

	return { 'Id' : id , 'Name' : name , 'Program' : program , 'Url' : url3 }


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
