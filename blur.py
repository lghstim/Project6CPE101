def blur_image():
   pixels = []
   in_file = open(sys.argv[1], 'r')
   out_file = open('faded.ppm', 'w')

def groups_of_3(values): # values is a list
   values = [int(val) for val in values] # convert string list to int list
   groups_of_three = []
   for index in range(0, len(values), 3): # increment by 3 each iteration
      groups_of_three.append(values[index:index+3])
   print(groups_of_three)
   return groups_of_three

   

if __name__ == '__main__':
   blur_image()
   

