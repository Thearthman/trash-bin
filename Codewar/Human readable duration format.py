def format_duration(input):
    output = ""
    minutes = round(input / 60)
    hours = round(minutes / 60)
    days = round(hours / 24)
    years = round(days / 365)
    seconds = input
    timeList = [years, days, hours, minutes, seconds]
    processedList = [0, 0, 0, 0, 0]
    nameList = [" years ", " days ", " hours ", " minutes ", " seconds "]
    #              0     ,    1    ,     2    ,      3     ,      4

    # cases where only one unit is required
    breakpoint()
    for i in range(1,5): processedList[i] = timeList[i] - timeList[i - 1] * 60
    position = [index for index, value in enumerate(processedList) if value > 0]
    for value in position: output += str(processedList[value]); output += nameList[value]

    return processedList


print(format_duration(890))

# test.assert_equal(format_duration(3662), "1 hour, 1 minute and 2 seconds")
