"""night exposure helper. the 500 rule, roughly."""

def max_shutter(focal_mm, crop=1.0):
    return 500 / (focal_mm * crop)

if __name__ == "__main__":
    f = float(input("focal length (mm): "))
    print("max shutter:", max_shutter(f), "seconds")
