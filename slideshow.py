import os, time, pathlib, sys, random, shutil

home = str(pathlib.Path.home())
pictures_folder = home + "/Pictures/"
wallpapers_folder = pictures_folder + "Wallpapers/"

user = input("Name of folder: ")

gallery = []
gallery_links = []

# Checks if user input exists as a folder.
if user == "" or not os.path.exists(pictures_folder + user + "/"):
	slideshow_folder = pictures_folder
else:
	slideshow_folder = pictures_folder + user + "/"

# Grabs all images in folder & puts name and location into lists
for piece in os.listdir(slideshow_folder ):
	if ".jpg" not in piece and ".png" not in piece:
		pass
	else:
		gallery.append(piece )
		gallery_links.append(slideshow_folder + piece )

# Goes through lists, randomly placing images as desktop background.
# Copies image into the Wallpapers folder and deletes other images.
for a in range(10000):
	for i in range(len(gallery ) ):
		random_piece = random.randint(0, len(gallery ) - 1 )

		print("Current Background: " + gallery[random_piece ] )
		print("Change no. " + str(a * len(gallery_links ) + i + 1) )

		os.system("/usr/bin/gsettings set org.gnome.desktop.background picture-uri " + gallery_links[random_piece ] )

		for erased in os.listdir(wallpapers_folder):
			os.remove(wallpapers_folder + erased)
		shutil.copyfile(gallery_links[random_piece], wallpapers_folder + gallery[random_piece])

		for remaining in range(5, 0, -1 ):
			sys.stdout.write("\r" )
			sys.stdout.write("{:2d} seconds remaining".format(remaining ) )
			sys.stdout.flush()
			time.sleep(1)
		
		print()


