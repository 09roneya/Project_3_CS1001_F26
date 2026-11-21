from data import CountyDemographics
#TASK 1 - input: counties output: total population of all counties purpose: adds upp the population of 2014 in each county
def population_total(counties: list[CountyDemographics]) -> int: 
    sum = 0
    for i in counties: 
        sum += i.population["2014 Population"]
    return sum
#TASK 2 input: list of counties, 2 letter state abbreviation to search for output:list of all counties from the state
def filter_by_state(counties: list[CountyDemographics], state: str) -> list[CountyDemographics]:
    result = []
    for i in counties: 
        if i.state == state: 
            result.append(i) 
    return result
#TASK 3A input: list of countries and education dictionary key output: estimated number of people in education catagory purpose: estiamte total population with specified education catagory
def population_by_education(counties: list[CountyDemographics], key: str) -> float:
    total = 0
    for i in counties: 
        if key in i.education:
            total+=((i.population["2014 Population"]*i.education[key])/100)
    return total
#TASK 3B input: list of counties and ethnciity key output: estimated number of people in ethnic group purpose: estimate total  population  in ethnic group
def population_by_ethnicity(counties: list[CountyDemographics], key: str) -> float:
    total = 0
    for i in counties: 
        if key in i.ethnicities:
            total+=((i.population["2014 Population"]*i.ethnicities[key])/100)
    return total
#TASK 3C input: list of counties  output: estimated number of people below poverty purpose: estimate total  population in below poverty level
def population_below_poverty_level(counties: list[CountyDemographics]) -> float:
    total = 0
    for i in counties: 
        if "Persons Below Poverty Level" in i.income:
            total+=((i.population["2014 Population"]*i.income["Persons Below Poverty Level"])/100)
    return total
#TASK 4A input: list of counties and education dictornary key output: education population percent purpose: calculates the total education percentage across counties
def percent_by_education(counties: list[CountyDemographics], key: str) -> float:
    populationpercounty= population_by_education(counties, key)
    totalpopulation = population_total(counties)
    if totalpopulation == 0: 
        return 0
    return 100 * (populationpercounty/totalpopulation)
#TASK 4B input: list of ocunties and ethnic dictionary key outuput: ethnic population percent purpose: calculates total ethicity percentage across counties
def percent_by_ethnicity(counties: list[CountyDemographics], key: str) -> float:
    populationpercounty=  population_by_ethnicity(counties, key)
    totalpopulation = population_total(counties)
    if totalpopulation == 0: 
        return 0
    return 100 * (populationpercounty/totalpopulation)
#TASK 4C input: list of counties output: below poverty level percentage purpose: calculates total percentage of those below poverty level across counties
def percent_below_poverty_level(counties: list[CountyDemographics]) -> float:
    populationpercounty= population_below_poverty_level(counties)
    totalpopulation = population_total(counties)
    if totalpopulation == 0: 
        return 0
    return 100 * (populationpercounty/totalpopulation)
#TASK 5A education thresholds input: list of counties, educaiton key and percent threshold output: list of counties iwth educaiton percent that is only greater than threshold purpose: find countries whose educaiton percent is above threshold
def education_greater_than(counties: list[CountyDemographics], key: str, threshold: float) -> list[CountyDemographics]:
    result = [] 
    for i in counties: 
        if key in i.education: 
            if i.education[key] > threshold:
                result.append(i)
    return result 
#input: list of counties, educaiton key and percent threshold output: list of counties iwth educaiton percent that is only less than threshold purpose: find countries whose educaiton percent is below threshold
def education_less_than(counties: list[CountyDemographics], key: str, threshold: float) -> list[CountyDemographics]:
    result = [] 
    for i in counties: 
        if key in i.education: 
            if i.education[key] < threshold:
                result.append(i)
    return result 
#TASK 5B ethnicity thresholds #input: list of counties, ethicity key and percent threshold output: list of counties with ethnicity percent that is only greater than threshold purpose: find countries whose ethnicity percent is above threshold

def ethnicity_greater_than(counties: list[CountyDemographics], key: str, threshold: float) -> list[CountyDemographics]:
    result = [] 
    for i in counties: 
        if key in i.ethnicities: 
            if i.ethnicities[key] > threshold:
                result.append(i)
    return result 
#input: list of counties, ethicity key and percent threshold output: list of counties with ethnicity percent that is only less than threshold purpose: find countries whose ethnicity percent is below threshold
def ethnicity_less_than(counties: list[CountyDemographics], key: str, threshold: float) -> list[CountyDemographics]:
    result = [] 
    for i in counties: 
        if key in i.ethnicities: 
            if i.ethnicities[key] < threshold:
                result.append(i)
    return result 
#TASK 5C income thresholds #input: list of counties and percent threshold output: list of counties with below income percent  percent that is only greater than threshold purpose: find countries whose poverty percent is greater threshold
def below_poverty_level_greater_than(counties: list[CountyDemographics], threshold: float) -> list[CountyDemographics]:
    result = [] 
    for i in counties: 
            if i.income["Persons Below Poverty Level"] > threshold:
                result.append(i)
    return result     
#input: list of counties and percent threshold output: list of counties with below income percent  that is only less than threshold purpose: find countries whose poverty percent is below threshold
def below_poverty_level_less_than(counties: list[CountyDemographics], threshold: float) -> list[CountyDemographics]:
    result = [] 
    for i in counties: 
            if i.income["Persons Below Poverty Level"] < threshold:
                result.append(i)
    return result     