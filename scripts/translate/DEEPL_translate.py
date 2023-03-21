import os
import re
import deepl

translator = deepl.Translator("API_KEY")


def main(dirfrom, dirto, langfrom, langto):
    for filename in [x for x in os.listdir(dirfrom) if x.endswith(".yml")]:
        localization = {}
        f = os.path.join(dirfrom, filename)
        with open(f, "r") as file:
            for line in file:
                r = re.search("(.*:?0?\s)\"(.+)\"", line)
                if r:
                    localization[r[1]] = r[2]
                    filename = file.name.rpartition("\\")[2]
                    filename = filename.replace(langfrom, langto)
            new_f = os.path.join(dirto, filename.replace(langfrom, langto))
            with open(new_f, "w") as newfile:
                newfile.write(f"l_{langto}:\n\n")
                translation_list = list(localization.values())
                result = translator.translate_text(translation_list, target_lang="FR")
                for j in result:
                    newfile.write(i + "\"" + j.text + "\"" + "\n")


if __name__ == '__main__':
    main(
        "C:\\Users\\USERNAME\\Documents\\Paradox Interactive\\Victoria 3\\mod\\More Flavor Events\\localization\\english",
        "C:\\Users\\USERNAME\\Documents\\Paradox Interactive\\Victoria 3\\mod\\More Flavor Events\\localization\\french",
        "english",
        "french"
    )
