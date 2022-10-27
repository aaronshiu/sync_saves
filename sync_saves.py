from pathlib import Path
import shutil
import time
import json

from checksumdir import dirhash

default_backup_dir = "./Game Saves" # default game saves backup location is in 'Game Saves' folder in the same directory as this script
default_save_locations = "./saveLocations.txt" # default game saves locations file is in the same directory as this script - in the form {"gameTitle1": "/path/to/game/save1", "gameTitle2": "/path/to/game/save2"} 

backup_dir = "" or default_backup_dir
save_locations = "" or default_save_locations

def hashing(loc):
	return dirhash(loc, "sha1")

print("\n\nScript to backup game saves to a syncing folder\n===============================================\n\n")

save_txt_path = Path(save_locations)

if not save_txt_path.exists():
	print(f"'{save_locations}' does not exist!\n\n")

try:
	with open(save_txt_path, "r") as f:
		data = f.read()

	dict_data = json.loads(data)

	if not dict_data:
		print("No save location data in file!\n\n")
		print("Quitting in 5s!\n")
		time.sleep(5)
		quit()

except Exception as e:
	print("Something went wrong with loading the data in the save locations file!")
	print(f"{e}\n\n")
	print("Quitting in 5s!\n")
	time.sleep(5)
	quit()

src_names = [y for y in dict_data.keys()]
src_dirs = [Path(x) for x in dict_data.values()]
dst_dirs = [Path(backup_dir)/j for j in src_names]

for i in range(len(src_names)):
	src_name = src_names[i]
	src = src_dirs[i]
	dst = dst_dirs[i]
	if not src.exists():
		print(f"The source directory '{src}' does not exist!\n")
		continue
	if dst.exists():
		if hashing(src) == hashing(dst):
			print(f"Hashes match for: '{src_name}'!\n")
			continue
	try:
		shutil.copytree(src, dst, dirs_exist_ok=True)
	except Exception as e:
		print(f"Could not copy '{src}' to '{dst}' for some reason!")
		print(f"{e}\n\n")
		print("Quitting in 5s!\n")
		time.sleep(5)
		quit()
	print(f"\n'{src_name}' saved!\n")

print("\nQuitting in 5s!\n")
time.sleep(5)
quit()
