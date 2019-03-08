"""Utils for visualizing artifice output. (Mostly for testing).
"""

import matplotlib.pyplot as plt
import numpy as np
import logging

logger = logging.getLogger('artifice')

def plot_image(*images, columns=10, ticks=False):
  columns = min(columns, len(images))
  rows = max(1, len(images) // columns)
  fig, axes = plt.subplots(rows,columns, squeeze=False,
                           figsize=(columns/2, rows/2))
  for i, image in enumerate(images):
    ax = axes[i // columns, i % columns]
    im = ax.imshow(np.squeeze(image), cmap='magma', vmin=0., vmax=1.)

  if not ticks:
    for ax in axes.ravel():
      ax.axis('off')
      ax.set_aspect('equal')

  fig.subplots_adjust(wspace=0, hspace=0)  

def plot_encodings(encodings, labels=None, num_classes=10):
  xs = encodings[:,0]
  ys = encodings[:,1]
  plt.figure()
  if labels is None:
    plt.plot(xs, ys, 'b.')
  else:
    for i in range(num_classes):
      plt.plot(xs[labels == i], ys[labels == i], f'C{i}.', label=str(i))
    plt.legend()
  plt.title("Latent Space Encodings")
  
def show_image(*images, **kwargs):
  plot_image(*images, **kwargs)
  plt.show()

def show_encodings(encodings, **kwargs):
  plot_encodings(encodings, **kwargs)
  plt.show()


