from PIL import Image
import Tkinter
stuff=[]
a=Image.open(r'C:\users\team2\desktop\pych\22.gif')
for k in range(133):
	a.seek(k)
	for i in range(200):
		for j in range(200):
			if a.getpixel((i,j)):
				stuff+=[(i,j)]
				print i,j


root=Tkinter.Tk()
c=Tkinter.Canvas(root,height=400,width=400)
stuff2=map(lambda x: (x[0]-100,x[1]-100), stuff)

c.pack()
startx,starty=50,50
clr=iter(['black','yellow','red','green','blue'])

for i in stuff2:
    if i==(0,0):
        fill=clr.next()
        startx+=50
        starty=50
    c.create_line(startx,starty,startx+i[0],starty+i[1],fill=fill,width=2)
    startx,starty=startx+i[0],starty+i[1]
    
root.mainloop()


