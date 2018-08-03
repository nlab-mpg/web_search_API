import pprint

print("please type in your key word:")
kw = str(input())
print("please choose the search engine: 1.google 2.bing 3.flickr")
cho = str( input())


def google_search(search_term,api,cse_id,**kwargs):
	from googleapiclient.discovery import build
	service = build("customsearch","v1",developerKey=api)
	res = service.cse().list(q=search_term,cx=cse_id,**kwargs).execute()
	return res['items']

def flickr_search(kw,api_key,api_secret):
	import flickrapi
	flickr=flickrapi.FlickrAPI(api_key,api_secret,cache=True)
	try:
		photos=flickr.walk(text=kw,extras='url_c')
	except Exception as e:
		print('Error')
	return photos

def bing_search():
	print('not avalable currently')

def baidu_search(kw,api_key):
	import sys, urllib, urllib2, json
	url = 'http://apis.baidu.com/txapi/'+kw
	req = urllib2.Request(url)
	req.add_header("apikey", api_key)
	resp = urllib2.urlopen(req)
	content = resp.read()
	if(content):
	    print(content)

if cho == '1':	
	my_api_key = ""   #pls type in ur api
	my_cse_id = ""
	results = google_search(kw,my_api_key,my_cse_id,num=10)
	for result in results:
		pprint.pprint(result)
elif cho == '2':
	api_key = ''   #pls type in ur api
	api_secret = ''
	results = flickr_search(kw,api_key,api_secret)
	for photo in results:
		url=photo.get('url_c')
		print(str(url))
elif cho == '3':
	print(bing_search())
elif cho == '4'
	api_key = ''
	baidu_search(kw,api_key)
	
else:
	print('please input 1,2 or 3')
