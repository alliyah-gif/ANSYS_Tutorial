## Inspect Geometry Keys
geo = Model.Geometry
contacts = DataModel.GetObjectsByType(DataModelObjectCategory.ContactRegion)
for prop in contacts:
    if "id" in prop.lower():
        print(prop)

# Get properties
contact = DataModel.GetObjectsByType(DataModelObjectCategory.ContactRegion)[0]
clr_type = contact.GetType()
for member in clr_type.GetProperties():
    print(member.Name)