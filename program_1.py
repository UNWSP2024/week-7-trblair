# Program #1: Rainfall
# Design a program that lets the user enter the total rainfall for each of 12 months into a list.
# The program should calculate and display the total rainfall for the year, 
# the average monthly rainfall, # and the months with the highest and lowest amounts.


#I recognize that this solution is very clunky, but I couldn't figure out a way to name what month the rain came from besides this
def rainfallcalc():
    jan=float(input("How much rainfall was there in January?\n"))
    feb=float(input("How much rainfall was there in February?\n"))
    mar=float(input("How much rainfall was there in March?\n"))
    apr=float(input("How much rainfall was there in April?\n"))
    may=float(input("How much rainfall was there in May?\n"))
    june=float(input("How much rainfall was there in June?\n"))
    july=float(input("How much rainfall was there in July?\n"))
    aug=float(input("How much rainfall was there in August?\n"))
    sep=float(input("How much rainfall was there in September?\n"))
    octo=float(input("How much rainfall was there in October?\n"))
    nov=float(input("How much rainfall was there in November?\n"))
    dec=float(input("How much rainfall was there in December?\n"))
    rainfalllist=[jan,feb,mar,apr,may,june,july,aug,sep,octo,nov,dec]
    totalrainfall=sum(rainfalllist)
    avgrainfall=sum(rainfalllist)/len(rainfalllist)
    lowestrainfall=min(rainfalllist)
    if lowestrainfall == jan:
        lowestrainfall="January"
    elif lowestrainfall == feb:
        lowestrainfall="February"
    elif lowestrainfall == mar:
        lowestrainfall="March"
    elif lowestrainfall == apr:
        lowestrainfall="April"
    elif lowestrainfall == may:
        lowestrainfall="May"
    elif lowestrainfall == june:
        lowestrainfall="June"
    elif lowestrainfall == july:
        lowestrainfall="July"
    elif lowestrainfall == aug:
        lowestrainfall="August"
    elif lowestrainfall == sep:
        lowestrainfall="September"
    elif lowestrainfall == octo:
        lowestrainfall="October"
    elif lowestrainfall == nov:
        lowestrainfall="November"
    elif lowestrainfall == dec:
        lowestrainfall="December"
    highestrainfall=max(rainfalllist)
    if highestrainfall == jan:
        highestrainfall="January"
    elif highestrainfall == feb:
        highestrainfall="February"
    elif highestrainfall == mar:
        highestrainfall="March"
    elif highestrainfall == apr:
        highestrainfall="April"
    elif highestrainfall == may:
        highestrainfall="May"
    elif highestrainfall == june:
        highestrainfall="June"
    elif highestrainfall == july:
        highestrainfall="July"
    elif highestrainfall == aug:
        highestrainfall="August"
    elif highestrainfall == sep:
        highestrainfall="September"
    elif highestrainfall == octo:
        highestrainfall="October"
    elif highestrainfall == nov:
        highestrainfall="November"
    elif highestrainfall == dec:
        highestrainfall="December"
    print("Total rainfall:",totalrainfall,"\nAverage rainfall:",avgrainfall,"\nThe month with the lowest rainfall is",lowestrainfall,"\nThe month with the most rainfall is",highestrainfall)

rainfallcalc()
