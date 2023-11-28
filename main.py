import os
import json
import xml.etree.ElementTree as ET

def convert_xml_to_json(xml_path, target_language):
    sound_data = {}

    root = ET.parse(xml_path).getroot()
    soundbanks = root.find("SoundBanks")

    for soundbank in soundbanks.findall("SoundBank"):
        language = soundbank.attrib.get("Language", "")
        if language != target_language and language != "SFX":
            continue

        soundbank_name = soundbank.find("ShortName").text
        events = [event.get("Name") for event in soundbank.findall(".//Event")]
        sound_data[soundbank_name] = events

    output_path = xml_path.replace(".xml", ".json")
    with open(output_path, "w") as json_file:
        json.dump(sound_data, json_file, indent=4)

    print(f"Conversion completed for {xml_path}. JSON file saved at {output_path}")

if __name__ == '__main__':
    for dir_entry in os.listdir('.'):
        xml_path = os.path.join(dir_entry, "SoundbanksInfo.xml")
        if os.path.isfile(xml_path):
            print(f"Converting {xml_path}")
            convert_xml_to_json(xml_path, "English(US)")

    input("Press any key to exit...")
