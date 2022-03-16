# DO NOT USE THIS DIRECTLY AS A SCRIPT.
# This script is used in automated workflow.

import nbformat as nbf


def remove_colab_link(filename):
    with open(filename, "r") as f:
        data = nbf.read(f, nbf.NO_CONVERT)
        if data["cells"][0]["metadata"]["id"] == "view-in-github":
            data["cells"].pop(0)

    with open(filename, "w") as f:
        nbf.write(data, f)
