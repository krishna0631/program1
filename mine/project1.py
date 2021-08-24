import bitly_api 
BITLY_ACCESS_TOKEN ="YOUR_ACCESS_TOKEN"
access = bitly_api.Connection(access_token = BITLY_ACCESS_TOKEN)
full_link = input()
short_url = access.shorten(full_link) 
print('Short URL = ',short_url['url'])
