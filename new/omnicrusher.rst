:captiontag:`OmniCrusher` Enhancements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:tag:`OmniCrusher=yes` units are allowed to overrun enemies, and units are eager
to try that when ordered to attack a victim, or when retaliating against an
enemy unit firing at it. This mechanism is sometimes useful, but sometimes it is
not. Like when a Battle Fortress deliberately closes in on a group of enemy
tanks, and is then lured into an ambush and overpowered itself.

:game:`Ares` allows to deactivate the agressive behavior.

:tagdef:`[TechnoType]OmniCrusher.Aggressive=boolean`
  Whether or not a unit should try to crush its target aggressively. If
  :value:`no`, the unit will not try to come as close as possible to the target
  to finally crush it. Requires :tag:`OmniCrusher=yes`. Defaults to :tag:`yes`.

  .. note:: Only supported if :tag:`OmniCrusher=yes` is set. The default might
    change in a later version.

.. index:: Crush; OmniCrusher=yes without aggressive auto-crushing

.. versionadded:: 0.A
