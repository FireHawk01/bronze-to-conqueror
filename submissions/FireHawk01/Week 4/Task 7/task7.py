import shodan
import sys
api_key = 'ut1TMbKqsM5zK6lNMas42aGvN25FM0Wv'
FACETS = [('org',3),('country',3)]
facet_titles = {'org':'Top 3 Organizations','country' : 'Top 3 Countries'}
print ('Enter the query')
query=input()
api= shodan.Shodan(api_key)
result = api.count(query, facets=FACETS)
for facet in result['facets']:
    print (facet_titles[facet])

    for term in result['facets'][facet]:
        print ('%s: %s' %(term['value'],term['count']))
        print ('')
