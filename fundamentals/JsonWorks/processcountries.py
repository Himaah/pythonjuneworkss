from json import load
f=open("C:\\Users\\user\\Desktop\\PythonJuneWorks\\fundamentals\\JsonWorks\\countries.json",encoding= "UTF-8")

countries=load(f)
# print (countries)

# 1. number  of data
# print(len(countries))

#2. find the largest populated country
def largest_populated(dic):

    return dic.get("population")

largest_population=max(countries,key=largest_populated)
# print(largest_population)

#3. find country with minimum population

def smallest_population(dic):

    return dic.get("population")

smallest_population_country=min(countries,key=largest_populated)
# print(smallest_population_country)


#4. if the country is independent or not

countryisIndependent=[i.get("name") for i in countries if i.get("independent")==True]
# print(len(countryisIndependent))


#5. subregion=western asia

subregion=[i.get("name") for i in countries if i.get("subregion")=="Western Asia"]
# print(subregion)



#6. not in euro and currency euro

# NotInEuro=[ for i in countries if i.get("currency")]

def is_euro(c):
    if c.get("currencies") != None:
        for curr in c.get("currencies"):
            return curr.get("code") == "EUR" 

country_currency_filter = [c.get("name") for c in countries if is_euro(c) and c.get("region") != "Europe"]
# print(country_currency_filter)
# print(country_currency_filter)

#7. find the country with smallest area

def smallest_area(dic):
    area = dic.get("area")
    if area is None or not isinstance(area, (float, int)):
        return float('inf') 
    return area

smallest_area_country = min(countries, key=smallest_area)

# print(smallest_area_country)

#8. find all the countries where the official language is arabic





#Which countries have alternate spellings that include the word 'Republic'?

def is_altSpelling(c):
    if c.get("altSpellings") is not None:
        for w in c.get("altSpellings"):
            if "Republic" in w:
                return True

countries_altSpelling = [c.get("name") for c in countries if is_altSpelling(c)]
# print(countries_altSpelling)


# 10. List all countries with a population less than 1 million.

countries_population_filter = [c.get("name") for c in countries if c.get("population") < 1000000]
# print(countries_population_filter)


#11. Find countries where the capital city's name is the same as the country's name.

countries_capital_filter = [c.get("name") for c in countries if c.get("capital") == c.get("name")]
# print(countries_capital_filter)

# 12. List all countries with a capital that starts with the letter 'A'.

country_capitalA = [c.get("name") for c in countries if c.get("capital") is not None and c.get("capital").startswith("A")]
# print(country_capitalA)


#13. other names

def fetch_country_name(name):


    return [c for c in countries if c.get("name")==name][0]   #list of dict maaraan

country_filter=fetch_country_name("India")

# print(country_filter)


# if "regionalBlocs" in country_filter:
#     block_data=country_filter.get("regionalBlocs")[0]

#     if "otherNames" in block_data:
#         # print(block_data.get("otherNames"))
#     else:
        # print(country_filter.get("name"))


#14. highest area

def get_area(dict):
    if "area" in dict:
        return dict.get("area")
    else:
        return 0
    
largest_area=max(countries,key=get_area)
# print(largest_area.get("name"))

#15. lang=eng


# for c in countries:
#     for l in c.get("languages"):
#         if l.get("name")=="English":
            # print(c.get("name"))

# 16.largest region

all_regions={c.get("region") for c in countries}        #no duplicates so set
print(all_regions)

# region: key,value:sum of area

region_summary={}
for c in countries:

    region_name=c.get("region")
    
    if region_name in region_summary:
        region_summary[region_name]+=c.get("area",0)
    else:
         region_summary[region_name]=c.get("area",0)

# print(region_summary)

key_values=[(v,k)for k,v in region_summary.items()]
print(max(key_values))






















