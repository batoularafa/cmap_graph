import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as colors 
import matplotlib.colors as mlc
import string
from matplotlib.patches import Patch
##markers
# x = [5]
# y = [6]

# plt.plot(x, y, linestyle='None', marker='o')

# plt.show()


def draw_graph():
    global mine, img , x_coord, y_coord, value, im, fig
    clr = [(1, 1, 1), '#0a3563', '#1592ad'] # white and two shades of blue

    # custom legends
    elment = [Patch(facecolor='#1592ad', edgecolor ='#1592ad', label ='Surface Mine'),
            Patch(facecolor='#0a3563', edgecolor ='#0a3563', label ='Buried Mine')]

    # axis labels
    y_axis = []
    x_axis =  string.ascii_uppercase[:19] 
    for i in range(19,0,-1):
        y_axis.append(str(i))

    mine =  np.zeros((19,19)) # buried, surface or no mine
    img =  np.zeros((19,19), dtype=float) #values of the cmap/ the colors (0.0,1.0,2.0)

    #initialize coordinates and mine state
    x_coord= 0 #(1-19)
    y_coord= '' #(A-S)
    value = 0  # 0- no mines , 1- buried mine, 2- surface mine

    cmap = mlc.LinearSegmentedColormap.from_list('ColorMap', clr)
    norm = colors.BoundaryNorm([0, 1, 2, 3], cmap.N)
    fig, ax = plt.subplots()
    im = ax.imshow(img, cmap=cmap, norm =  norm)

    # Show all ticks and label them with the respective list entries
    ax.spines[:].set_visible(False)
    ax.set_xticks(np.arange(len(x_axis)), labels=x_axis)
    ax.set_yticks(np.arange(len(y_axis)), labels=y_axis)
    ax.set_xticks(np.arange(len(x_axis))-.5, minor=True)
    ax.set_yticks(np.arange(len(y_axis))-.5, minor=True)
    ax.grid(which="minor", color="k", linestyle='-', linewidth=0.1)
    ax.tick_params(which="minor", bottom=False, left=False)

    plt.legend(handles = elment, loc = 'upper left',bbox_to_anchor=(1,1))
    ax.set_title("Mines Map Representation")
    fig.tight_layout()

    plt.ion() #interative mode, the window will not block the execution of the script
    plt.show(block=False) # show the graph without blocking the script

def update_mine():
    x_coord = input("Enter x coordinate (1-19): ")
    y_coord = input("Enter y coordinate (A-S): ")
    value = input("Enter mine state (0-2): ")
    x_coord = 19 - int(x_coord)
    y_coord = ord(y_coord) - 65
    mine[x_coord][y_coord] = int(value)
    for i in range(19):
        for j in range(19):
            if mine[i][j] == 0:
                img[i][j]=0.0  #  (first color) >> white
            elif mine[i][j] ==1:
                img[i][j]=1.0 # (second color) >> dark blue
            else:
                img[i][j]=2.0  # (third color)
    im.set_data(img) # update the data of the img array 
    fig.canvas.draw_idle #redraw the graph

if __name__ == "__main__":
    draw_graph()
    while True:
        update_mine()