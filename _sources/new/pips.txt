Pips
~~~~

In :game:`Yuri's Revenge`, the values that were accepted for :tag:`Pip` and
:tag:`OccupyPip` were hardcoded to a list of known names. While fixing the
:doc:`Pip Distortion Bug </bugfixes/type1/pipdistortionbug>`, :game:`Ares` makes
this more flexible.

Any tag that defines a pip accepts an alternative notation now. If the tag value
cannot be resolved using the list of known names (like :value:`personblue`), the
value is parsed as integer. The integers are used as frame index into the pips
files (:file:`pips.shp` and :file:`pips2.shp`).

If the value is neither a known name nor an integer, a parsing error is put into
:file:`debug.log`.

:tagdef:`[TechnoType]Pip=integer`
  Frame index in the pips file to use as pip image. Valid values range from
  :value:`0` to the pip file's frame count - 1.

  .. note:: If the tag is read as integer and the value is out of bounds, no
    error is logged in :file:`debug.log`. 

.. index:: Pips; User-defined pips.

.. versionadded:: 0.4
