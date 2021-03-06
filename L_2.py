import matplotlib.pyplot as opt, matplotlib.animation as animation, pathlib, random as rd
from Main import dl, intrs, animate, get_y

data = open(str(pathlib.Path(__file__).parent.absolute())+"\Data.txt","w")
otr_s = ((-3, 3), (3, 3))
line_1 = dl(otr_s[0][0], otr_s[0][1], otr_s[1][0], otr_s[1][1])
line_2 = dl(otr_s[0][0], otr_s[0][1], otr_s[1][0]-8, otr_s[1][1]-8)
#lrand, rrand = rd.randint(-8, -1), rd.randint(1, 8)
lrand, rrand = -1, 1
rp_1, rp_2 = (lrand, get_y(lrand, line_2)), (rrand, get_y(rrand, line_2))
point_1 = ((lrand+rrand)/2, get_y((lrand+rrand)/2, line_2))
otr_1 = ((otr_s[0][0], point_1[0]), (otr_s[1][0], point_1[1]))
otr_2 = ((otr_s[0][1], rp_1[0]), (otr_s[1][1], rp_1[1]))
point_2 = intrs(otr_1, otr_2)
line_3 = dl(rp_2[0], point_2[0], rp_2[1], point_2[1])
point_3 = intrs(line_1, line_3)
data.write("l "+str(line_1)+'\n')
data.write("o "+str(otr_s)+'\n')
data.write("l "+str(line_2)+'\n')
data.write("p "+str(rp_1)+'\n'+"p "+str(rp_2)+'\n'+"p "+str(point_1)+'\n')
data.write("o "+str(otr_1)+'\n'+"o "+str(otr_2)+'\n')
data.write("p "+str(point_2)+'\n')
data.write("l "+str(line_3)+'\n')
data.write("p "+str(point_3)+'\n')
data.write("p "+str((otr_s[0][1], otr_s[1][1]))+'\n')
data.close()
fig = opt.figure()
AnI = animation.FuncAnimation(fig, animate, interval=1000)
opt.xlim(-10, 10)
opt.ylim(-10, 10)
opt.grid()
opt.show()