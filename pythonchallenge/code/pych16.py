from PIL import Image
a=Image.open(r'C:\users\team2\desktop\pych\mozart.gif')
test=None
for i in range(640-4):
    test=a.getpixel((i,0))
    if test==a.getpixel((i+4,0)) and a.getpixel((i+1,0))==a.getpixel((i+2,0))==a.getpixel((i+3,0)):
        print i #example line


        
print a.getpixel((429,0))#color
indexes=[]
for j in range(480):
    for i in range(640-4):
        test=a.getpixel((i,j))
        if test==a.getpixel((i+4,j)) and test==195:
            indexes+=[(i,j)]

b=Image.new(a.mode,a.size)


#putpixels by indexes later
for i in indexes:
	for j in range(640):
		b.putpixel((j,i[1]),a.getpixel(((i[0]+j)%640,i[1])))
b.save(r'C:\users\team2\desktop\pych\16.gif')
