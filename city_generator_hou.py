import hou

def city_generator():
     obj_level = hou.node

#destroys and recreate old node from last deploy
 
     for node in obj_level.children():
          node.destroy()

     city_geo = obj_level.createNode("geo", node_name = "city_geo")
     ground = city_geo.createNode("grid", node_name =  "ground")
     building = city_geo.createNode("box", node_name = "building")
     building_points = city_geo.createNode("scatter", "building_points")

     building_points.setInput(0, ground)

     building_copy = city_geo.createNode("copytopoints", "building_copy")
     match_floor = city_geo.createNode("xform", "match_size")
     match_floor.setFirstInput(building)
     
     pscale_rand = city_geo.createNode("attribrandomize", "pscale_rand")
     pscale_rand.setFirstInput(building_points)

     point_relax = city_geo.createNode("relax", "point_relax")
     point_relax.setInput(0, pscale_rand)
     point_relax.setInput(1, ground)

     building_copy.setInput(match_floor)
     building_copy.setnextInput(point_relax)



     grid_scale = city_geo.createNode("xform", "gridscale")
     grid_scale.setFirstInput(ground)

     merge = city_geo.createNode("merge", "building_ground_merge")
     merge.setFristInput(grid_scale)
     merge.setNextInpu(building_copy)


     Output = city_geo.createNode("null", "OUTPUT")
     Output.setFirstInput(merge)
     Output.setDisplayFlag(True)
     Output.setRenderFlag(True)


     # setting parameters

     building_points.parm("npts").set(40)
     
     pscale_rand.parm("name").set("pscale")
     pscale_rand.parm("minx").set(0.3)
     pscale_rand.parm("maxx").set(1.5)


     building.parm("sizey").set(1.3)

     point_relax.parm("maxiterations").set(100)
     point_relax.parm("relaxin3d").set(True)

     grid_scale.parm("s").set((1.2, 1.2, 1.2))

     match_floor.parm("ty").setExpression("ch('../building/sizey')/2")


#laysouts nodes in houdini upon creation

     city_geo.layoutChildren()

city_generator()

#needs python path to be able to communicafte with houdini fuctions
