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
