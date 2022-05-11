import glob
import os
counter=0
os.makedirs("new_images",exist_ok=True)
for img in sorted(glob.glob("images/*")):
    os.rename(img,"new_images/"+str(counter)+".png")
    counter+=1