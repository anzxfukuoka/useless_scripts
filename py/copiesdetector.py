import os
import sys

def get_duplicates(dir):
	unique = []
	copies = []

	tmp = []

	filelist = os.listdir(dir)
	filelist.reverse()

	for fn in filelist:
		if os.path.isdir(dir + fn):
			continue
		f = open(dir + fn, "rb")
		data = f.read()
		fh = hash(data)
		f.close()

		if fh not in tmp:
			tmp.append(fh)
			unique.append(fn)#unique.append([fn, fh])
		else:
			copies.append(fn)#copies.append([fn, fh])


	return {"unique": unique, "copies": copies}

if __name__ == "__main__": 
	print(sys.argv)
	if len(sys.argv) == 2:
		path = sys.argv[1] + "/"
	else:
		path = input("path to dir: ") + "/"
	#print(get_duplicates(path))
	files = get_duplicates(path)

	if len(files["copies"]) == 0:
		print("no copies.")
		sys.exit(0)

	print("unique files:")
	for f in files["unique"]:
		print("	" + f)
	print("copies:")
	for f in files["copies"]:
		print("	" + f)
	

	ok = input("delete copies?(y/n)")
	if ok.lower() == "y":
		for f in files["copies"]:
			os.remove(path + f)
		print("copies deleted.")
	elif ok.lower() == "n":
		sys.exit(0)
	else:
		print("err")
		sys.exit(0)
