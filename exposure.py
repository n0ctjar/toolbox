"""night exposure helper. the 500 rule, roughly."""

# what i actually use on walks. higher iso = more noise, my sensor hates 6400
ISO_NOTES = {
    800: "clean, needs a tripod",
    1600: "fine for streets",
    3200: "ok if there's a streetlight",
    6400: "pigeons only",
}

def max_shutter(focal_mm, crop=1.0):
    return round(500 / (focal_mm * crop), 1)

if __name__ == "__main__":
    f = float(input("focal length (mm): "))
    c = float(input("crop factor (1.5 for my camera): ") or 1.5)
    print("max shutter:", max_shutter(f, c), "seconds")
    for iso, note in ISO_NOTES.items():
        print(f"  iso {iso}: {note}")
