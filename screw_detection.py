for conn in Model.Connections.Children:
    print(conn.Name, conn.DataModelObjectCategory)

for part in Model.Geometry.Children:
    for body in part.Children:
        if "screw" in body.Name.lower() or "bolt" in body.Name.lower() or "fastener" in body.Name.lower():
            print(body.Name)