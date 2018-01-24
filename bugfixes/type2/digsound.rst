.. index::
  Super Weapons; Nukes can be overridden to not use global DigSound for their siren
  Subterranean; Nuke super weapons using DigSound for their siren

======================
:captiontag:`DigSound`
======================

:tag:`[AudioVisual]DigSound` is used for both the global Nuke siren and the
sound made when a subterranean unit (with
:tag:`Locomotor={4A582743-9839-11d1-B709-00A024DDAFD1}`) digs into or emerges
from the ground. With :game:`Ares`, the super weapon can specify its own
:tag:`SW.ActivationSound` (which defaults to :tag:`[AudioVisual]DigSound`
for nukes).

.. versionadded:: 0.1
