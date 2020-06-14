#!/usr/bin/python

import matplotlib as mpl
mpl.use("AGG")

from pylab import *

#mpl.use("PDF")

R=10

def b(l, c, y, x, xy, sz = 12, r = 0, fs = "full", prp = {"ha":"left", "va":"bottom"}, m="o"):
	plot(xy[0] + array(x), xy[1] + array(y), '-' + m, color = c,
		linewidth = 3, markersize = sz, fillstyle = fs)
	text(xy[0] + x[-1], xy[1] + y[-1], "  " + l,
		prp, fontsize = sz, rotation = r)

if __name__ == "__main__":
	figure(1, figsize=(45, 8))
	L = range(10, 7, -1)
	F = (40, 20, 14)
	
	xy = [0,0]
	text(xy[0], xy[1] + L[0], "git", fontsize=F[0])

	xy = [-4,0]
	text(xy[0], xy[1] + L[1], "init", fontsize=F[1])
	text(xy[0], xy[1] + L[2], ".", fontsize=20)
	b("*master", "grey", (0,), (0,), xy, fs = "none")

	xy[0] += 4
	text(xy[0], xy[1] + L[1], "clone", fontsize=F[1])
	text(xy[0], xy[1] + L[2], "https://github.com/\n  pmamonov/git-cs", fontsize=10)
	b("origin/b1", "red", (2,3), (0,1), xy, r = 90)
	b("origin/b2", "blue", (2,3), (0,2), xy, r = 90)
	b("*master, origin/master", "green", (0,1,2,3), (0,0,0,0), xy, r=90)

	xy[0] += 4
	text(xy[0], xy[1] + L[1], "branch -a", fontsize=F[1])
	text(xy[0], xy[1] + 7, """
* master
  origin/master
  origin/b1
  origin/b2
""", {"ha":"left", "va":"top"}, fontsize=F[2], family="monospace")
	b("*master, origin/master", "green", (0,1,2,3), (0,0,0,0), xy)

	xy[0] += 4
	text(xy[0], xy[1] + L[1], "checkout [-b]", fontsize=F[1])
	text(xy[0], xy[1] + L[2], "b1", fontsize=F[2])
	text(xy[0], xy[1] + 7, """
  master
* b1
  origin/master
  origin/b1
  origin/b2
""", {"ha":"left", "va":"top"}, fontsize=F[2], family="monospace", color="grey")
	b("*b1", "red", (2,3), (0,1), xy)
	b("", "green", (0,1,2,), (0,0,0), xy)

	xy[0] += 4
	text(xy[0], xy[1] + L[1], "add [-p]", fontsize=F[1])
	text(xy[0], xy[1] + L[2], "file", fontsize=F[2])
	b("", "orange", (3, 4), (1,1), xy)
	b("*b1", "red", (2,3), (0,1), xy)
	b("", "green", (0,1,2,), (0,0,0), xy)

	xy[0] += 4
	text(xy[0], xy[1] + L[1], "status, diff", fontsize=F[1])
	text(xy[0], xy[1] + L[2], "[ file ]", fontsize=F[2])
	b("?", "orange", (3, 4), (1,1), xy)
	b("*b1", "red", (2,3), (0,1), xy)
	b("", "green", (0,1,2,), (0,0,0), xy)

	xy[0] += 4
	text(xy[0], xy[1] + L[1], "commit", fontsize=F[1])
	text(xy[0], xy[1] + L[2], "[ file | . ]", fontsize=F[2])
	b("*b1", "red", (2,3,4), (0,1,1), xy)
	b("", "green", (0,1,2,), (0,0,0), xy)

	xy[0] += 4
	text(xy[0], xy[1] + L[1], "cherry-pick", fontsize=F[1])
	text(xy[0], xy[1] + L[2], "origin/b2", fontsize=F[2])
	b("origin/b2", "blue", (2,3), (0,2), xy, r=90)
	b("*b1", "blue", (4,5), (1,1), xy)
	b("", "red", (2,3,4), (0,1,1), xy)
	b("", "green", (0,1,2,), (0,0,0), xy)

	xy[0] += 4
	text(xy[0], xy[1] + L[1], "rebase [-i]", fontsize=F[1])
	text(xy[0], xy[1] + L[2], "master", fontsize=F[2])
	b("*b1", "blue", (5,6), (1,1), xy)
	b("", "red", (2,3,4), (0,1,1), xy, m="-.")
	b("", "red", (3,4,5), (0,1,1), xy)
	b("master", "green", (0,1,2,3), (0,0,0,0), xy, r=90)

	xy[0] += 4
	text(xy[0], xy[1] + L[1], "revert", fontsize=F[1])
	text(xy[0], xy[1] + L[2], "HEAD", fontsize=F[2])
	b("*b1, HEAD", "yellow", (6,7), (1,1), xy)
	text(xy[0], xy[1] + 7, "-1", fontsize=F[2], color="red")
	b("HEAD^", "blue", (5,6), (1,1), xy)
	text(xy[0], xy[1] + 6, "+1", fontsize=F[2], color="green")
	b("", "red", (3,4), (0,1,), xy)
	b("HEAD^^", "red", (4,5), (1,1), xy)
	b("", "green", (0,1,2,3), (0,0,0,0), xy)

	xy[0] += 4
	text(xy[0], xy[1] + L[1], "reset [--hard]", fontsize=F[1])
	text(xy[0], xy[1] + L[2], "HEAD^^", fontsize=F[2])
	b("", "grey", (5,6,7), (1,1,1), xy, m = "X")
	b("*b1", "red", (3,4,5), (0,1,1), xy)
	b("", "green", (0,1,2,3), (0,0,0,0), xy)

	xy[0] += 4
	text(xy[0], xy[1] + L[1], "log", fontsize=F[1])
	text(xy[0], xy[1] + L[2], "[b1]", fontsize=F[2])
	b("*b1, 9c0a6867c5", "red", (4,5), (0,0), xy)
	b("54ee43f497", "red", (3,4), (0,0), xy)
	b("e71241d3fd", "green", (2,3), (0,0), xy)
	b("62ecea94ff", "green", (1,2), (0,0), xy)
	b("a71c7178cb", "green", (0,1), (0,0), xy)
	b("457ce19651", "green", (0,), (0,), xy)

	xy[0] += 4
	text(xy[0], xy[1] + L[1], "show", fontsize=F[1])
	text(xy[0], xy[1] + L[2], "[b1 | HEAD | 9c0a... ]", fontsize=12)
	b("9c0a6867c5", "red", (5,), (0,), xy)
	text(xy[0], xy[1] + 5, """
commit 9c0a...
Author: ...
Date:   ...

    change 1 line

--- a/file
+++ b/file
@@ -1,4 +1,4 @@ func(x)

    context
-   delete line
+   add line
    context
""", {"ha":"left", "va":"top"}, fontsize=10, family="monospace")

	xy[0] += 4
	text(xy[0], xy[1] + L[1], "fetch", fontsize=F[1])
	text(xy[0], xy[1] + L[2], "[origin]", fontsize=F[2])
	b("*b1", "red", (3,4,5), (0,1,1), xy)
	b("origin/master", "lightgreen", (3,4), (0,0), xy, r=90)
	b("origin/b1", "red", (2,3), (0,1), xy, r = 45)
	b("origin/b2", "blue", (2,3), (0,2), xy, r = 45)
	b("master  ", "green", (0,1,2,3), (0,0,0,0), xy, prp = {"ha":"right", "va":"bottom"}, r=-45)

	xy[0] += 4
	text(xy[0], xy[1] + L[1], "push [--force]", fontsize=F[1])
	text(xy[0], xy[1] + L[2], "origin b1:b1", fontsize=F[2])
	b("*b1, origin/b1", "red", (3,4,5), (0,1,1), xy)
	b("origin/master", "lightgreen", (3,4), (0,0), xy, r=90)
	b("origin/b2", "blue", (2,3), (0,2), xy)
	b("master", "green", (0,1,2,3), (0,0,0,0), xy)


	ylim(-1,11)
	axis("off")
	savefig("git-cs.png", bbox_inches="tight")
