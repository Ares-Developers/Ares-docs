Tiberium Damage
```````````````

Infantry being damaged when walking on tiberium (not just standing there) is a
feature of :game:`Tiberian Dawn` and :game:`Tiberian Sun`. :game:`Ares` brings
this feature back and extends it to work with all unit types.

Units killed by Tiberium Damage may convert into a Visceroid. See
:ref:`Visceroids <visceroids>`

.. index: Tiberium; Damage units moving over tiberium.

.. versionadded:: 0.5


Enabling Tiberium Damage
------------------------

:game:`Ares` requires a new tag to be set to enable the Damage feature, and it
does no longer damage units that are positioned above
:tag:`[General]HoverHeight`.

:tagdef:`[General]TiberiumDamageEnabled=boolean`
  Whether tiberium damages units that are not tiberium proof. Required for the
  following tags to work. Defaults to :value:`no`.


Who gets damaged
----------------

All units that are not tiberium proof (neither through the tag
:tag:`TiberiumProof` nor through the :value:`TIBERIUM_PROOF` veteran ability)
will be damaged when entering a cell containing tiberium. It does not matter how
long they stay in a cell.

:tagdef:`[TechnoType]TiberiumProof=boolean`
  Whether this unit is immune to tiberium damage. Defaults to :value:`no` for
  :type:`InfantryTypes`, to :value:`yes` otherwise.


Damage and Warhead
------------------

The damage and the warhead used to deliver it can be customized for each of the
:type:`Tiberiums`.

:tagdef:`[Tiberium]Damage=integer`
  The damage a unit that is not tiberium proof receives from entering a cell
  containing this type of Tiberium. Defaults to :value:`Power / 10`, but at
  least :value:`1`.

:tagdef:`[Tiberium]Warhead=warhead`
  The warhead that deals the Tiberium Damage. Defaults to
  :tag:`[CombatDamage]C4Warhead`.

  .. note:: This is not used for the Tiberium Explosive feature.


.. _visceroids:

Visceroids
``````````

Visceroids have been recreated partially.

They will move around the map, and when two units with :tag:`SmallVisceroid=yes`
(not :tag:`[General]SmallVisceroid`) meet, they will merge into a unit of type
:tag:`[General]LargeVisceroid`.

.. note:: Visceroids will not yet retreat to a patch of tiberium to regenerate
  health when badly damaged.

When units die because of Tiberium Damage, there is a chance they will spawn a
unit of type :tag:`[General]SmallVisceroid` (if defined). This logic requires
:tag:`[Basic]TiberiumDeathToVisceroid=yes` in a map to work. The Visceroid is
owned by the country :value:`Neutral`. 

:game:`Ares` adds a global tag that can be customized for each type. The global
tag existed since :game:`Tiberian Sun` but did not do anything.

:tagdef:`[General]TiberiumTransmogrify=integer - percent`
  Chance of which a unit dying of tiberium damage transforms into a
  :tag:`[General]SmallVisceroid`. Defaults to :value:`0`.

:tagdef:`[TechnoType]TiberiumTransmogrify=integer - percent`
  Chance of which a unit of this type dying of tiberium damage transforms into a
  :tag:`[General]SmallVisceroid`. Defaults to
  :tag:`[General]TiberiumTransmogrify`.

.. index: Tiberium; Visceroids.

.. versionadded:: 0.5
