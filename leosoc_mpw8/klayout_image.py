in_file = "caravel_0008927d.oas"
out_name = "leosoc_mpw8"

w = 2048
aspect_ratio = 7.3/10
h = w / aspect_ratio
background_white = "#FFFFFF"
background_black = "#000000"

import klayout.lay as lay
import klayout.db as db

lv = lay.LayoutView()

lv.set_config("grid-visible", "false")
lv.set_config("grid-show-ruler", "false")
lv.set_config("text-visible", "false")
lv.load_layout(in_file, 0)
lv.max_hier()

lv.set_config("background-color", background_white)
lv.save_image(out_name + "_wb.png", w, h)

lv.set_config("background-color", background_black)
lv.save_image(out_name + "_bb.png", w, h)

lv.load_layer_props("sky130A.lyp")

lv.set_config("background-color", background_white)
lv.save_image(out_name + "_wb_lyp.png", w, h)

lv.set_config("background-color", background_black)
lv.save_image(out_name + "_bb_lyp.png", w, h)
