import xml.etree.ElementTree as ET
import os

def changeNames(baseTiles, fileName):
    tsx_file_path = '../TileSets/{}.tsx'.format(fileName)

    tree = ET.parse(tsx_file_path)
    root = tree.getroot()

    path_base = os.path.join(baseTiles, fileName)

    errors = []

    for tile in root.iter('tile'):
        image = tile.find('image')

        if image is not None:
            source = image.get('source') 

            fileName = os.path.basename(source)

            properties = tile.find('properties')
            property_element = properties.find('property[@name="AssetName"]')

            if property_element is not None:
                name = property_element.get('value')

                new_file_name = '{}.png'.format(name)

                old_file_path = os.path.join(path_base, fileName)
                new_file_path = os.path.join(path_base, new_file_name)

                if os.path.exists(old_file_path):
                    try:
                        os.rename(old_file_path, new_file_path)
                        print("Renamed {} to {}".format(old_file_path, new_file_path))
                    except Exception as e:
                        errors.append("Error renaming file: {}".format(e))
                else:
                    errors.append("File not found: {}".format(old_file_path))

    tree.write(tsx_file_path)

    if errors:
        print("[*] Wait for an second for Error Logs.")
        print("\nErrors:")
        for error in errors:
            print(error)


if __name__ == "__main__":
    baseTilesPath = "/Users/yigithanaydin/hunter-assassin-2/AgentProject/Resources/textures/tiles"
    listOfObject = ["Floor", "Box", "Decal", "Gate", "Floor", "Walls"]

    for i in listOfObject:
        changeNames(baseTilesPath, i)
