import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as colors 
import matplotlib.colors as mlc
import string
from matplotlib.patches import Patch
from matplotlib.lines import Line2D

marker = None
def draw_graph():
    global mine, img , x_mine, y_mine, value, im, fig,ax
    clr = [(1, 1, 1), '#0a3563', '#1592ad'] # white and two shades of blue

    # custom legends
    elment = [Patch(facecolor='#1592ad', edgecolor ='#1592ad', label ='Surface Mine'),
            Patch(facecolor='#0a3563', edgecolor ='#0a3563', label ='Buried Mine'),
            Line2D([0], [0], marker='o', label='Robot', markersize=10,  linewidth=0)]

    # axis labels
    x_axis =  string.ascii_uppercase[:19] 
    y_axis = [str(i) for i in range(19, 0, -1)]

    mine =  np.zeros((19,19)) # buried, surface or no mine
    img =  np.zeros((19,19), dtype=float) #values of the cmap/ the colors (0.0,1.0,2.0)

    #initialize coordinates and mine state
    x_mine= '' #(A-S)
    y_mine= 0  #(1-19)
    value = 0  # 0- no mines , 1- buried mine, 2- surface mine


    cmap = mlc.LinearSegmentedColormap.from_list('ColorMap', clr)
    norm = colors.BoundaryNorm([0, 1, 2, 3], cmap.N)
    fig, ax = plt.subplots()
    im = ax.imshow(img, cmap=cmap, norm =  norm)

    # Show all ticks and label them with the respective list entries
    # ax.spines[:].set_visible(False)
    ax.set_xticks(np.arange(len(x_axis)), labels=x_axis)
    ax.set_yticks(np.arange(len(y_axis)), labels=y_axis)
    ax.set_xticks(np.arange(len(x_axis))-.5, minor=True)
    ax.set_yticks(np.arange(len(y_axis))-.5, minor=True)
    ax.grid(which="minor", color="k", linestyle='-', linewidth=0.1)
    ax.tick_params(which="minor", bottom=False, left=False)

    plt.legend(handles = elment, loc = 'upper left',bbox_to_anchor=(1,1))
    ax.set_title("Mines Map Representation")
    fig.tight_layout()
    
    plt.ion() #interactive mode, the window will not block the execution of the script
    plt.show(block=False) # show the graph without blocking the script
    
def update_mine():
    global marker
    x_mine = input("Enter x coordinate (A-S): ")
    y_mine = input("Enter y coordinate (1-19): ")
    value = input("Enter mine state (0-2): ")
    x_mine = ord(x_mine) - 65
    y_mine = 19 - int(y_mine)
    mine[y_mine][x_mine] = int(value) #x and y are inverted
    x_robot, y_robot = input("enter robot coordinates(char, int):").split(',')
    
    if marker:  # Check if marker exists
        marker.remove()
    x_robot = ord(x_robot) - 65
    y_robot = 19 - int(y_robot)
    marker = plt.plot(x_robot,y_robot, linestyle='None', marker = 'o', color='#1592ad')[0]
    
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
