
reinforcement = DataModel.GetObjectsByName("15141799 REINFORCMENT")[0]
ns = Model.AddNamedSelection()
ns.Name = "Test-Selection"
#NOTE: This line throws a warning/error "ArgumentTypeException: expected ISelectionInfo, got Part: line 4" but it doesn't seem to affect rendering?
ns.Location = reinforcement

new_force = static_structural.AddForce()
new_force.Location = ns
new_force.DefineBy = LoadDefineBy.Components
new_force.YComponent.Output.DiscreteValues = [Quantity(10, "N")]