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

.. index:: Units; Customizable dig animations and sounds

.. versionadded:: 0.D
