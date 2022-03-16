# DO NOT USE THIS DIRECTLY AS A SCRIPT.
# This script is used in automated workflow.

import nbformat as nbf

with open("/home/patel_zeel/probml-notebooks/notebooks-d2l/batchnorm_torch.ipynb") as f:
    data = nbf.read(f, nbf.NO_CONVERT)
    if data["cells"][0]["metadata"]["id"] == "view-in-github":
        data["cells"].pop(0)

with open(
    "/home/patel_zeel/probml-notebooks/notebooks-d2l/batchnorm_torch.ipynb", "w"
) as f:
    nbf.write(data, f)

pass
