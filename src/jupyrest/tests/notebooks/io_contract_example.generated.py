# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.1
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown]
# # SAMPLE NOTEBOOK
# This is a sample notebook to demonstrate how to define input/output contracts for a notebook and how to save outputs within a notebook.
#
#

# %% tags=["parameters"]
foo = "foo"
bar = 500
baz = "baz"

# %%
print(f"foo={foo}, bar={bar}, baz={baz}")

# %%
import json

data = [
    {
        "red": foo,
        "green": bar,
        "blue": baz
    },
    {
        "red": baz,
        "green": bar,
        "blue": foo
    }
]

# %%
data

# %%
from jupyrest import save_output
save_output(json.dumps(data))
