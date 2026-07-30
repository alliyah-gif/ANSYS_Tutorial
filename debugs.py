## Inspect Geometry Keys
geo = Model.Geometry
part = geo.Children[0].Children[0]
for prop in dir(part):
    if "id" in prop.lower():
        print(prop)