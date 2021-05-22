import glob
import os
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--indir", "-i", type=str, default="indir")
    parser.add_argument("--outdir", "-o", type=str, default="outdir")
    parser.add_argument("--startno", "-s", type=int, default=0)
    args = parser.parse_args()

    os.makedirs(args.outdir, exist_ok=True)

    search_path = os.path.join(args.indir, "**", "*.jpg")
    files = glob.glob(search_path, recursive=True)

    for i, old_name in enumerate(files):
        new_name = os.path.join(args.outdir, "img_{0:05d}.jpg".format(args.startno + i))
        os.rename(old_name, new_name)
        print(old_name + " -> " + new_name)
