# Program #3: US_Population
def main():
    # Have the user input (using a loop) various information that contains three pieces of data: 
    # year, name of state, and population.  
    # Store all of this information in a list of lists.  For example it might be stored like this:
    # [[2010, "Maine", 1987435], [2010,"Minnesota",6873202], [2011, "Iowa", 3421988]]
    limiter=0
    all_entered_values = []
    for x in range(3):
        year=int(input("Year:"))
        state=(input("State Name:"))
        population=int(input("State Population:"))
        data=[year,state,population]
        all_entered_values.append(data)

    # Now have the user enter a year. 
    year_to_sum = int(input("Select Year:"))
    sum_population_for_year(all_entered_values, year_to_sum)

    # The program will add the populations from all states in the list of list for that year only.
    # Pass the list and year to the sum_population_for_year

def sum_population_for_year(all_entered_values, year_to_sum):
    # Loop through and sum the populations for the appropriate year. 
    # e.g. for the list on line 7 the total would be 8,860,637 if the user enterd 2010 for the year to sum,
    # or 3,421,988 if they enterd 2011 for the year to sum.
    final=0
    for i in range(0, len(all_entered_values)):
        if all_entered_values[i][0] == year_to_sum:
            final=all_entered_values[i][2]+final
    print(final)

main()
# Call the main function.
#if __name__ == '__main__':
#    main()
