.. index::
  Terrain; Forest fires
  Universe; Forest fires

Forest Fires
~~~~~~~~~~~~

Forest fires were a feature of :game:`Tiberian Sun`. Trees were set on fire if
hit by a :tag:`Sparky=yes` warhead. While burning, they could ignite trees
nearby and thus over time spread like a wildfire.

:game:`Ares`'s implementation of forest fires slightly differs from the one in
:game:`Tiberian Sun`. It is now required to also set the previously unused tag
:tag:`IsFlammable=yes` on each tree that may be set on fire. This is the only
noticeable change.

See `Sparky on ModEnc <http://modenc.renegadeprojects.com/Sparky>`_ for a more
detailed description of the logic, and for the requirements to get it working.
To prevent crashes when firing a :tag:`Sparky=yes` warhead, do not forget to set
three valid animations as :tag:`[AudioVisual]OnFire` and two valid animations as
:tag:`[AudioVisual]TreeFire`.

.. note:: If trees are not burning down, make sure that the animation used as
  \ :tag:`[AudioVisual]SmallFire` has :tag:`Scorch=no` set.

.. versionadded:: 0.8
