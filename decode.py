import sys
'''The puzzle image (shown below) hides a real image behind a mess of random pixels. In reality, the image is hidden in the red components of the pixels. Decode the image by increasing the value of the red component by multiplying it by 10 (do not allow the resulting value to pass the maximum value of 255). In addition, set the green and blue components equal to the new red value.'''

'''Note: you must read a pixel, process the pixel, and then output the pixel before moving to the next pixel (in other words, you must not store all of the pixels).

'''

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

def decode_image():
   try:
      in_file = open(sys.argv[1], 'r')
      out_file = open('decoded.ppm', 'w')

      # read each pixel and set image properties
      line_num = 1
      pixel = []
      image_properties = []
      for line in in_file:
         line = line.strip() # strip \n at end of string 
         if line_num <= 3:
            image_properties.append(line)
         if line_num == 3:
            set_out_file_image_properties(image_properties, out_file) # set out file image properties
         if line_num > 3: 
            if len(groups_of_3(line.split(' '))) >= 2: # if more than one pixel on a line
               pixels = groups_of_3(line.split(' '))
               # process each pixel
               for pixel_lst in pixels:
                  if len(pixel_lst) == 3:
                     red_val = int(pixel_lst[0]) # old red val
                     if red_val * 10 <= 255: # only proceed if result less than or equal to 255 
                        red_val = red_val * 10 # new red val
                     green_val = red_val # new green
                     blue_val = red_val # new blue
                     write_pixel(red_val, green_val, blue_val, out_file) # output pixel
                     pixels = [] # reset pixel variable
            else : # if not more than one pixel on a line
               pixel.append(line)
               # process each pixel
               if len(pixel) == 3:
                  red_val = int(pixel[0]) # old red val
                  if red_val * 10 <= 255: # only proceed if result less than or equal to 255 
                     red_val = red_val * 10 # new red val
                  green_val = red_val # new green
                  blue_val = red_val # new blue
                  write_pixel(red_val, green_val, blue_val, out_file) # output pixel
                  pixel = [] # reset pixel variable
         line_num += 1
      in_file.close()
      out_file.close()
   except IndexError:
      print("Usage: python3 decode.py <image>")
   except PermissionError:
      print("Unable to open {:s}".format(sys.argv[1]))
   except FileNotFoundError:
      print("Unable to open {:s}".format(sys.argv[1]))
   finally:
      sys.exit(1)

def write_pixel(red_val, green_val, blue_val, out_file):
   out_file.write('{:s}\n'.format(str(red_val)))
   out_file.write('{:s}\n'.format(str(green_val)))
   out_file.write('{:s}\n'.format(str(blue_val)))
   
def set_out_file_image_properties(image_properties, out_file):
   for value in image_properties:
      out_file.write('{:s}\n'.format(str(value)))

if __name__ == '__main__':
   decode_image()

   



