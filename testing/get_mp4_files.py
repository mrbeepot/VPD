from pathlib import Path
import sys
#
pathList = Path("../dataset/videos/").glob("**/*.mp4")
print(type(pathList))
# print(len(list(pathList)))
for path in pathList:
	# print(str(path))
	print(path.stem)
# for x in range(10):
#     # sys.stdout.write('\r')
#     # sys.stdout.write(str(x))
#     # sys.stdout.flush()
#     print(str(x))
