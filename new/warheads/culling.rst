.. index::
  Warheads; Culling effect for ordinary warheads
  Culling; Supported on ordinary warheads

:captiontag:`Culling`
`````````````````````

With :game:`Ares` the culling effect used by naval parasites like Squids can
also be applied to conventional warheads. Culling is responsibile for dealing a
deadly blow once the victim is below a certain health percentage.

:tagdef:`[Warhead]Culling.RookieBelowHealth=integer - percentage`

:tagdef:`[Warhead]Culling.VeteranBelowHealth=integer - percentage`

:tagdef:`[Warhead]Culling.EliteBelowHealth=integer - percentage`
  The health a victim unit must fall below to be culled by a hit using this
  warhead. Use :value:`1` to :value:`100` to represent percentages of full
  health; use :value:`0`, :value:`-1`, and :value:`-2` to represent health
  states critical/red, damaged/yellow, and healthy/green respectively.
  Requires :tag:`Culling=yes`.

  Defaults to :value:`0` for :tag:`Culling.RookieBelowHealth` and
  :tag:`Culling.VeteranBelowHealth`, to :value:`-1` for
  :tag:`Culling.EliteBelowHealth`.

  The default is the behavior of parasites with :tag:`Culling=yes`: They cull
  units with critical health if the firer is rookie or veteran, and also cull
  damaged units (yellow) if firer is elite.


:tagdef:`[Warhead]Culling.Chance=integer - percentage`

:tagdef:`[Warhead]Culling.RookieChance=integer - percentage`

:tagdef:`[Warhead]Culling.VeteranChance=integer - percentage`

:tagdef:`[Warhead]Culling.EliteChance=integer - percentage`
  The chance that a cullable unit is actually culled by a hit using this
  warhead. Requires :tag:`Culling=yes`. Defaults to :value:`100` (always).

  Use :tag:`Culling.Chance` to set the chance for all veterancy levels.

  .. note:: This chance is applied every time damage is dealt using this
    warhead, not once per victim. That means with :value:`70` there is a 70%
    chance of culling on the first hit, and a 91% chance of culling the unit
    on the second hit.

.. versionadded:: 3.0
