import sys
import math

def blur_image():
   try:
      pixel = []
      pixels = []
      pixels_row = []
      print(sys.argv)
      if len(sys.argv) <= 2:
         reach = 4
      else:
         reach = int(sys.argv[2])
      in_file = open(sys.argv[1], 'r')
      out_file = open('blur.ppm', 'w')
      line_num = 1
      image_properties = []
      row = 0
      col = 0
      width_image = 0
      height_image = 0
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
               pixels_row.append(pixel)
               if col == width_image - 1:
                  pixels.append(pixels_row)
                  pixels_row = []
                  row += 1
                  col = 0
               else:
                  col += 1
               pixel = []
         line_num += 1

      process_pixels(pixels, out_file, reach)
      out_file.close()
      in_file.close()
      
   except IndexError:
      print("Usage: python3 blur.py <image> [<reach>]")
   except PermissionError:
      print('Unable to open <image>'.format(sys.argv[1]))
   except FileNotFoundError:
      print('Unable to open <image>')
   finally:
      sys.exit(1)

def process_pixels(pixels, out_file, reach):
   # process pixels
   print(len(pixels[0])) # width
   print(len(pixels)) # height
   for y in range(len(pixels)): 
      for x in range(len(pixels[0])): 
         current_pixel = pixels[y][x]
         cur_x = x
         cur_y = y
         updated_pixel = get_updated_pixel(current_pixel, cur_x, cur_y, pixels, reach)
         red_val = updated_pixel[0]
         green_val = updated_pixel[1]
         blue_val = updated_pixel[2]
         write_pixel(red_val, green_val, blue_val, out_file)

  
def groups_of_3(values): # values is a list
   values = [int(val) for val in values] # convert string list to int list
   groups_of_three = []
   for index in range(0, len(values), 3): # increment by 3 each iteration
      groups_of_three.append(values[index:index+3])
   return groups_of_three

def get_neighbor_pixels(current_pixel, cur_x, cur_y, pixels, reach):
   neighbor_pixels = []
   x_min = cur_x - reach # starting x
   y_min = cur_y - reach # starting y
   x_max = cur_x + reach
   y_max = cur_y + reach
   if (x_min < 0): # if out of bounds on left
      x_min = 0
   if (y_min < 0): # if out of bounds on top
      y_min = 0
   if (y_max > len(pixels)):
      y_max = len(pixels) # if out of bounds on right side
   if (x_max > len(pixels[0])):
      x_max = len(pixels[0]) # if out of bounds on bottom

   for x in range(x_min, x_max, 1):
      for y in range(y_min, y_max, 1): 
         if (x == cur_x and y == cur_y): # if not the current pixel
            pass
         else:
            #print("x: {:d}".format(x))
            #print("y: {:d}".format(y))
            neighbor_pixels.append(pixels[y][x])
   return neighbor_pixels

def get_updated_pixel(current_pixel, cur_x, cur_y, pixels, reach):
   neighbor_pixels = get_neighbor_pixels(current_pixel, cur_x, cur_y, pixels, reach)
   sum_red_val = 0
   sum_green_val = 0
   sum_blue_val = 0
   num_pixels = len(neighbor_pixels) + 1
   for index in range(len(neighbor_pixels)):
      sum_red_val += neighbor_pixels[index][0]
      sum_green_val += neighbor_pixels[index][1]
      sum_blue_val += neighbor_pixels[index][2]
   sum_red_val += current_pixel[0]
   sum_green_val += current_pixel[1]
   sum_blue_val += current_pixel[2]
   red_val_avg = sum_red_val / (num_pixels) # get avg red
   green_val_avg = sum_green_val / (num_pixels) # get avg green
   blue_val_avg = sum_blue_val / (num_pixels) # get avg blue
   updated_pixel = [int(red_val_avg), int(green_val_avg), int(blue_val_avg)]
   return updated_pixel # color of updated pixel

def set_out_file_image_properties(image_properties, out_file):
   for value in image_properties:
      out_file.write('{:s}\n'.format(str(value)))

def write_pixel(red_val, green_val, blue_val, out_file):
   out_file.write('{:s}\n'.format(str(red_val)))
   out_file.write('{:s}\n'.format(str(green_val)))
   out_file.write('{:s}\n'.format(str(blue_val)))

if __name__ == '__main__':
   blur_image()
   

