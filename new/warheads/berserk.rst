Berserk
=======

.. index::
  TechnoType; Reloading time multiplier when berserking
  Berserk; Reloading time multiplier

Reloading Time Modifier
-----------------------

Units under the effect of Chaos Gas or other :tag:`Psychedelic=yes` warheads go
berserk, which reduces their willingness to obey orders as well as their
reloading time. This reloading time factor can be customized globally and for
each :type:`TechnoType`.

:tagdef:`[CombatDamage]BerserkROFMultiplier=float - multiplier`
  The multiplier applied to the reloading time when a unit is berserking.
  Smaller means shorter reloading and faster firing. Defaults to :value:`0.5`.

:tagdef:`[TechnoType]Berserk.ROFMultiplier=float - multiplier`
  The multiplier applied when this unit is berserking. Smaller means faster
  firing. Defaults to :tag:`[CombatDamage]BerserkROFMultiplier`.

.. versionadded:: 0.8


.. index::
  TechnoType; Immunity to Berserk
  Berserk; Immunity

Immunity to Berserk
-------------------

The tag :tag:`ImmuneToPsionics` is determines whether a unit or structure is
susceptible to mind control and :tag:`Psychedelic=yes` weapons. If the object is
immune to one, it is immune to the other. :game:`Ares` allows to differentiate.

:tagdef:`[TechnoType]ImmuneToBerserk=boolean`
  Whether this object is immune to berserking, the Chaos Gas effect. Can be used
  to override :tag:`ImmuneToPsionics` and the PSIONICSIMMUNE ability. If set to
  :value:`yes`, the object is not affected by Chaos Gas even if not
  :tag:`ImmuneToPsionics=yes`; if set to :value:`no`, the object can be affected
  by Chaos Gas despite maybe being immune to psionics.

  If not set, acts as if set to :value:`yes` if :tag:`ImmuneToPsionics=yes` or
  the object gained the :value:`PSIONICSIMMUNE` ability through veterancy,
  otherwise as if set to :value:`no`.

  .. note:: Currently, the default of not being set cannot be restored once this
    tag has been set.

.. versionadded:: 2.0
