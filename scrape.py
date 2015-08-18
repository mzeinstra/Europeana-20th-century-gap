import sys, requests, json, csv

key = "&wskey=<API KEY HERE>
api = "http://www.europeana.eu/api/v2/search.json?"

terms = ['proxy_dc_date','date']
types = ['IMAGE','TEXT']

#including year
from_year = 1700
#until but excluding
to_year = 2016 
 
def getResults(term, types, conditions):
	global errors
	global key
	global api
	query = 'query=TYPE:'+type
	for condition in conditions:
		query += '+OR+' + term + ':' + condition
	print (api + query + key)
	try:
		result = requests.get(api + query + key)
		result = result.json()
		total = int(result['totalResults'])
		return total
	except requests.ConnectionError:
		#connection error, try one more time
		try: 
			result = requests.get(api + query + key)
			result = result.json()
			total = int(result['totalResults'])
			return total
		except:
			errors.append([api + query + key, sys.exc_info()[0]])
			return 0
	except:
		errors.append([api + query + key, sys.exc_info()[0]])
		return 0

def getCount(term, type, year):
	'''
	just YYYY
	YYYY-DD-MM and YYYY-MM-DD, starts with YYYY-
	DD-MM-YYYY and MM-DD-YYYY, ends with -YYYY
	quotes "YYYY"
	brackets (YYYY)
	bracket date (YYYY-DD-MM) & (YYYY-MM-DD)
	accolades  [YYYY]
	accolades date [YYYY-MM-DD]
	dot .YYYY
	'''
	conditions = [year, year + "-*", "*-" + year,"\\\""+year+"\\\"" , "\\\""+year+"-*\\\"", "\\\"*-"+year+"\\\"", "("+year+")", "("+year+"-*)","(*-"+year+")","\["+year+"\]","\["+year+"-*\]","\[*-"+year+"\]", year + "."]
	return getResults(term, type, conditions)
	

#progress tracker
calls = len(types) * len(terms) * (to_year - from_year - 1)
callcounter = 0

# iterate over type, term, row
for type in types:
	results = []
	errors = []
	# set up header row
	row =[]
	row.append("year")
	for year in range(from_year,to_year):
		row.append(str(year))
	results.append(row)
	for term in terms:
		row = []
		row.append(term)
		query = 'query=' + term + ":*"
		result = requests.get(api + query + key)
		result = result.json()
		total = int(result['totalResults'])
		if total == 0:
			continue
		for year in range(from_year,to_year):
			year = str(year)
			print type, term, year + " (" + str(callcounter) + "/" + str(calls) + ")"
			callcounter += 1
			total = getCount(term, type, year)
			row.append(str(total))
			print total
		results.append(row)	

	# for each type create a new csv
	with open(type + ".csv", 'w') as fp:
		out = csv.writer(fp, 'excel-tab')
		for row in results:
		  out.writerow(row)
		out.writerow(errors)	