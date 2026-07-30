import ansys.mechanical.core
from ansys.mechanical.core import App

#NOTE: Add mechanical app inside this python process, injects Model, DataModel, Tree etc.
app = App(globals = globals())
#BUG: Need and Ansys mechanical app to be running in order to use this API. If not, it will throw an error.
print(app)

#NOTE: Trivial analysis
Model.addStaticStructuralAnalysis()
ns = DataModel.Project.Model.AddNamedSelection()
ns.Name = "HelloWorld"

print("Named selections in project: ", [n.Name for n in DataModel.Project.Model.NamedSelections.Children])

"""STDOUT

"""