#IMPORTS
from PIL import Image
from info import functions as f
#FUNCTIONS
def colour(path, max):
    img = Image.open(path).convert("RGBA")
    colors = img.getcolors(max)
    colorlst = [f"#{color[1][0]:02x}{color[1][1]:02x}{color[1][2]:02x}" for color in colors]
    numlst = [color[0] for color in colors]
    return colorlst, numlst
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
def run(path,max=100000000):
    color,num = colour(path,max)
    dict_ = {color[i]:num[i] for i in range(len(num))}
    sorteddict = sorted(dict_.items(), key=lambda x:x[1])
    final = dict(sorteddict)
    return final
#MAINLOOP
for colour_ in list(run("info/image.png").keys()):
    try:
        exec("f."+colour_.replace("#","")+'()')
    except:
        continue
