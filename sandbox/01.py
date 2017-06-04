from pylib.geom.mbr import MBR

box = MBR(0, 0, 0, 0)
box.expand_include_xy(2, 2)
print box