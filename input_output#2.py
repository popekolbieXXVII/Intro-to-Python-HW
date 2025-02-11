# Ask for the number of slices each person eats
slices_person_1 = int(input("How many slices does person 1 eat? "))
slices_person_2 = int(input("How many slices does person 2 eat? "))
slices_person_3 = int(input("How many slices does person 3 eat? "))
slices_person_4 = int(input("How many slices does person 4 eat? "))
# Calculate the total number of slices needed
total_slices_needed = slices_person_1 + slices_person_2 + slices_person_3 + slices_person_4
# Calculate the number of whole pizzas needed
pizzas_needed = total_slices_needed / 8  # each pizza has 8 slices
leftover_slices = total_slices_needed % 8  # remaining slices
# Print the result
print("Number of whole pizzas needed:", pizzas_needed)
print("Number of leftover slices:", leftover_slices)
