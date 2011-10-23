Spy Behavior
~~~~~~~~~~~~

Yuri's Revenge only permits a Spy to achieve one effect on
infiltrating, which is determined by a hard-coded order of precedence.
Spy infiltration logic has been rewritten in Ares to be more flexible,
including some new effects that a Spy can achieve.

All of the following flags default to no or zero.

:[BuildingType]SpyEffect.Custom= (boolean): Whether or not to use the
  Ares spy infiltration logic instead of the original Yuri's Revenge
  logic. SpyEffect.Custom=


NB: Must be set to yes for any of the following effects to work... Spy
behaviour: Multiple effects can be achieved on a single building.



Radar
`````

:[BuildingType]SpyEffect.ResetRadar= (boolean): Whether or not spying
  this enemy building will cause the normal radar sabotage behavior
  (i.e. re-shrouding the enemy's map down to just the terrain that they
  can presently see). SpyEffect.ResetRadar=
:[BuildingType]SpyEffect.RevealRadar= (boolean) *NEW EFFECT*: Whether
  or not spying this enemy radar will reveal to you, the infiltrator,
  all of the terrain that they, the enemy, have thus far explored. The
  building must also have `Radar=yes` set. New effect: Reveal radar
  (shows you what the enemy can see). SpyEffect.RevealRadar=




Power
`````

:[BuildingType]SpyEffect.PowerOutageDuration= (integer - frames): The
  number of frames for which the enemy's power will be sabotaged (i.e.
  temporarily reduced to zero). Per-building power outage duration.
  SpyEffect.PowerOutageDuration=




Money
`````

:[BuildingType]SpyEffect.StolenMoneyAmount= (integer - credits) *NEW
  EFFECT*: The amount of credits that will be stolen from the enemy upon
  spying this enemy building. New effect: Steal money amount (steals a
  set amount of money rather than a percentage).
  SpyEffect.StolenMoneyAmount=
:[BuildingType]SpyEffect.StolenMoneyPercentage= (float - multiplier):
  The percentage of the enemy's current credits that will be stolen from
  the enemy upon spying this enemy building. Only has an effect if
  `SpyEffect.StolenMoneyAmount=0`. The amount of money ultimately stolen
  from the enemy is always capped by the amount of money they presently
  have (i.e. if `SpyEffect.StolenMoneyAmount=500` but the enemy only has
  200 credits then you will only gain 200 credits from spying the
  building). Per-building steal money percentage.
  SpyEffect.StolenMoneyPercentage=




Super Weapons
`````````````

:[BuildingType]SpyEffect.ResetSuperweapons= (boolean): Whether or not
  spying this enemy building will cause all super weapons attached to it
  (SuperWeapon, SuperWeapon2 and all super weapons on attached upgrades)
  to have their countdown timers restarted. SpyEffect.ResetSuperweapons=




Stolen Technology
`````````````````

:[BuildingType]SpyEffect.StolenTechIndex= (integer): The stealable
  technology type that is stolen upon spying this enemy building. New
  effect: Stolen tech index (multiple new stolen techs).
  SpyEffect.StolenTechIndex=
:[TechnoType]Prerequisite.StolenTechs= (list of integers): The list of
  stealable technology types that must be stolen before this object can
  be built. SpyEffect.StolenTechs=


In Yuri's Revenge, there were only three types of stealable technology
available and these were hard-coded to specific buildings.
Spying `[GATECH]` satisfies `RequiresStolenAlliedTech=yes`
Spying `[NATECH]` satisfies `RequiresStolenSovietTech=yes`
Spying `[YATECH]` satisfies `RequiresStolenThirdTech=yes`
In Ares, spying a building with `SpyEffect.StolenTechIndex=2` (for
example) satisfies the stolen tech requirements for units that require
stolen tech 2.
NB: If you set `SpyEffect.Custom=yes` on GATECH, NATECH or YATECH then
those buildings will no longer satisfy the old RequiresStolen*Tech
flags.



Factories
`````````

:[BuildingType]SpyEffect.UnitVeterancy= (boolean): Whether or not
  spying this enemy factory will make all future units you build from
  your own factories of the same type start veteran. For example, spying
  an enemy barracks with `SpyEffect.UnitVeterancy=yes` set will cause
  all future InfantryTypes that you build to start veteran. NB: This
  only works for VehicleType and InfantryType factories at present. Also
  note that infiltrating any VehicleType factory (i.e. War Factory or
  Naval Yard) will only make land vehicles start veteran - Naval
  vehicles cannot be made to start veteran through spy infiltration
  logic. SpyEffect.UnitVeterancy=
:[BuildingType]SpyEffect.RevealProduction= (boolean) *NEW EFFECT*:
  Whether or not spying this enemy factory will allow you to see what
  the enemy is presently building from that factory. Once the building
  has been spied, select the building and the cameo of the unit that is
  being produced will be displayed over the building. New effect: Reveal
  production cameo (shows you what the enemy are currently building).
  SpyEffect.RevealProduction=


.. versionadded:: 0.1



<<<SEPARATOR>>>
