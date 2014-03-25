Sight
~~~~~

:tag:`Sight` was using a lookup table almost like :tag:`CellSpread`, thus it was
limited to a maximum value of 10. :game:`Ares` increases this and now larger
values can be used.

.. warning:: For performance reasons, :tag:`Sight` values larger than 10 should
  be used judiciously. It is not designed for full map reveal.

.. note:: Using larger :tag:`Sight` values will result in a distinct octagonal
  shaped field of view. That is how :tag:`CellSpread` logic works and thus no
  bug. The logic used for :tag:`Sight` values larger than 10 might change in the
  future.

.. index:: Sight; Values larger than 10 are possible.

.. versionadded:: 0.6
