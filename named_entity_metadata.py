static_structural = Model.Analyses[0]
fixed_support = static_structural.Children[2]
loc = fixed_support.Location
pressure = static_structural.Children[1]
ids = loc.Ids
print("Fixed support geometry IDS: ", ids)
geo = Model.Geometry
for body in geo.Children:
    for part in body.Children:
       print(part.Name, part.ObjectId) #Note, ObjectId not Id!


