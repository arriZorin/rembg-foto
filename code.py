from rembg import remove
from PIL import Image
import easygui as eg

red=[235,0,0,255]

input_path = eg.fileopenbox(title='Select image file')
output_path = eg.filesavebox(title='Save file to..')
input = Image.open(input_path)
output = remove(input, bgcolor=red, post_process_mask=True)
output.save(output_path)
