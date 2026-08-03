source_id = 113
Model.AddStaticStructuralAnalysis()
static_structural = Model.Analyses[0]
bolt_pretension = static_structural.AddBoltPretension()

clr_type = bolt_pretension.GetType()
for member in clr_type.GetProperties():
    print(member.Name)