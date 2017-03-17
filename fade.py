import math
import sys

def fade_image():
   try:
      in_file = open(sys.argv[1], 'r')
      out_file = open('faded.ppm', 'w')
      # read each pixel and set image properties
      line_num = 1
      pixel = []
      image_properties = []
      x_loc = 0
      y_loc = 0
      for line in in_file:
         line = line.strip() # strip \n at end of string 
         if line_num <= 3:
            image_properties.append(line)
            if line_num == 2:
               width_image = int(line.split(' ')[0])
               height_image = int(line.split(' ')[1])
         if line_num == 3:
            set_out_file_image_properties(image_properties, out_file) # set out file image properties
         if line_num > 3: 
             if len(groups_of_3(line.split(' '))) >= 2: # if more than one pixel on a line
               pixels = groups_of_3(line.split(' '))
               for single_pixel in pixels:
                  if len(single_pixel) == 3:
                     process_single_pixel(single_pixel, x_loc, y_loc, out_file)
                     if x_loc == width_image - 1:
                        y_loc += 1
                        x_loc = 0
                     else:
                        x_loc += 1
               pixels = [] # reset pixels variable
             else:  # if not more than one pixel on a line 
                pixel.append(line)
                if len(pixel) == 3:
                   process_single_pixel(pixel, x_loc, y_loc, out_file) 
                   if x_loc ==  width_image - 1:
                      y_loc += 1
                      x_loc = 0
                   else:
                      x_loc += 1
                   pixel = [] # reset pixel variable
         line_num += 1
      in_file.close()
      out_file.close()
   except IndexError:
      print('Usage: python3 fade.py <image> <row> <column> <radius>')
   except PermissionError:
      print('Unable to open {:s}'.format(sys.argv[1]))
   except FileNotFoundError:
      print('Unable to open {:s}'.format(sys.argv[1]))
   finally: 
      sys.exit(1)

def process_single_pixel(pixel, x_loc, y_loc, out_file):
   dist = distance_from_pixel_to_point((x_loc, y_loc), (int(sys.argv[2]), int(sys.argv[3])))
   pixel =  scale_pixel_components(pixel, dist) # returns scaled pixel
   red_val = pixel[0]
   green_val = pixel[1]
   blue_val = pixel[2]
   write_pixel(red_val, green_val, blue_val, out_file) # output pixel 

def distance_from_pixel_to_point(pixel_coords, point):
   return math.sqrt((pixel_coords[0] - point[0]) ** 2 + (pixel_coords[1] - point[1]) ** 2)

def write_pixel(red_val, green_val, blue_val, out_file):
   out_file.write('{:s}\n'.format(str(red_val)))
   out_file.write('{:s}\n'.format(str(green_val)))
   out_file.write('{:s}\n'.format(str(blue_val)))
   
def set_out_file_image_properties(image_properties, out_file):
   for value in image_properties:
      out_file.write('{:s}\n'.format(str(value)))

def scale_pixel_components(pixel, dist):
   radius = int(sys.argv[4])
   scale = (radius - dist) / radius
   if scale < 0.2:
      scale = 0.2
   red_val = int(pixel[0])
   green_val = int(pixel[1])
   blue_val = int(pixel[2])
   pixel[0] = int(red_val * scale)
   pixel[1] = int(green_val * scale)
   pixel[2] = int(blue_val * scale)
   return pixel

def groups_of_3(values): # values is a list
   groups_of_three = []
   for index in range(0, len(values), 3): # increment by 3 each iteration
      groups_of_three.append(values[index:index+3])
   groups_of_three = convert_stringlist_to_intlist(groups_of_three)
   return groups_of_three

def convert_stringlist_to_intlist(lst):
   for group in lst:
      for index in range(len(group)):
         group[index] = int(group[index])
   return lst

if __name__ == '__main__':
   fade_image()

