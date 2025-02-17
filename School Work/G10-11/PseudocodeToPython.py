# OUTPUT "Enter the grade"
print("Enter the grade")
1
# DECLARE points: REAL
# points <- 0.0
points = 0.0

# CASE OF grade
#   "A*" : points <- "100.0"
#   "A" : points <- "95.0"
#   "B" : points <- "85.0"
#   "C" : points <- "75.0"
#   "D" : points <- "65.0"
#   "E" : points <- "55.0"
#   OTHERWISE points <- 0.0
# ENDCASE
if grade == "A*":
    points = 100.0
elif grade == "A":
    points = 95.0
elif grade == "B":
    points = 85.0
elif grade == "C":
    points = 75.0
elif grade == "D":
    points = 65.0
elif grade == "E":
    points = 55.0
else:
    points = 0.0

# OUPUT points
print(points)
