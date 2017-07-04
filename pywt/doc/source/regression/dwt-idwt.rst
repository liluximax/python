.. _reg-dwt-idwt:

.. currentmodule:: pywt

DWT and IDWT
============

Discrete Wavelet Transform
--------------------------

Let's do a :func:`Discrete Wavelet Transform <dwt>` of a sample data ``x``
using the ``db2`` wavelet. It's simple..

    >>> import pywt
    >>> x = [3, 7, 1, 1, -2, 5, 4, 6]
    >>> cA, cD = pywt.dwt(x, 'db2')

And the approximation and details coefficients are in ``cA`` and ``cD``
respectively:

    >>> print(cA)
    [ 5.65685425  7.39923721  0.22414387  3.33677403  7.77817459]
    >>> print(cD)
    [-2.44948974 -1.60368225 -4.44140056 -0.41361256  1.22474487]

Inverse Discrete Wavelet Transform
----------------------------------

Now let's do an opposite operation
- :func:`Inverse Discrete Wavelet Transform <idwt>`:

    >>> print(pywt.idwt(cA, cD, 'db2'))
    [ 3.  7.  1.  1. -2.  5.  4.  6.]

Voilà! That's it!

More Examples
-------------

Now let's experiment with the :func:`dwt` some more. For example let's pass a
:class:`Wavelet` object instead of the wavelet name and specify signal
extension mode (the default is :ref:`symmetric <Modes.symmetric>`) for the
border effect handling:

    >>> w = pywt.Wavelet('sym3')
    >>> cA, cD = pywt.dwt(x, wavelet=w, mode='constant')
    >>> print(cA)
    [ 4.38354585  3.80302657  7.31813271 -0.58565539  4.09727044  7.81994027]
    >>> print(cD)
    [-1.33068221 -2.78795192 -3.16825651 -0.67715519 -0.09722957 -0.07045258]

Note that the output coefficients arrays length depends not only on the input
data length but also on the :class:Wavelet type (particularly on its
:attr:`filters length <~Wavelet.dec_len>` that are used in the transformation).

To find out what will be the output data size use the :func:`dwt_coeff_len`
function:

    >>> # int() is for normalizing Python integers and long integers for documentation tests
    >>> int(pywt.dwt_coeff_len(data_len=len(x), filter_len=w.dec_len, mode='symmetric'))
    6
    >>> int(pywt.dwt_coeff_len(len(x), w, 'symmetric'))
    6
    >>> len(cA)
    6

Looks fine. (And if you expected that the output length would be a half of the
input data length, well, that's the trade-off that allows for the perfect
reconstruction...).

The third argument of the :func:`dwt_coeff_len` is the already mentioned signal
extension mode (please refer to the PyWavelets' documentation for the
:ref:`modes <modes>` description). Currently there are six
:ref:`extension modes <Modes>` available:

    >>> pywt.Modes.modes
    ['zero', 'constant', 'symmetric', 'periodic', 'smooth', 'periodization', 'reflect']

As you see in the above example, the :ref:`periodization <Modes.periodization>`
(periodization) mode is slightly different from the others. It's aim when
doing the :func:`DWT <dwt>` transform is to output coefficients arrays that
are half of the length of the input data.

Knowing that, you should never mix the periodization mode with other modes when
doing :func:`DWT <dwt>` and :func:`IDWT <idwt>`. Otherwise, it will produce
**invalid results**:

    >>> x
    [3, 7, 1, 1, -2, 5, 4, 6]
    >>> cA, cD = pywt.dwt(x, wavelet=w, mode='periodization')
    >>> print(pywt.idwt(cA, cD, 'sym3', 'symmetric')) # invalid mode
    [ 1.  1. -2.  5.]
    >>> print(pywt.idwt(cA, cD, 'sym3', 'periodization'))
    [ 3.  7.  1.  1. -2.  5.  4.  6.]


Tips & tricks
-------------

Passing ``None`` instead of coefficients data to :func:`idwt`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Now some tips & tricks. Passing ``None`` as one of the coefficient arrays
parameters is similar to passing a *zero-filled* array. The results are simply
the same:

    >>> print(pywt.idwt([1,2,0,1], None, 'db2', 'symmetric'))
    [ 1.19006969  1.54362308  0.44828774 -0.25881905  0.48296291  0.8365163 ]

    >>> print(pywt.idwt([1, 2, 0, 1], [0, 0, 0, 0], 'db2', 'symmetric'))
    [ 1.19006969  1.54362308  0.44828774 -0.25881905  0.48296291  0.8365163 ]

    >>> print(pywt.idwt(None, [1, 2, 0, 1], 'db2', 'symmetric'))
    [ 0.57769726 -0.93125065  1.67303261 -0.96592583 -0.12940952 -0.22414387]

    >>> print(pywt.idwt([0, 0, 0, 0], [1, 2, 0, 1], 'db2', 'symmetric'))
    [ 0.57769726 -0.93125065  1.67303261 -0.96592583 -0.12940952 -0.22414387]

Remember that only one argument at a time can be ``None``:

    >>> print(pywt.idwt(None, None, 'db2', 'symmetric'))
    Traceback (most recent call last):
    ...
    ValueError: At least one coefficient parameter must be specified.


Coefficients data size in :attr:`idwt`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When doing the :func:`IDWT <idwt>` transform, usually the coefficient arrays
must have the same size.

    >>> print(pywt.idwt([1, 2, 3, 4, 5], [1, 2, 3, 4], 'db2', 'symmetric'))
    Traceback (most recent call last):
    ...
    ValueError: Coefficients arrays must have the same size.


Not every coefficient array can be used in :func:`IDWT <idwt>`. In the
following example the :func:`idwt` will fail because the input arrays are
invalid - they couldn't be created as a result of :func:`DWT <dwt>`, because
the minimal output length for dwt using ``db4`` wavelet and the :ref:`symmetric
<Modes.symmetric>` mode is ``4``, not ``3``:

    >>> pywt.idwt([1,2,4], [4,1,3], 'db4', 'symmetric')
    Traceback (most recent call last):
    ...
    ValueError: Invalid coefficient arrays length for specified wavelet. Wavelet and mode must be the same as used for decomposition.

    >>> int(pywt.dwt_coeff_len(1, pywt.Wavelet('db4').dec_len, 'symmetric'))
    4
