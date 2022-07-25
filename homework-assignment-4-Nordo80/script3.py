import shutil
from hurry.filesize import size
from hurry.filesize import alternative

def drive_size(drive):
  total, used, free = shutil.disk_usage(drive)
  print("Total: " + size(total, system = alternative))
  print("Used: " + size(used, system = alternative))
  print("Free: " + size(free, system = alternative))
drive_size("/")
