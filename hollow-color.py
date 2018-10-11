from __future__ import division
import matplotlib.pyplot as plt
import numpy as np


def sample_hollow_lamina(size, outer_width, outer_height, a, b, inner_width, inner_height):
    """
    (a, b) is the lower-left corner of the "hollow".
    """
    llcorners = np.array([[0, 0], [a, 0], [a+inner_width, 0],
                          [0, b], [a+inner_width, b],
                          [0, b+inner_height], [a, b+inner_height], [a+inner_width, b+inner_height]])
    top_height = outer_height - (b + inner_height)
    right_width = outer_width - (a + inner_width)
    widths = np.array([a, inner_width, right_width, a, right_width, a, inner_width, right_width])
    heights = np.array([b, b, b, inner_height, inner_height, top_height, top_height, top_height])
    areas = widths * heights
    shapes = np.column_stack((widths, heights))

    regions = np.random.multinomial(size, areas/areas.sum())
    indices = np.repeat(range(8), regions)
    unit_coords = np.random.random(size=(size, 2))
    pts = unit_coords * shapes[indices] + llcorners[indices]

    return pts
pts = sample_hollow_lamina(2000, 3, 3, 0.5, 1.0, 1.5, 0.5)
print pts
plt.plot(pts[:,0], pts[:,1], 'o', alpha=0.75)
plt.show()
#plt.grid()
