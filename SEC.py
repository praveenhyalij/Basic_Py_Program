#Program to find web site URL from page
page = ('<html>	<head> <title> Webpage	</title> </head> <body>	This is the simple web page. contains link for <a href="www.facebook.com"> facebook </a> </body> </html>')
print(page) #string to find/extract web url
start_link=(page.find('<a href'))   #find position of a herf tag
print(start_link)
start_quote=(page.find('"',start_link))    #find first " position
print(start_quote)
end_quote=(page.find('"',start_quote + 1))   #find end position of "
print(end_quote)
url=(page[start_quote+1:end_quote]) #get the URL from page
print(url)

