from tensorflow.keras import activations

"""Documentation strings for latens.
"""

description = """\
Latens. An Unsupervised Learning approach to active learning.
"""

command_choices = ['debug', 'train', 'predict', 'convert']
command_help = "latens command to run."

input_help = """Name or names of data files."""

l2_reg_help = """L2 regularization factor. Default is None."""

output_help = """Command output. Default is 'show'."""

model_path_help = """Prefix for saved model path. Default (None) doesn't save
the model. Required for prediction."""

overwrite_help = """overwrite model if it exists"""

image_shape_help = """Shape of the image. Must be 3D. Grayscale uses 1 for last
dimension. Default is '28 28 1' for mnist."""

epochs_help = """Number of training epochs. Default is 1."""

num_components_help = """Number of components in the low-dimensional
representation. Default is 10."""

eval_secs_help = """Evaluate model every EVAL_SECS during training. Default is
1200."""

eval_mins_help = """See EVAL_SECS. Default is 20 minutes (1200 seconds)"""

splits_help = """Number of examples to use for splits on the dataset. Must
define at least two splits for training and validation sets. Default is '60000
10000' for MNIST."""

cores_help = """Number of CPU cores to use when parallelizing. Default, -1,
parallelizes across all visible processors."""

batch_size_help = """Batch size for training. Default is 16."""

dropout_help = """Dropout rate for the representational layer. Default is 0.1"""

activation_choices = {'sigmoid' : activations.sigmoid}

activation_help = """Activation function to use at the representational
layer. Default is sigmoid. (Other layers use relu)."""

learning_rate_help = """Learning rate for training. Default is 0.01"""

momentum_help = """Momentum for the momentum optimizer. Default is 0.9"""
