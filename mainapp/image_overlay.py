# overlay('face.jpg', 'glasses.png', 225, [(140, 185), (188, 185)], 50, 100).save('new.jpg')
from PIL import Image
from math import floor

def overlay(face: str, glasses: str, dim_width: int,
            coords_eyes: list, h_offset: int, v_offset: int):
	original_face = Image.open(face)
	original_glasses = Image.open(glasses)

	scale = dim_width / original_glasses.size[0]

	new_dims = floor(original_glasses.size[0] * scale), \
				floor(original_glasses.size[1] * scale)

	new_glasses = original_glasses.resize(new_dims, 
		Image.ANTIALIAS)

	mid_coords_eyes = floor((coords_eyes[0][0] + coords_eyes[1][0]) / 2),\
						floor((coords_eyes[1][0] + \
                                                       coords_eyes[1][1]) / 2)

	# implement rotation if have time

	original_face.paste(new_glasses, (h_offset,
                                          v_offset), new_glasses)

	return original_face
