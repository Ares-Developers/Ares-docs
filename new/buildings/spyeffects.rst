.. index:: Spies; Multiple effects on a single building

Spy Effects
~~~~~~~~~~~

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



.. index:: Spies; Show what the enemy can see

Radar
`````

:tagdef:`[BuildingType]SpyEffect.ResetRadar=boolean`
  Whether or not spying this enemy building will cause the normal radar sabotage
  behavior (i.e. re-shrouding the enemy's map down to just the terrain that they
  can presently see).
:tagdef:`[BuildingType]SpyEffect.RevealRadar=boolean`
  **NEW EFFECT** Whether or not spying this enemy radar will reveal all further
  unit movements to the infiltrating player. Enemy units will then scout the map
  like own units until the infiltrated building is destroyed, sold, or captured.
  The building must also have :tag:`Radar=yes` set.
:tagdef:`[BuildingType]SpyEffect.KeepRadar=boolean`
  **NEW EFFECT** If enabled, a player infiltrating this building will still have
  access to the owning player's radar even if the building is destroyed, sold,
  or captured. Otherwise the spy effect is removed. Requires
  :tag:`SpyEffect.RevealRadar=yes` and a :tag:`Radar=yes` building.



.. index:: Spies; Create power outage

Power
`````

:tagdef:`[BuildingType]SpyEffect.PowerOutageDuration=integer - frames`
  The number of frames for which the enemy's power will be sabotaged (i.e.
  temporarily reduced to zero).



.. index:: Spies; Steal fixed amount or percentage of money

Money
`````

The amount of money ultimately stolen from the enemy is always capped by the
amount of money they presently have.

:tagdef:`[BuildingType]SpyEffect.StolenMoneyPercentage=float - percentage`
  The percentage of the enemy's current credits that will be stolen from the
  enemy upon spying this enemy building. Defaults to :value:`0%`.
:tagdef:`[BuildingType]SpyEffect.StolenMoneyAmount=integer - credits`
  **NEW EFFECT** The fixed amount of credits that will be stolen from the enemy
  upon spying this enemy building. Defaults to :value:`0`.

  If used together with :tag:`SpyEffect.StolenMoneyPercentage`, this defines the
  maximum amount of money to steal.

  .. quickstart:: If you want to express "Take three quarters of the enemy's
    money, but no more than 10,000 credits", use both tags:
    \ :tag:`SpyEffect.StolenMoneyPercentage=75%` and
    \ :tag:`SpyEffect.StolenMoneyAmount=10000`.



.. index::
  Spies; Reset all super weapons a building provides
  Spies; Grant one-time or permanent super weapon

Super Weapons
`````````````

:tagdef:`[BuildingType]SpyEffect.ResetSuperweapons=boolean`
  Whether or not spying this enemy building will cause all super weapons
  attached to it (:tag:`SuperWeapon`, :tag:`SuperWeapon2`, :tag:`SuperWeapons`
  and all super weapons on attached upgrades) to have their countdown timers
  restarted.


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



.. _`spybehavior-stolentech`:

.. index:: Spies; Grant multiple stolen techs

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
available and these were hard-coded to the first three buildings in the
:tag:`[AI]BuildTech` list (game defaults given in parens):

+ Spying the first (:tag:`GATECH`) satisfies :tag:`RequiresStolenAlliedTech=yes`
+ Spying the second (:tag:`NATECH`) satisfies :tag:`RequiresStolenSovietTech=yes`
+ Spying the third (:tag:`YATECH`) satisfies :tag:`RequiresStolenThirdTech=yes`

In :game:`Ares`, spying a building with :tag:`SpyEffect.StolenTechIndex=2` (for
example) satisfies the stolen tech requirements for units that require stolen
tech 2.

.. note:: If you set :tag:`SpyEffect.Custom=yes` on buildings in the
  \ :tag:`BuildTech` list (like :tag:`GATECH`, :tag:`NATECH` or :tag:`YATECH`),
  then those buildings will no longer satisfy the old :tag:`RequiresStolen*Tech`
  flags.

.. versionchanged:: 0.B



.. index:: Spies; Build vehicles or train infantry as veteran
.. index:: Spies; Veteran buildings or aircraft or navy

Veterancy
`````````

:game:`Ares` adds five independent fine grained controls to gain veterancy by
spying, thus it is possible to grant one or more types veterancy at the same
time where the original game only supported either :type:`InfantryType`\ s or
:type:`VehicleType`\ s depending on the :tag:`Factory=` setting.

:tagdef:`[BuildingType]SpyEffect.InfantryVeterancy=boolean`
  Whether spying this building will make all future infantry with
  :tag:`Trainable=yes` you build from your own factories start veteran. Defaults
  to :value:`no`.

:tagdef:`[BuildingType]SpyEffect.VehicleVeterancy=boolean`
  Whether spying this building will make all future :tag:`Naval=no` vehicles
  with :tag:`Trainable=yes` you build from your own factories start veteran.
  Defaults to :value:`no`.

:tagdef:`[BuildingType]SpyEffect.NavalVeterancy=boolean`
  **NEW EFFECT** Whether spying this building will make all future
  :tag:`Naval=yes` vehicles with :tag:`Trainable=yes` you build from your own
  factories start veteran. Defaults to :value:`no`.

:tagdef:`[BuildingType]SpyEffect.AircraftVeterancy=boolean`
  **NEW EFFECT** Whether spying this building will make all future aircraft with
  :tag:`Trainable=yes` you build from your own factories start veteran.
  Defaults to :value:`no`.

:tagdef:`[BuildingType]SpyEffect.BuildingVeterancy=boolean`
  **NEW EFFECT** Whether spying this building will make all future buildings
  with :tag:`Trainable=yes` you build from your own Construction Yards start
  veteran. Defaults to :value:`no`.

.. versionadded:: 0.1
.. versionchanged:: 2.0



.. _`spybehavior-revealproduction`:

.. index:: single: Spies; Reveal production, money, or power

Intelligence
````````````

:tagdef:`[BuildingType]SpyEffect.RevealProduction=boolean`
  **NEW EFFECT** Whether or not spying this enemy building will allow you to see
  what the enemy is presently building from that factory, or the power output,
  or the owning player's money. Once the building has been spied, select the
  building and the information of the unit that is being produced will be
  displayed over the building.

  * :tag:`Fake=yes` buildings will show the text :value:`TXT_FAKE` and reveal
    their true name in tooltips (see :doc:`EnemyUIName </new/enemyuiname>`)
  * :tag:`Power` greater than :value:`0` buildings will reveal the power level
    (formatted using :value:`TXT_POWER_DRAIN2`)
  * :tag:`Storage` greater than :value:`0` buildings will see the player's
    credits (formatted using :value:`TXT_MONEY_FORMAT_1`)
  * :tag:`Factory` buildings will reveal the cameo of the current production

  .. note:: Observers have been enabled to always have access to this
    information.

.. image:: /images/production_spying.png
  :alt: Screenshot of a current production being revealed
  :align: center

.. versionchanged:: 0.B



.. _`spybehavior-unreverse`:

.. index:: single: Spies; Reset all reverse engineered build options

Reverse Engineering
```````````````````

Reset a player's build options gained by :doc:`Reverse Engineering
</new/reverseengineerlogic>`.

:tagdef:`[BuildingType]SpyEffect.UndoReverseEngineer=boolean`
  **NEW EFFECT** Whether spying this building will remove all technology the
  infiltrated player has reverse-engineered so far. Defaults to :value:`no`.

.. versionadded:: 0.2



.. index:: single: Spies; Demolish infiltrated building

Sabotage
````````

:tagdef:`[BuildingType]SpyEffect.SabotageDelay=integer - frames`
  The number of frames after which the building will be demolished as if C4 had
  been planted. If negative, :tag:`[CombatDamage]C4Delay` is used. Use
  :value:`0` to disable. Defaults to :value:`0`.

.. versionadded:: 0.E
