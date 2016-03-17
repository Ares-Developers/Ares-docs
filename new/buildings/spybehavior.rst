Spy Behavior
~~~~~~~~~~~~

:game:`Yuri's Revenge` only permits a Spy to achieve one effect on infiltrating,
which is determined by a hard-coded order of precedence. Spy infiltration logic
has been rewritten in :game:`Ares` to be more flexible, including some new
effects that a Spy can achieve.

All of the following flags default to :value:`no` or :value:`0`.

.. versionadded:: 0.1

:tagdef:`[BuildingType]SpyEffect.Custom=boolean`
  Whether or not to use the :game:`Ares` spy infiltration logic instead of the
  original :game:`Yuri's Revenge` logic.

.. note:: Must be set to :value:`yes` for any of the following effects to
  work...

.. index:: Spy behaviour; Multiple effects can be achieved on a single building.


Radar
`````

:tagdef:`[BuildingType]SpyEffect.ResetRadar=boolean`
  Whether or not spying this enemy building will cause the normal radar sabotage
  behavior (i.e. re-shrouding the enemy's map down to just the terrain that they
  can presently see).
:tagdef:`[BuildingType]SpyEffect.RevealRadar=boolean`
  **NEW EFFECT** Whether or not spying this enemy radar will reveal to you, the
  infiltrator, all of the terrain that they, the enemy, have thus far explored.
  The building must also have :tag:`Radar=yes` set.
:tagdef:`[BuildingType]SpyEffect.KeepRadar=boolean`
  **NEW EFFECT** If enabled, a player infiltrating this building will still have
  access to the owning player's radar even if the building is destroyed, sold or
  captured. Otherwise the spy effect is removed. Requires
  :tag:`SpyEffect.RevealRadar=yes` and a :tag:`Radar=yes` building.

.. index Spy behaviour; New effect: Reveal radar (shows you what the enemy can see).


Power
`````

:tagdef:`[BuildingType]SpyEffect.PowerOutageDuration=integer - frames`
  The number of frames for which the enemy's power will be sabotaged (i.e.
  temporarily reduced to zero).

.. index:: Spy behaviour; Per-building power outage duration.



Money
`````

:tagdef:`[BuildingType]SpyEffect.StolenMoneyAmount=integer - credits`
  **NEW EFFECT** The amount of credits that will be stolen from the enemy upon
  spying this enemy building.
  
  The amount of money ultimately stolen from the enemy is always capped by the
  amount of money they presently have (i.e. if
  :tag:`SpyEffect.StolenMoneyAmount=500` but the enemy only has 200 credits then
  you will only gain 200 credits from spying the building).
:tagdef:`[BuildingType]SpyEffect.StolenMoneyPercentage=float - multiplier`
  The percentage of the enemy's current credits that will be stolen from the
  enemy upon spying this enemy building. Only has an effect if
  :tag:`SpyEffect.StolenMoneyAmount=0`.

.. index:: Spy behaviour; New effect: Steal money amount (steals a set amount of
  money rather than a percentage).
  
.. index:: Spy behaviour; Per-building steal money percentage.


Super Weapons
`````````````

:tagdef:`[BuildingType]SpyEffect.ResetSuperweapons=boolean`
  Whether or not spying this enemy building will cause all super weapons
  attached to it (:tag:`SuperWeapon`, :tag:`SuperWeapon2`, :tag:`SuperWeapons`
  and all super weapons on attached upgrades) to have their countdown timers
  restarted.

.. index:: Spy behaviour; Reset all super weapons provided by a building


The following tags can be used to grant super weapons like the Sonar Pulse in
:game:`Red Alert` when a spy infiltrates a Sub Pen.

:tagdef:`[BuildingType]SpyEffect.SuperWeapon=SuperWeaponType`
  **NEW EFFECT** Grants this super weapon when infiltrating an enemy building of
  this type.

  .. note:: Not all super weapon types might be supported.

:tagdef:`[BuildingType]SpyEffect.SuperWeaponPermanent=boolean`
  Whether the granted super weapon will become available permanently. If
  :value:`yes`, it will become available uncharged, and it won't be lost once
  fired. Otherwise, the super weapon will become available pre-charged but
  disappear again after being fired once. Defaults to :value:`no`.

.. versionadded:: 0.B

.. index:: Spy behaviour; Grant one-time or permanent super weapon


.. _`spybehavior-stolentech`:

Stolen Technology
`````````````````

:tagdef:`[BuildingType]SpyEffect.StolenTechIndex= list of integers`
  The stealable technology types that is stolen upon spying this enemy building.
  Only values from 0 to 31 (inclusive) are supported. Use :value:`-1` to
  disable the effect. Defaults to :value:`-1`.

  .. note:: Note that despite its singular name this tag takes a list of
    integers and it is thus possible to steal several technology types when
    infiltrating a single building.

:tagdef:`[TechnoType]Prerequisite.StolenTechs=list of integers`
  The list of stealable technology types that must be stolen before this object
  can be built. Only values from 0 to 31 (inclusive) are supported. Use
  :value:`-1` to disable this requirement. Defaults to :value:`-1`.

In :game:`Yuri's Revenge`, there were only three types of stealable technology
available and these were hard-coded to specific buildings.

+ Spying :tag:`[GATECH]` satisfies :tag:`RequiresStolenAlliedTech=yes`
+ Spying :tag:`[NATECH]` satisfies :tag:`RequiresStolenSovietTech=yes`
+ Spying :tag:`[YATECH]` satisfies :tag:`RequiresStolenThirdTech=yes`

In :game:`Ares`, spying a building with :tag:`SpyEffect.StolenTechIndex=2` (for
example) satisfies the stolen tech requirements for units that require stolen
tech 2.

.. note:: If you set :tag:`SpyEffect.Custom=yes` on  :tag:`[GATECH]`,
  \ :tag:`[NATECH]` or :tag:`[YATECH]` then those buildings will no longer
  satisfy the old :tag:`RequiresStolen*Tech` flags.

.. index:: Spy behaviour; New effect: Stolen tech index (multiple new stolen techs).

.. versionchanged:: 0.B



Factories
`````````

:tagdef:`[BuildingType]SpyEffect.UnitVeterancy=boolean`
  Whether or not spying this enemy factory will make all future units you build
  from your own factories of the same type start veteran. For example, spying an
  enemy barracks with :tag:`SpyEffect.UnitVeterancy=yes` set will cause all
  future :type:`InfantryTypes` that you build to start veteran.
  
  .. note:: This only works for :type:`VehicleType` and :type:`InfantryType`
    factories at present. Also note that infiltrating any :type:`VehicleType`
    factory (i.e. War Factory or Naval Yard) will only make land vehicles start
    veteran - Naval vehicles cannot be made to start veteran through spy
    infiltration logic.
:tagdef:`[BuildingType]SpyEffect.RevealProduction=boolean`
  **NEW EFFECT** Whether or not spying this enemy factory will allow you to see
  what the enemy is presently building from that factory. Once the building has
  been spied, select the building and the cameo of the unit that is being
  produced will be displayed over the building.

.. image:: /images/production_spying.png
  :alt: Screenshot of a current production being revealed
  :align: center

.. index:: Spy behaviour; New effect: Reveal production cameo (shows you what the enemy are currently building).


Reverse Engineering
```````````````````

For a spy effect to reset a player's build options gained by reverse
engineering, see :doc:`/new/reverseengineerlogic`.
