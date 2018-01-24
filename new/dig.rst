.. index::
  Subterranean; Dig animations and sounds
  Units; Subterranean dig animations and sounds
  Art; Dig animations and sounds per type

Dig Animation and Sound
~~~~~~~~~~~~~~~~~~~~~~~

The global settings :tag:`Dig` and :tag:`DigSound` have been deglobalized and
split into separate tags for units with Tunnel locomotors for digging into
the surface and emerging from the ground again.

:tagdef:`[TechnoType]DigIn=animation`
  The optional animation used when this unit digs into the ground. Defaults to
  :tag:`[AudioVisual]Dig`.

:tagdef:`[TechnoType]DigOut=animation`
  The optional animation used when this unit digs out of the ground. Defaults to
  :tag:`[AudioVisual]Dig`.

:tagdef:`[TechnoType]DigInSound=sound entry`
  The optional sound played when this unit digs into the ground. Defaults to
  :tag:`[AudioVisual]DigSound`.

:tagdef:`[TechnoType]DigOutSound=sound entry`
  The optional sound played when this unit digs out of the ground. Defaults to
  :tag:`[AudioVisual]DigSound`.

.. versionadded:: 0.D
