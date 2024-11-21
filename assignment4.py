import sys
import build_data

data_set = build_data.get_data()


def state_filter(counties: list, wanted_state: str):
    return [county for counties in data_set if county.state == wanted_state]

#check
def filter_greater_than(counties: list, field: str, cond: str, limit: float):
    result = []
    if field == "Ethnicity":
        for county in counties:
            for i in county.ethnicities:
                if cond in county.ethnicities:
                    ethnicity_value = county.ethnicities[i][1]
                    if ethnicity_value > limit:
                        result.append(county)

    elif field == "Income":
        for county in counties:
            if cond == county.income[1]:
                income_value = county.income[1][1]
                if income_value > limit:
                    result.append(county)

    elif field == "Education":
        for county in counties:
            for i in county.education:
                if cond in county.education:
                    education_value = county.education[i][1]
                    if education_value > limit:
                        result.append(county)

try:
    #open the file
    operation = sys.argv[1]
    with open(operation, 'r') as file:
        for line in file:
            line = str(line)
            action = line.strip()

   #extract the operations and parameters
    if ":" in action:
        task = action.split(":")
        function_needed = task[0]


        #displays the objects using __str__ in data.py
        if action == "display":
            for county in data_set:
                print(county)

        #filter by state
        if action == "filter-state":
            state = str(task[1])
            state_filter(data_set, state)

        #filter greater than -- check!!!
        if action == "filter-gt":
            if "." in task[1]:
                category = str(task[1].split('.')[0])
                condition = str(task[1].split('.')[1])
                if task[2]:
                    bounds = float(task[2])
                    filter_greater_than(data_set, category, condition, bounds)
                else:
                    bounds = 0
                    filter_greater_than(data_set, category, condition, bounds)


        if action == "filter-lt":
