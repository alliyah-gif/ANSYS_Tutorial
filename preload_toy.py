#Create beam, check properties
beam = Model.Connections.AddBeam()
clr_type = beam.GetType()
for member in clr_type.GetProperties():
    print(member.Name)

#Toy preload
source_id, target_id = 113, 160

beam = Model.Connections.AddBeam()

ref_sel = ExtAPI.SelectionManager.CreateSelectionInfo(SelectionTypeEnum.GeometryEntities)
ref_sel.Ids = [source_id]
beam.ReferenceLocation = ref_sel

mob_sel = ExtAPI.SelectionManager.CreateSelectionInfo(SelectionTypeEnum.GeometryEntities)
mob_sel.Ids = [target_id]
beam.MobileLocation = mob_sel

print(beam.ReferenceLocation.Ids)
print(beam.MobileLocation.Ids)
print(beam.ReferenceXCoordinate, beam.ReferenceYCoordinate, beam.ReferenceZCoordinate)
print(beam.MobileXCoordinate, beam.MobileYCoordinate, beam.MobileZCoordinate)