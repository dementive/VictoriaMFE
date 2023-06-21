import os
import re
import deepl
import collections

translator = deepl.Translator("API_KEY")

def frequency_sort(li):
	f = collections.Counter(li)
	li.sort(key = lambda x:(-f[x], x))
	return li

def remove_list_duplicates(seq):
	seen = set()
	seen_add = seen.add
	return [x for x in seq if not (x in seen or seen_add(x))]

def create_file_to_translate(dirfrom, dirto, langfrom, langto):
	text = []
	key_text = []
	for filename in [x for x in os.listdir(dirfrom) if x.endswith(".yml")]:
		localization = {}
		f = os.path.join(dirfrom, filename)
		with open(f, "r", encoding='utf-8-sig') as file:
			for line in file:
				r = re.search("([A-Za-z_0-9\.][A-Za-z_0-9\.]*):?\d?\s\"(.+)\"", line)
				if r:
					localization[r[1]] = r[2] + "\n"
					filename = file.name.rpartition("\\")[2]
					filename = filename.replace(langfrom, langto)
			new_f = os.path.join(dirto, filename.replace(langfrom, langto))
			translation_list = list(localization.values())
			keys = list(localization.keys())
			key_string = ""
			for i in keys:
				key_string += i + ","
			key_text += [f"----[{filename}, {[key_string]}]----\n"]
			text.append(translation_list)

	with open("keys.txt", "w", encoding='utf-8-sig') as f:
		for i in key_text:
			f.write(i)
	text_list = list()
	at_bracket_loc_links_list = list()
	dollar_loc_links_list = list()
	at_loc_links_list = list()
	dynamic_text_list = list()
	for i in text:
		for j in i:
			# Remove @[SCOPE.GetFlag]! first because they are super irregular and don't play well with the other regexes
			at_bracket_links = re.findall("(\@\[.*?\]\!)", j)
			if at_bracket_links:
				for k in at_bracket_links:
					at_bracket_loc_links_list.append(k)
			# < character marks @[SCOPE.GetFlag]! replacements in translated text
			j = re.sub("(\@\[.*?\]\!)", "<", j)

			loc_links = re.findall("(\$[A-Za-z_0-9\.|%+-=][A-Za-z_0-9\.|%+-=]*\$)", j)
			if loc_links:
				for k in loc_links:
					dollar_loc_links_list.append(k)
			dynamic_text = re.findall("(\[.*?\])", j)
			if dynamic_text:
				for k in dynamic_text:
					dynamic_text_list.append(k)
			at_loc_links = re.findall("(@[A-Za-z_0-9\.][A-Za-z_0-9\.]*!)", j)
			if at_loc_links:
				for k in at_loc_links:
					at_loc_links_list.append(k)
			# ~ character marks $x$ replacements in translated text
			j = re.sub("(\$[A-Za-z_0-9\.|%+-=][A-Za-z_0-9\.|%+-=]*\$)", "~", j)
			# ^ character marks [Prompt.GetFunction] replacements in translated text
			j = re.sub("(\[.*?\])", "^", j)
			# > character marks @loc_key! replacements in translated text
			j = re.sub("(@[A-Za-z_0-9\.][A-Za-z_0-9\.]*!)", ">", j)
			text_list.append(j)
	with open("text.txt", "w", encoding='utf-8-sig') as f:
		for i in text_list:
			f.write(i)

	return (at_bracket_loc_links_list, dollar_loc_links_list, at_loc_links_list, dynamic_text_list)

def translate_all_files(indir, outdir, target):
	for filename in [x for x in os.listdir(indir) if x.endswith(".yml")]:
		filename = indir + "\\" + filename
		translate_file(filename, target, outdir)

def translate_file(file, target_language, outdir):
	with open(file, "r") as f:
		to_tranlate = f.read()
	print(to_tranlate)

	#result = translator.translate_text(to_tranlate, target_lang="FR")
	#for j in result:
	#	newfile.write(i + "\"" + j.text + "\"" + "\n")

def rebuild_localization_from_translation(dirfrom, dirto, langfrom, langto):
	pass

if __name__ == '__main__':
	indir = "C:\\Users\\demen\\Documents\\Paradox Interactive\\Imperator\\mod\\ImperatorFMO\\localization\\english"
	outdir = "C:\\Users\\demen\\Documents\\Paradox Interactive\\Imperator\\mod\\ImperatorFMO\\localization\\french"
	# lists = create_file_to_translate(
	# 	"C:\\Users\\demen\\Documents\\Paradox Interactive\\Victoria 3\\mod\\More Flavor Events\\localization\\english",
	# 	"C:\\Users\\demen\\Documents\\Paradox Interactive\\Victoria 3\\mod\\More Flavor Events\\localization\\french",
	# 	"english",
	# 	"french"
	# )
	translate_all_files(indir, outdir, "FR")
