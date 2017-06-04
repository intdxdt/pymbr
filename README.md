# mbr-py
Minimum bounding box operations in python

# example
```py
box = MBR(0, 0, 0, 0)
box.expand_include_xy(2, 2)
print box  # POLYGON ((0 0, 0 2, 2 2, 2 0, 0 0))
```

# lic
MIT