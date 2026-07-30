contacts = DataModel.GetObjectsByType(DataModelObjectCategory.ContactRegion)
for c in contacts:
    print(c.Name, "| source:", c.SourceLocation.Name, "| target:", c.TargetLocation.Name)


"""
Model
  Geometry Imports
    Geometry Import
  Geometry
    Solid
      Solid
    Solid
      Solid
    Solid
      Solid
    Solid
      Solid
    Solid
      Solid
    Solid
      Solid
  Materials
    Structural Steel
  Coordinate Systems
    Global Coordinate System
  Remote Points
  Connections
    Contacts
      Contact Region
      Contact Region 2
      Contact Region 3
      Contact Region 4
      Contact Region 5
      Contact Region 6
      Contact Region 7
      Contact Region 8
      Contact Region 9
  Mesh
  Named Selections
    block3_block2_cont
    block3_block2_targ
    shank_block3_targ
    shank_block3_cont
    block1_washer_cont
    block1_washer_targ
    washer_bolt_cont
    washer_bolt_targ
    shank_bolt_targ
    shank_bolt_cont
    block2_block1_cont
    block2_block1_targ
    all_bodies
    bodies_5
    shank
    shank_face
    shank_face2
    bottom_surface
    block2_surface
    shank_surface
"""