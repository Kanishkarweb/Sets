it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

print(len(it_companies)) # length of it companies
it_companies.add('Twitter') # add Twitter to it companies
print (it_companies)

multiple_it_companies = {'TCS', 'Infosys', 'Wipro', 'HCL', 'Accenture'}
it_companies.update(multiple_it_companies) # add multiple companies
print(it_companies)

it_companies.remove('IBM') # remove IBM from it companies
print (it_companies)