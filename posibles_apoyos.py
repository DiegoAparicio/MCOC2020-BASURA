from numpy import loadtxt

def ver_apoyos(xy):
    import matplotlib.pylab as plt
    plt.figure()
    plt.plot(xy[:,0], xy[:,1],"--.",color="#B49158")
    for i, (x, y) in enumerate(xy):
        plt.text(x, y, f"{i}", 
            verticalalignment="center",
            horizontalalignment="center")

    plt.xlabel("X (m)")
    plt.ylabel("Z (m)")
    plt.show()


posibles_apoyos = loadtxt("coordenadas_apoyos.txt")
visualizar = True


if visualizar:
    ver_apoyos(posibles_apoyos)