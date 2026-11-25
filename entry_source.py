import os

TEXT = "I still hear the screen door slap shut behind me as I ran barefoot down the warm concrete steps, a melting orange popsicle dripping down my wrist, while Dad's radio played through the kitchen window and Mom called that dinner was almost ready."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
