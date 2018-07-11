import tensorflow as tf
import warnings

from distutils.version import LooseVersion


def reduce_function(op_func, input_tensor, axis=None, keepdims=None,
                    name=None, reduction_indices=None):
    """
    Handler function for Tensorflow depreciation of keep_dims for tf 1.8
    and above, but tf 1.4 requires keep_dims
    :param op_func: expects the function to handle eg: tf.reduce_sum.
    :param input_tensor: The tensor to reduce. Should have numeric type.
    :param axis: The dimensions to reduce. If None (the default),
            reduces all dimensions. Must be in the range
            [-rank(input_tensor), rank(input_tensor)).
    :param keepdims: If true, retains reduced dimensions with length 1.
    :param name: A name for the operation (optional).
    :param reduction_indices: The old (deprecated) name for axis.
    :param keep_dims: Deprecated alias for keepdims.
    :return: outputs same value as op_func.
    """

    if LooseVersion(tf.__version__) < LooseVersion('1.8.0'):
        warning = "Running on tensorflow version " + \
                   LooseVersion(tf.__version__).vstring + \
                   ". This version will not be supported by CleverHans" + \
                   "in the future."
        warnings.warn(warning)
        out = op_func(input_tensor, axis=axis,
                      keep_dims=keepdims, name=name,
                      reduction_indices=reduction_indices)
    else:
        out = op_func(input_tensor, axis=axis,
                      keepdims=keepdims, name=name,
                      reduction_indices=reduction_indices)
    return out


def reduce_sum(input_tensor, axis=None, keepdims=None,
               name=None, reduction_indices=None):
    """
    Wrapper around the tf.reduce_sum to handle argument keep_dims
    """
    return reduce_function(tf.reduce_sum, input_tensor, axis=axis,
                           keepdims=keepdims, name=name,
                           reduction_indices=reduction_indices)


def reduce_max(input_tensor, axis=None, keepdims=None,
               name=None, reduction_indices=None):
    """
    Wrapper around the tf.reduce_max to handle argument keep_dims
    """
    return reduce_function(tf.reduce_max, input_tensor, axis=axis,
                           keepdims=keepdims, name=name,
                           reduction_indices=reduction_indices)


def reduce_min(input_tensor, axis=None, keepdims=None,
               name=None, reduction_indices=None):
    """
    Wrapper around the tf.reduce_min to handle argument keep_dims
    """
    return reduce_function(tf.reduce_min, input_tensor, axis=axis,
                           keepdims=keepdims, name=name,
                           reduction_indices=reduction_indices)


def reduce_mean(input_tensor, axis=None, keepdims=None,
                name=None, reduction_indices=None):
    """
    Wrapper around the tf.reduce_mean to handle argument keep_dims
    """
    return reduce_function(tf.reduce_mean, input_tensor, axis=axis,
                           keepdims=keepdims, name=name,
                           reduction_indices=reduction_indices)


def reduce_any(input_tensor, axis=None, keepdims=None,
               name=None, reduction_indices=None):
    """
    Wrapper around the tf.reduce_any to handle argument keep_dims
    """
    return reduce_function(tf.reduce_any, input_tensor, axis=axis,
                           keepdims=keepdims, name=name,
                           reduction_indices=reduction_indices)
