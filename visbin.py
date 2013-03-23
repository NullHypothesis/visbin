#!/usr/bin/env python
#
# Copyright 2013 by Philipp Winter <phw@riseup.net>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from scapy import *
from PIL import Image
import sys

DIM = 50

if not (len(sys.argv) == 2):
	print >>sys.stderr, "\nUsage: %s FILE\n" % sys.argv[0]
	sys.exit(1)

with open(sys.argv[1], "r") as fd:
	data = fd.read()
fd.close()

if len(data) < (DIM * DIM):
	print >>sys.stderr, "Missing %d byte(s) of data." % (DIM**2 - len(data))
	sys.exit(1)

imgSize = DIM, DIM

img = Image.new('RGB', imgSize, (255,255,255))
putpixel = img.im.putpixel

ctr = 0
for x in range(0, DIM):
	for y in range(0, DIM):
		v = ord(data[ctr])
		putpixel((x, y), (v, v, v))
		ctr += 1

img.save("%s.png" % sys.argv[1])
