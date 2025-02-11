# Ask for the number of slices each person eats
slices_per_person = int(input("How many slices does each family member eat? "))
# Calculate the total number of slices needed
total_slices_needed = slices_per_person * 4 # number of family members is 4
# Calculate the number of whole pizzas needed
pizzas_needed = total_slices_needed / 8 # pizzas have 8 slices each
leftover_slices = total_slices_needed % 8 # slices remaining
# print the result
print("Number of whole pizzas needed:", pizzas_needed)
print("Number of leftover slices:", leftover_slices)
