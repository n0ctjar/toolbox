"""night exposure helper. the 500 rule, roughly."""

def max_shutter(focal_mm, crop=1.0):
    return round(500 / (focal_mm * crop), 1)

if __name__ == "__main__":
    f = float(input("focal length (mm): "))
    c = float(input("crop factor (1.5 for my camera): ") or 1.5)
    print("max shutter:", max_shutter(f, c), "seconds")
