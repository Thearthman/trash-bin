def lovesomeone(person, counts):
    output = " I love " + person + " "
    for i in range(counts):
        output = "♥" + output + "♥"
    print(output)
    return output


lovesomeone("you", 100)
