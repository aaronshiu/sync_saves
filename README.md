# Backup any game save for cloud-sync'ing
Little script to backup an editable list of game save folders (steam/non-steam/emulation etc.) by checking hashes, for self-hosted cloud-sync purposes such as Nextcloud


## Usage
Clone the repository
```
git clone https://github.com/aaronshiu/sync_saves.git
cd sync_saves
```
Add the location(s) of the game save(s) you wish to backup in ```saveLocations.txt``` in the dict form ```{"gameTitle1": "/path/to/save1", "gameTitle2": "/path/to/save2"}``` i.e.
```
{
    "Cyberpunk 2077": "/home/deck/pfx/Cyberpunk 2077/drive_c/users/deck/Saved Games/CD Projekt Red/Cyberpunk 2077",
    "Xenoblade Chronicles 3": "/home/deck/.local/share/yuzu/nand/user/save/0000000000000000/FCD8B4E17D8B29718718973F848A4AD2/010074F013262000"
}
```
Install a dependency via pip
```
python -m pip install -r requirements.txt
```
Run the script
```
python -m sync_saves.py
```



## Documentation

- Can optionally add a new ```Game Saves``` folder location/name on ```line 11``` (in the quotation marks ```"```) to match a folder in sync'ing software like Nextcloud Desktop client
- Can optionally add a new ```saveLocations.txt``` file location/name on ```line 12``` (in the quotation marks ```"```) for a more convenient location/name
