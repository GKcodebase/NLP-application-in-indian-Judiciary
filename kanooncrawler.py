from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

filename = "judgements.csv"
f = open(filename, "w")
headers = "Title, Details, Doc_source\n"
f.write(headers)

# page numbers 0-9
for i in range(0,1):
	try:
		my_url = "https://indiankanoon.org/search/?formInput=Section%202%20in%20The%20Information%20Technology%20Act%2C%202000%20%20%20%20doctypes%3A%20judgments&pagenum=" + str(i)
		print ("\nurl opening up..")
		#opening up connection, grabbing the page
		uClient = uReq(my_url)
		print ("url loaded.")
		#offloads content to a variable
		page_html = uClient.read()
		#close the client
		uClient.close()
		#html parsing
		page_soup = soup(page_html, "html.parser")
		print ("html parsed.")
		#grabs each result
		rows = page_soup.find_all('div', {'class':'result'})

		for row in rows:
			title = row.div.a.text.strip()
			link = "https://indiankanoon.org" + row.div.a["href"]
			
			print ("\n" + title + " : url opening up..")
			newClient = uReq(link)
			print (title + " : url loaded.")
			details_html = newClient.read()
			newClient.close()
			details_soup = soup(details_html, "html.parser")
			print (title + " : html parsed.")
			detail_row = details_soup.find_all("div", {"class":"expanded_headline"})[0]
			
			detailbody = ""
			
			detail_row_fragments = detail_row.find_all("div", {"class":"fragment"})
			if (len(detail_row_fragments) > 0):
				for detail_row_fragment in detail_row_fragments:
					#multiple p's in fragment
					detail_frag_pbqs = detail_row_fragment.find_all("p")
					if (len(detail_frag_pbqs) > 0):
						for detail_frag_pbq in detail_frag_pbqs:
							if (isinstance(detail_frag_pbq, str)):
								detailbody += ""
							else: 
								# remove multiple whitespaces, tabs and newlines.
								detailbody += " ".join((detail_frag_pbq.text).split()) 
			
			detail_row_emptys = detail_row.find_all("div", {"class":""})
			if (len(detail_row_emptys) > 0):
				for detail_row_empty in detail_row_emptys:
					#multiple p's in empty
					detail_empty_pbqs = detail_row_empty.contents
					if (len(detail_empty_pbqs) > 0):
						for detail_empty_pbq in detail_empty_pbqs:
							if (isinstance(detail_empty_pbq, str)):
								detailbody += ""
							else:
								# remove multiple whitespaces, tabs and newlines.
								detailbody += " ".join((detail_empty_pbq.text).split())
			
			print ("\n" + detailbody + "\n---------------------------\n\n")
			
			print (detailbody.replace(",", "|") + "\n---------------------------\n\n")
			
			docsource = (row.find_all("div", {"class":"docsource"}))[0].text.strip()
	
			f.write(title.replace(",", "|") + "," + detailbody.replace(",", "|") + "," + docsource + "\n")
	
	except:
		break
		
f.close()
	
