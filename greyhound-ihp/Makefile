
create-image:
	klayout -z -r klayout_image.py -rd input_gds=greyhound_ihp_top.gds.gz -rd output_image=greyhound_ihp_top.png
	convert greyhound_ihp_top.png -resize 25% greyhound_ihp_top_small.png
.PHONY: create-image

