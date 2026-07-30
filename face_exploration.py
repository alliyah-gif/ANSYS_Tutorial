for part in Model.Geometry.Children: 
    for body in part.Children:
        print(part.Name, body.Name, type(body))

one_body = Model.Geometry.Children[0].Children[0]
geo_body = one_body.GetGeoBody()
print(geo_body)
faces = geo_body.Faces
print(faces)
print(len(faces))

sample_face = faces[0]
print(type(sample_face))
clr_type = sample_face.GetType()
for member in clr_type.GetProperties():
    print(member.Name)

for f in faces:
    print(f.Id, f.SurfaceType)

contact = DataModel.GetObjectsByType(DataModelObjectCategory.ContactRegion)[0]
source_ids = list(contact.SourceLocation.Ids)
print(source_ids)

matching_faces = [f for f in faces if f.Id in source_ids]
print(len(matching_faces))

#NOTE: Looking for: Ansys.ACT.Interfaces.Geometry.GeoSurfaceTypeEnum.GeoSurfaceCylinder