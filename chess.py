import matplotlib.pyplot as plt

chess = [
    [10,0,10,0,10,0,10,0,10,0,10],
    [0,10,0,10,0,10,0,10,0,10,0],
    [10,0,10,0,10,0,10,0,10,0,10],
    [0,10,0,10,0,10,0,10,0,10,0],
    [10,0,10,0,10,0,10,0,10,0,10],
    [0,10,0,10,0,10,0,10,0,10,0],
    [10,0,10,0,10,0,10,0,10,0,10],
]

plt.imshow(chess,cmap="grey")
plt.show()