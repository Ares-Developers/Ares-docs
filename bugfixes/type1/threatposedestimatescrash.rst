.. index:: House; Out of bounds write could corrupt memory

================================================
Out of Bounds Array Access Could Lead to Crashes
================================================

Under certain conditions the game would use invalid cell coordinates to write to
items in an array. This lead to out of bound writes that corrupted memory and
lead to crashes. Whether this could cause desynchronisations is not known. This
error has been fixed.

.. versionadded:: 0.9
