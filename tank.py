from PIL import Image
import sys
import numpy as np


def main(argv):
    if len(argv) != 4:
        print("Error")
        pass

    image_white = np.array(Image.open(argv[1]).convert("L"))
    image_black = np.array(Image.open(argv[2]).convert("L"))
    image_black = image_black * 0.3

    a = 255.0 + image_black - image_white
    g = 255.0 / a * image_black
    g[g == np.inf] = 255.0
    g.clip(0, 255)
    a.clip(0, 255)

    a = np.round(a, 0).astype("ubyte")
    g = np.round(g, 0).astype("ubyte")

    print("amax:%d gmax%d amin:%d gmin:%d" % (a.max(), g.max(), a.min(), g.min()))

    result = np.dstack([g, g, g, a])

    print(result.shape)

    im = Image.fromarray(result, "RGBA")

    im.save(argv[3], "PNG")
    im.show()


if __name__ == '__main__':
    main(sys.argv)
