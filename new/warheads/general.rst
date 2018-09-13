General Settings
~~~~~~~~~~~~~~~~

.. index:: Warheads; AffectsEnemies= added as counterpart for AffectsAllies=

:captiontag:`AffectsEnemies`
````````````````````````````

:tagdef:`[Warhead]AffectsEnemies=boolean`
  Specifies whether or not this warhead can damage enemy units. This has no
  effect on the warhead's ability to target enemy units. A counterpart to the
  existing :tag:`AffectsAllies` flag.

.. versionadded:: 0.1


.. index:: Warheads; AffectsOwner= split from AffectsAllies=

:captiontag:`AffectsOwner`
``````````````````````````

:tagdef:`[Warhead]AffectsOwner=boolean`
  Whether this warhead can affect the very player who fired it. Defaults to
  :tag:`AffectsAllies` flag.

.. versionadded:: 2.0


.. index::
  Warheads; Effects without damage
  Warheads; Effects requiring damage

.. _wh-effects:

Warhead Effects
```````````````

The effects KillDriver, Sonar, Disable Weapon and Flashing can be applied
independently of conventional damage.

:tagdef:`[Warhead]EffectsRequireDamage=boolean`
  Whether warheads will only apply the effects if at least one hitpoint of
  damage has actually been dealt to a unit or structure. If :value:`no`, effects
  are also applied if the no damage is dealt. Requires positive damage; healing
  does not use this setting. Defaults to :value:`no`.

:tagdef:`[Warhead]EffectsRequireVerses=boolean`
  Whether :tag:`Verses` needs to be greater than :value:`0%` for the warhead to
  apply effects. Can be used to distinguish between :value:`0%` and greater
  verses that potentially nullify damage, between immunity and vulnerability. If
  :value:`no`, effects are applied to any unit or structure regardless of
  verses. Defaults to :value:`yes`.

.. versionadded:: 2.0


.. index:: Warheads; No conventional damage

Non-Damaging Warheads
`````````````````````

This can be used to punctually disable an optimization in the game to still
apply warhead effects without doing damage. By default, :game:`Yuri's Revenge`
checks whether no damage is to be dealt before expensively determining which
units and structures are in range.

:tagdef:`[Warhead]AllowZeroDamage=boolean`
  Whether damage of 0 hitpoints will still be passed on to all units and
  structures affected by the warhead. Otherwise, a damage of 0 will not be
  passed on. Defaults to :value:`no`.

.. versionadded:: 2.0


.. index::
  Warheads; Suppress EVA's "Ore miner under attack" warnings
  EVA; Suppress "Ore miner under attack" warnings per warhead

Non-Malicious Warheads
``````````````````````

:tagdef:`[Warhead]Malicious=boolean`
  Specifies whether or not EVA should notify an ore miner's owner of an attack
  (:value:`EVA_OreMinerUnderAttack`). No other EVA messages are suppressed. For
  example, if a warhead's purpose is to spread ore dealing damage as a side
  effect only you can use :tag:`Malicious=no` to disable unreasonable EVA attack
  warnings for ore miners. Defaults to :value:`yes`.

.. versionadded:: 0.2


Prevent scattering
``````````````````

A unit hit by a warhead might scatter on impact. This tag on the attacking
warhead prevents this.

:tagdef:`[Warhead]PreventScatter=boolean`
  Whether units should not scatter when attacked with this warhead even if they
  have the ability to. Defaults to :value:`no`.

.. versionadded:: 0.7
