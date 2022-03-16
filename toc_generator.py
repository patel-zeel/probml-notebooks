from glob import glob
from colab_remover import remove_colab_link

files = glob("*/*.ipynb")
# print(files)


def parse_labels():
    labels = set()
    for file in files:
        label = file.split("/")[0]
        labels.add(label)
    return sorted(labels)


with open("_toc.yml", "w") as f:
    f.write("format: jb-book\n")
    f.write("root: intro\n")
    f.write("parts:\n")
    labels = parse_labels()
    for label in labels:
        f.write(f"  - caption: {label}\n")
        f.write(f"    chapters:\n")
        for file in sorted(files):
            if file.startswith(label + "/"):
                f.write(f"      - file: {file.replace('.ipynb','')}\n")
                remove_colab_link(file)  # First cell must contain title.
                print(file, "added")
