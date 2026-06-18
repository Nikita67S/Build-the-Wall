"""Here connection all modules by functions from another modules for count all needed materials for building the wall
"""


from buildWall.CalcCommon.volume_wall import volume
from buildWall.CalcCommon import constants
from buildWall.CalcBricks.percent_bricks_in_wall import percent_bricks
from buildWall.CalcBricks.count_of_bricks import counter_bricks
from buildWall.CalcMortar.volume_mortar_in_wall import mortar_volume
from buildWall.CalcMortar.volume_mortar_in_kg import kilograms
from buildWall.CalcCommon.Stock import stock_func


wall_lwh = (10000, 510, 3000) #Size the wall: length, width, height in mm
#unpacking
l, w, h = wall_lwh
#Commentars about func volume
volume_of_wall = volume(length_wall=l, thickness_wall=w, height_wall=h)
#Commentars about func percent_bricks
per_bricks = percent_bricks(volume_of_wall, constants.standard_percentage_brick)
#Commentars about func counter_bricks
need_bricks = counter_bricks(per_bricks, constants.BRICKS_PER_M3)
#Commentars about func mortar_volume
v_mortar = mortar_volume(volume_of_wall, constants.standard_percentage_wall)
#Commentars about func kilograms
kg = kilograms(v_mortar, constants.MORTAR_KG_PER_M3)
#Commentars about func stock_func
all_resources = stock_func(need_bricks, kg, constants.BRICK_RESERVE_FACTOR, constants.MORTAR_RESERVE_FACTOR)

bricks, mortar_kg = all_resources

print(f"All need bricks: {bricks}\n"
      f"All need mortar in kilograms: {mortar_kg}"
      )


















