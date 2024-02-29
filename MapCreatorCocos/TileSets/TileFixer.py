class TileData:
    def __init__(self, fileName, specialCharacter):
        self.fileName = fileName
        self.specialCharacter = specialCharacter

    def getFilePath(self):
        return self.fileName
    def getSpecialCharacter(self):
        return self.specialCharacter
    
############################

import xml.etree.ElementTree as ET

def update_tileset(file_path, special_character):
    tree = ET.parse(file_path)
    root = tree.getroot()

    new_id_counter = 1

    for tile in root.findall(".//tile"):
        tile.set("id", str(new_id_counter))  
        new_id_counter += 1

        properties = tile.find(".//property[@name='AssetName']")
        if properties is not None:
            current_value = properties.get("value")
            if current_value:
                new_value = "{}{:04d}".format(special_character, new_id_counter - 1)
                properties.set("value", new_value)

    tree.write(file_path, encoding="UTF-8", xml_declaration=True)

#   NAMES  :   SHORTCUTS
#   Gates       G
#   Floor       F
#   Decals      D
#   Box         B
#   Walls       W
    

if __name__ == "__main__":
    file_extension = ".tsx"
    listOfObject = []
    
    listOfObject.append(TileData("Gate", "G"))
    listOfObject.append(TileData("Floor", "F"))
    listOfObject.append(TileData("Decal", "D"))
    listOfObject.append(TileData("Box", "B"))
    listOfObject.append(TileData("Walls", "W"))
    

    for i in listOfObject:
        update_tileset(i.getFilePath() + file_extension, i.getSpecialCharacter())


