#staff={"A":34 , "B":45 ,"C":56 , "D": 43 }
#print sum of ages and average age

staff = {"A": 34, "B": 45, "C": 56, "D": 43}
sum_of_ages = sum(staff.values())
average_age = sum_of_ages / len(staff)
 
print("Sum of ages:", sum_of_ages)
print("Average age:", average_age)