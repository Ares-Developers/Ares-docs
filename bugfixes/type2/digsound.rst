.. index:: Super Weapons; Nuke super weapons can be overridden to use a sound other than DigSound for their siren.

========
DigSound
========

``[AudioVisual]`` |>| ``DigSound`` is used for both the global Nuke siren and
the sound made when a subterranean unit (with
``Locomotor={4A582743-9839-11d1-B709-00A024DDAFD1}``) digs into or
emerges from the ground. With Ares, the super weapon can specify its
own ``SW.ActivationSound`` (which defaults to ``[AudioVisual]`` |>| ``DigSound``
for nukes).

.. versionadded:: 0.1
