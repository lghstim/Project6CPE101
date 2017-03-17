import sys
import math

def blur_image():
   try:
      pixel = []
      pixels = []
      all_pixel_coords = []
      reach = 4
      if len(sys.argv) == 2:
         reach = 4
      in_file = open(sys.argv[1], 'r')
      out_file = open('blur.ppm', 'w')
      line_num = 1
      image_properties = []
      x_loc = 0
      y_loc = 0
      # read each pixel and set image properties
      for line in in_file:
         line = line.strip() # strip \n at end of string 
         if line_num <= 3:
            image_properties.append(line)
            if line_num == 2:
               width_image = int(line.split(' ')[0])
               height_image = int(line.split(' ')[1])
         if line_num == 3:
            set_out_file_image_properties(image_properties, out_file)
         if line_num > 3:
            pixel.append(int(line))
            if len(pixel) == 3:
               pixels.append(pixel) # append pixel to the 2D list
               all_pixel_coords.append((x_loc, y_loc)) # append pixel coords
               if x_loc == width_image - 1:
                  y_loc += 1
                  x_loc = 0
               else:
                  x_loc += 1
               pixel = []
         line_num += 1
      # process pixels
      for current_pixel in pixels: 
         neighbor_pixels = get_neighbor_pixels(current_pixel, all_pixel_coords, pixels, reach)
         updated_pixel = get_updated_pixel(current_pixel, neighbor_pixels)
         current_pixel = updated_pixel 
         red_val = current_pixel[0]
         green_val = current_pixel[1]
         blue_val = current_pixel[2]
         write_pixel(current_pixel[0], current_pixel[1], current_pixel[2], out_file)
       
      in_file.close()
      out_file.close()
   except IndexError:
      print('Usage: python3 blur.py <image> [<reach>]')
   except PermissionError:
      print('Unable to open <image>'.format())
   except FileNotFoundError:
      print('Unable to open <image>'.format())
   finally:
      sys.exit(1)

# returns pixels list
def process_pixels():
   pass

def groups_of_3(values): # values is a list
   values = [int(val) for val in values] # convert string list to int list
   groups_of_three = []
   for index in range(0, len(values), 3): # increment by 3 each iteration
      groups_of_three.append(values[index:index+3])
   #print(groups_of_three)
   return groups_of_three

def get_neighbor_pixels(current_pixel, all_pixel_coords, pixels, reach):
   neighbor_pixels = []
   current_pixel_index = pixels.index(current_pixel) # get index of current_pixel
   for index in range(len(pixels)):
      dist = get_distance(all_pixel_coords[current_pixel_index], all_pixel_coords[index]) # distance from current pixel to another pixel in image
      if dist <= reach * math.sqrt(2) and dist != 0: # if within neighbor range and not the current pixel
         neighbor_pixels.append(pixels[index]) # the pixels list and all_pixel_coords list are indexed in the same way
   return neighbor_pixels

# get distance between two pixels
def get_distance(current_pixel_coords, other_pixel_coords):
   return math.sqrt((current_pixel_coords[0] - other_pixel_coords[0]) ** 2 + (current_pixel_coords[1] - other_pixel_coords[1]) ** 2)

def get_updated_pixel(current_pixel, neighbor_pixels):
   sum_red_val = 0
   sum_green_val = 0
   sum_blue_val = 0
   num_vals = 0
   for index in range(len(neighbor_pixels)):
      num_vals += 1
      sum_red_val += neighbor_pixels[index][0]
      sum_green_val += neighbor_pixels[index][1]
      sum_blue_val += neighbor_pixels[index][2]
   sum_red_val += current_pixel[0]
   sum_green_val += current_pixel[1]
   sum_blue_val += current_pixel[2]
   red_val_avg = sum_red_val / (num_vals + 1) # get avg red
   green_val_avg = sum_green_val / (num_vals + 1) # get avg green
   blue_val_avg = sum_blue_val / (num_vals + 1) # get avg blue
   return [int(red_val_avg), int(green_val_avg), int(blue_val_avg)] # color of updated pixel

def set_out_file_image_properties(image_properties, out_file):
   for value in image_properties:
      out_file.write('{:s}\n'.format(str(value)))

def write_pixel(red_val, green_val, blue_val, out_file):
   out_file.write('{:s}\n'.format(str(red_val)))
   out_file.write('{:s}\n'.format(str(green_val)))
   out_file.write('{:s}\n'.format(str(blue_val)))

if __name__ == '__main__':
   blur_image()
   

