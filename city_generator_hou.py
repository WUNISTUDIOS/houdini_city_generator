import hou

def city_generator():
     obbj_level = hou.node

#destroys and recreate old node from last deploy
     for node in obj_level.children():
          node.destroy()

     city_geo = obj_level.createNode("geo", node_name = "city_geo")
     ground = city_geo.createNode("grid", node_name =  "ground")
     building = city_geo.createNode("box", node_name = "building")
     building_points = city_geo.createNode("scatter", "building_points")

     building_points.setInput(0, ground)

     city_multiply = city_geo.createNode("copytopoints", "city_multiply")
     match_floor = city_geo.createNode("xform", "match_size")

     match_floor.setInput(building)
     
     pscale_rand = city_geo.createNode("attribrandomize", "pscale_rand")
     pscale_rand.setInput(building_points)





#laysouts nodes in houdini upon creation
     city_geo.layoutChildren()





city_generator()





#needs python path to be able to communicafte with houdini fuctions
