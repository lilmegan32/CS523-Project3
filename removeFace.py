import sys
import getopt
from PIL import Image, ImageDraw

def removeFace(inputfile, outputfile, x, y, width, height):
	im = Image.open(inputfile)

	# Convert to RGB mode
	if im.mode != "RGB":
		im = im.convert("RGB")

	draw = ImageDraw.Draw(im)
	#draw.line((0, 0) + im.size, fill=128)
	#draw.line((0, im.size[1], im.size[0], 0), fill=128)

	#strTemp = x.str() + ',' + y.str() + ',' + (x+width).str() + ',' + (y+height).str()
	x2 = x + width
	y2 = y + height
	draw.rectangle([x,y,x2,y2], fill='grey')

	del draw

	# write to stdout

	#outfile = open('image2.png');
	#outfile.close();
	im.save(outputfile, "PNG")




def main(argv):
   inputfile = ''
   outputfile = ''
   x = 0
   y = 0
   width = 0
   height = 0

   #print "argv[0] = ", argv[6]
   #print argv

   try:
      opts, args = getopt.getopt(argv,"h:i:o:x:y:w:z:")
      #print opts
      #print args
   except getopt.GetoptError:
      print('test.py -i <inputfile> -o <outputfile> -x <xLocationOfBox> -y <yLocationOfBox> -w <widthOfBox> -z <heightOfBox>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
        print('test.py -i <inputfile> -o <outputfile> -x <xLocationOfBox> -y <yLocationOfBox> -w <widthOfBox> -z <heightOfBox>')
        sys.exit()
      elif opt in ("-i"):
        inputfile = arg
      elif opt in ("-o"):
        outputfile = arg
      elif opt in ("-x"):
        x = int(arg)
      elif opt in ("-y"):
        y = int(arg)
      elif opt in ("-w"):
        width = int(arg)
      elif opt in ("-z"):
      	print 'arg = ', arg
        height = int(arg)
      else:
        print('test.py -i <inputfile> -o <outputfile>')
        sys.exit(0)

   print
   print     
   print 'Input file is: ', inputfile
   print 'Output file is: ', outputfile
   print 'x is: ', x
   print 'y is: ', y
   print 'width is: ', width
   print 'height is: ', height
   print
   print

   removeFace(inputfile, outputfile, x, y, width, height)

if __name__ == "__main__":
   main(sys.argv[1:])