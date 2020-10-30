from pygame import *
import sys
init()
display.set_caption("shapes")
koki=display.set_mode((400,300))
hari=display.get_surface()
draw.ellipse(koki,(255,0,0),(250,350,80,60),0)
draw.circle(koki,(0,0,255),(370,450),200,5)
draw.ellipse(koki,(255,0,0),(400,350,80,60),0)
draw.ellipse(koki,(0,255,0),(280,510,180,40),1)
draw.rect(koki,(0,0,255),(230,650,300,500),1)
draw.rect(koki,(0,0,255),(110,700,120,80),1)
draw.rect(koki,(0,0,255),(530,700,120,80),1)
draw.rect(koki,(0,0,255),(260,1150,80,200),1)
draw.rect(koki,(0,0,255),(420,1150,80,200),1)
display.flip()
while True:
	for e in event.get():
		if e.type==QUIT:
			quit()
			sys.exit()
	display.update()