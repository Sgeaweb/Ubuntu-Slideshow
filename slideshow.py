import os, time, pathlib, sys, random

home = str(pathlib.Path.home())

pictures_folder = home + "/Pictures/"

user = input("Folder Name: ")

if user == "" or not os.path.exists(pictures_folder + user + "/"):
	slideshow_folder = pictures_folder
else:
	slideshow_folder = pictures_folder + user + "/"

gallery = []
gallery_links = []

for piece in os.listdir(slideshow_folder ):
	if ".jpg" not in piece and ".png" not in piece:
		pass
	else:
		gallery.append(piece )
		gallery_links.append(slideshow_folder + piece )

for a in range(10000):
	for i in range(len(gallery ) ):
		random_piece = random.randint(0, len(gallery ) - 1 )
		print(gallery[random_piece ] )
		print("Current Background: " + gallery[random_piece ] )
		os.system("/usr/bin/gsettings set org.gnome.desktop.background picture-uri " + gallery_links[random_piece ] )
		for remaining in range(5, 0, -1 ):
			sys.stdout.write("\r" )
			sys.stdout.write("{:2d} seconds remaining".format(remaining ) )
			sys.stdout.flush()
			time.sleep(1)


