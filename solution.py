static_structural = Model.Analyses[0]
solution = static_structural.Solution

eq_stress = solution.AddEquivalentStress()
solution.Solve(True) #NOTE: this is a function not to be assigned to anything
total_deformation =  solution.Children[1]
print("Max deformation: ", total_deformation.Maximum)
print("Max equivalent stress: ", eq_stress.Maximum)
##Says there's an error but solution rendered correctly:
