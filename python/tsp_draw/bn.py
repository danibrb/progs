import os

from tspart import studio

from PIL import Image
from IPython.display import display

def display_width(img, width=600):
    ratio = img.size[0] / img.size[1]
    
    new_size = (
        width,
        int(round(width / ratio))
    )
    
    display(img.resize(new_size))
    
working_directory = ""
image_file = os.path.join(working_directory, "nword.jpg")
number_of_points = 8000
color_mode = studio.ColorMode.GRAYSCALE

image_name = os.path.splitext(os.path.basename(image_file))[0]
main_name = f"{image_name}_{number_of_points}_{color_mode.value}"

tsp_image_file = os.path.join(working_directory, f"{main_name}.jpg")
tsp_file = os.path.join(working_directory, f"{main_name}.tspstudio")

image = Image.open(image_file)
tsp = studio.TspStudio(
            mode=color_mode,
            image=image,
            num_points=number_of_points
    )

tsp.stipple(iterations=5)
tsp.save(tsp_file)

tsp.offline_solves(time_limit_minutes=5, verbose=False)
tsp.save(tsp_file)
print("Saved.")

tsp.line_width = 1
tsp.save(tsp_file)
print("Saved.")
drawn_image = tsp.draw(scale=1)

display_width(drawn_image)
drawn_image.save(tsp_image_file)
