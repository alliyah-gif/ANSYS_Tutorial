#SOURCE: https://discuss.ansys.com/discussion/35/can-you-provide-an-example-of-using-the-materials-module-in-mechanical

import materials

mats = ExtAPI.DataModel.Project.Model.Materials.Children

for mat in mats:
    print("="*30)
    print(mat.Name)
    print("="*30)
    matED = mat.GetEngineeringDataMaterial()
    print("="*30)
    listMatProp = materials.GetListMaterialProperties(matED)
    print(listMatProp)
    print("="*30)
    strength = materials.GetMaterialPropertyByName(matED, "Tensile Yield Strength")
    print(strength)
