#!/usr/bin/env python3

import os
import glob
from pathlib import Path

max_recent = 5

download_dir = str(Path.home()) + "/Downloads/*"
files = glob.glob(download_dir)
files.sort(key=os.path.getctime, reverse=True)

count = max_recent if len(files) > max_recent else len(files)

print("Downloads")
print("---")
print("Downloads | iconName=folder-symbolic href='file://"
      + download_dir + "'")
i = 0
while (i < count):
    print(os.path.basename(files[i]) + " | " + "href='file://" + files[i]
          + "'")
    i = i + 1
