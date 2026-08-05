import materials

###Exercise 1
mat = ExtAPI.DataModel.Project.Model.Materials.Children[0]
matED = mat.GetEngineeringDataMaterial()
props = materials.GetListMaterialProperties(matED)
for p in props:
    print(p)
"""
Output:

Script Executed
Appearance
Coefficient of Thermal Expansion
Density
Elasticity
Tensile Yield Strength
Tensile Ultimate Strength
Thermal Conductivity
Specific Heat
Resistivity
Field Variable
"""

#Exercise 2: 
mats = ExtAPI.DataModel.Project.Model.Materials.Children
for m in mats:
    matED = m.GetEngineeringDataMaterial()
    print(m.Name,":", materials.GetMaterialPropertyByName(matED, "Tensile Yield Strength"))
