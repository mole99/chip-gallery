import os
import glob
import klayout.lay as lay
import klayout.db as db

def main(resolution: int = 2048, oversampling: int = 8):

    files = []
    for ext in ["*.gds", "*.gds.gz", "*.oas"]:
        files.extend([file for file in glob.glob(ext)])

    lyps = [file for file in glob.glob("*.lyp")]
    
    colors = {
        "white": "#FFFFFF",
    }

    for file in files:
        for lyp in lyps:
    
            print(f"Rendering: {file}")
            basename = os.path.splitext(file)[0]
            
            lyp_basename = os.path.splitext(lyp)[0]

            lv = lay.LayoutView()

            lv.set_config("grid-visible", "false")
            lv.set_config("grid-show-ruler", "false")
            lv.set_config("text-visible", "false")
            lv.load_layout(file, 0)
            lv.max_hier()

            # Get aspect ratio
            top_cell = lv.active_cellview().layout().top_cell()
            top_bbox = top_cell.dbbox()
            aspect_ratio = top_bbox.width() / top_bbox.height()
        
            width = resolution
            height = int(width / aspect_ratio)

            background_white = "#FFFFFF"
            background_black = "#000000"

            lv.load_layer_props(lyp)

            for color_name, color in colors.items():

                lv.set_config("background-color", color)
                lv.save_image_with_options(
                    f"{basename}_{lyp_basename}_{color_name}.png",
                    width,
                    height,
                    oversampling=oversampling,
                )


if __name__ == "__main__":
    main()
