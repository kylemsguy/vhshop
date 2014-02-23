from PIL import Image

def overlay(face: str, glasses: str, dim_width: tuple, coords_eyes: list):
	original_face = Image.open(face)
	original_glasses = Image.open(glasses)

	scale = dim_width /
 