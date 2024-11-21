from data import CountyDemographics

#Part 1
def population_total(population: list[CountyDemographics])->int:
    total_population = 0
    for county in population:
        if '2014 Population' in county.population:
            total_population += county.population['2014 Population']

    return total_population
#The purpose of this function is to take in a list of the counties of type CountyDemographics and return the total population is 2014 for all the counties.

#Part 2
def filter_by_state(all_counties: list[CountyDemographics], state: str) -> list[CountyDemographics]:
    return [county for county in all_counties if county.state == state]
#The purpose of this function is to take in a list of the counties of type CountyDemographics along with a selected state (type string) and return only all the objects that match the state.


#Part 3
def population_by_education(counties: list[CountyDemographics], education: str) -> float:
    population = 0.0

    for county in counties:
        if education in county.education:
            percentage = county.education[education]
            population += county.population['2014 Population'] * (percentage / 100)
    return population
#The purpose of this function is to take in a list of the counties of type CountyDemographics along with an education level of type string (key) and return the total 2014 subpopulation across the set of counties that matches the key.

def population_by_ethnicity(counties:list[CountyDemographics], ethnicity_key: str) -> int:
    population = 0
    for county in counties:
        ethnicity = county.ethnicities
        if ethnicity_key in ethnicity:
            population += ethnicity[ethnicity_key]

    return population
#The purpose of this function is to take in a list of the counties of type CountyDemographics along with an ethnicity of choice (type str) and only output the total 2014 subpopulation across the set of counties that matches the key/ethnicity.

def population_below_poverty_level(counties: list[CountyDemographics]) -> float:
    below_poverty = 0.0

    for county in counties:
        poverty_percentage = county.income.get('Persons Below Poverty Level', 0)
        county_population = county.population.get('2014 Population', 0)
        below_poverty += county_population * (poverty_percentage / 100)

    return below_poverty
#The purpose of this function is to take in a list of the counties of type CountyDemographics and return the number of people below the poverty level.

#Part 4
def percent_by_education(counties: list[CountyDemographics], education: str) -> float:
    population = 0
    for county in counties:
        population += county.population['2014 Population']
    education_population = population_by_education(counties, education)
    return (education_population/population) * 100


#The purpose of this function is to take in a list of the counties of type CountyDemographics along with a level of education of type string and return a float percentage value of 2014 subpopulation with that level of education.

def percent_by_ethnicity(counties: list[CountyDemographics], ethnicity: str) -> float:
    population = 0
    ethnicity_population = 0

    for county in counties:
        if ethnicity in county.ethnicities:
            population += county.population['2014 Population']
            ethnicity_population += county.ethnicities[ethnicity] * county.population['2014 Population'] / 100

    if population == 0:
        return 0

    return (ethnicity_population/population) * 100
#The purpose of this function is to take in a list of the counties of type CountyDemographics along with an ethnicity of type string and return a float percentage value of 2014 subpopulation with that ethnicity.

def percent_below_poverty_level(counties: list[CountyDemographics]) -> float:
    population = 0.0
    below_poverty = population_below_poverty_level(counties)

    for county in counties:
       population += county.population['2014 Population']

    if population > 0:
        return below_poverty/population * 100
    else:
        return 0.0
#The purpose of this function is to take in a list of the counties of type CountyDemographics and return a float percentage value of 2014 subpopulation under the poverty level.

#Part 5
def education_greater_than(counties: list[CountyDemographics], education_key: str, threshold: float) -> list[CountyDemographics]:
    result = []

    for county in counties:
        education_value = county.education.get(education_key, 0)
        if education_value > threshold:
            result.append(county)
    return result
#The purpose of this function is to take in a list of the counties of type CountyDemographics, an education level which is a key of type string, and a threshold of type float. If the education level for each object is above the threshold it will be returned as a list object.

def education_less_than(counties: list[CountyDemographics], education_key: str, threshold: float) -> list[CountyDemographics]:
    result = []

    for county in counties:
        education_value = county.education.get(education_key, 0)
        if education_value < threshold:
            result.append(county)
    return result
#The purpose of this function is to take in a list of the counties of type CountyDemographics, an education level which is a key of type string, and a threshold of type float. If the education level for each object is below the threshold it will be returned as a list object.


def ethnicity_greater_than(counties: list[CountyDemographics], ethnicity_key: str, threshold: float) -> list[CountyDemographics]:
    result = []

    for county in counties:
        ethnicity_value = county.ethnicities.get(ethnicity_key, 0)
        if ethnicity_value > threshold:
            result.append(county)
    return result
#The purpose of this function is to take in a list of the counties of type CountyDemographics, an ethnicity which is a key of type string, and a threshold of type float. If the percent of the population with that ethnicity for each object is greater than the threshold it will be returned as a list object.


def ethnicity_less_than(counties: list[CountyDemographics], ethnicity_key: str, threshold: float) -> list[CountyDemographics]:
    result = []

    for county in counties:
        ethnicity = county.ethnicities.get(ethnicity_key, 0)
        if ethnicity < threshold:
            result.append(county)
    return result
#The purpose of this function is to take in a list of the counties of type CountyDemographics, an ethnicity which is a key of type string, and a threshold of type float. If the percent of the population with that ethnicity for each object is less than the threshold it will be returned as a list object.

def below_poverty_level_greater_than(counties: list[CountyDemographics], threshold: float) -> list[CountyDemographics]:
    result = []
    for county in counties:
        poverty = county.income.get('Persons Below Poverty Level', 0)
        if poverty > threshold:
            result.append(county)

    return result
#The purpose of this function is to take in a list of the counties of type CountyDemographics and a threshold of type float. If the percent of the population below the poverty level for the object is greater than the threshold it will be returned as a list object.

def below_poverty_level_less_than(counties: list[CountyDemographics], threshold: float) -> list[CountyDemographics]:
    result = []
    for county in counties:
        poverty = county.income.get('Persons Below Poverty Level', 0)
        if poverty < threshold:
            result.append(county)

    return result
#The purpose of this function is to take in a list of the counties of type CountyDemographics and a threshold of type float. If the percent of the population below the poverty level for the object is less than the threshold it will be returned as a list object.