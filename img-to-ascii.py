from PIL import Image

def asciiConvert(source: str, destination: str, scale: float):
    img = Image.open(source)
    w, h = img.size

    w = max(1, int(w / scale))
    h = max(1, int(h / scale))
    
    img = img.resize((w, h))
    w, h = img.size

    grid = [["X"] * w for _ in range(h)]

    pix = img.load()

    for y in range(h):
        for x in range(w):
            brightness = sum(pix[x, y])
            if brightness == 0:
                grid[y][x] = "#"
            elif brightness in range(1, 100):
                grid[y][x] = "X"
            elif brightness in range(100, 200):
                grid[y][x] = "%"
            elif brightness in range(200, 300):
                grid[y][x] = "&"
            elif brightness in range(300, 400):
                grid[y][x] = "*"
            elif brightness in range(400, 500):
                grid[y][x] = "+"
            elif brightness in range(500, 600):
                grid[y][x] ="/"
            else:
                grid[y][x] = " "
    
    with open(destination + ".txt", "w") as f:
        for row in grid:
            f.write("".join(row) + "\n")

if __name__ == "__main__":
    source: str = input("Enter the file name: ")
    destination: str = input("Enter the name of output: ")
    scale: float = float((input("Enter the scale of image to work on:")))
    while (scale < 1 or scale > 4):
        print("It is recommended to have a scale between 1 and 4!\n")
        scale: float = float(input("Enter the scale of image to work on:"))

    asciiConvert(source, destination, scale)
