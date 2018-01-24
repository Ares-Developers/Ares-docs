Customizable Veterancy
~~~~~~~~~~~~~~~~~~~~~~

Configure the way units get experience from killing enemies.

:tag:`Trainable=no` is always honored, no untrainable unit will get any
experience. Mind that an open-topped vehicle in the unmodified game also could
promote its passengers (but without the mind-control check) if it had
:tag:`Trainable=no` set.

.. versionadded:: 0.2


.. index:: Veterancy; Experience from passengers

From Passengers
```````````````

:tagdef:`[TechnoType]Experience.FromPassengers=boolean`
  Allow :tag:`OpenTopped=yes` and :tag:`Gunner=yes` units to gain experience
  when a passenger kills an enemy. If this is :value:`no` the unit only gets
  promoted when killing enemies itself. For gunners like the IFV this means the
  vehicle may not have any passengers to gain experience. Defaults to
  :value:`yes`.
:tagdef:`[TechnoType]Experience.PromotePassengers=boolean`
  If an :tag:`OpenTopped=yes` or :tag:`Gunner=yes` unit is trainable and already
  elite,  the passenger shooting will get the experience instead. If this is
  :value:`no` the additional experience will be lost as the vehicle is elite
  already. Defaults to :value:`no`.
:tagdef:`[TechnoType]Experience.PassengerModifier=float - multiplier`
  If a kill gets credited to a passenger, the experience gain is multiplied by
  this value. Defaults to :value:`100%`.


.. index::
  Veterancy; Experience from airstrikes
  Airstrikes; Give experience to designator

From Airstrikes
```````````````

:tagdef:`[TechnoType]Experience.FromAirstrike=boolean`
  If a kill gets credited to an aircraft that was called in by an air strike,
  the designator will get the experience instead of the actual aircraft.
  Defaults to :value:`no`.
:tagdef:`[TechnoType]Experience.AirstrikeModifier=float - multiplier`
  If :tag:`Experience.FromAircraft=yes` is set on the designator of an airstrike
  (like Boris), the experience gain is multiplied by this value. Defaults to
  :value:`100%`.


.. index::
  Veterancy; Experience from mind control
  Mind Control; Give experience to mind-controller

From Mind-Controlled
````````````````````

:tagdef:`[TechnoType]Experience.MindControlSelfModifier=float - multiplier`
  If a mind-controlled unit kills an enemy, its controller gets this percentage
  of the experience the original killer can get (the amount before
  :tag:`Experience.MindControlVictimModifier` is applied). This additional
  experience is not subtracted from the experience gained by the original
  killer. Defaults to :value:`0%`.
:tagdef:`[TechnoType]Experience.MindControlVictimModifier=float - multiplier`
  If a mind-controlled unit kills an enemy, its gained experience is multiplied
  by this value. Use this for example to subtract the amount the unit's
  controller gets by having this value and
  :tag:`Experience.MindControlSelfModifier` sum up to 100%. Defaults to
  :value:`100%`.

Mind-controlled open-topped vehicles will not gain any experience from their
passengers if the mind-controller's and the open-topped's players aren't allied.
Mind-controllers will not gain experience from killing enemies with a captured
allied unit.


.. index::
  Veterancy; Experience from spawns
  Spawns; Give experience to spawners

From Spawns
```````````

Spawners like the Aircraft Carrier or the Destroyer can get experience from
their spawned aircrafts' kills. For this to work, both the spawn and the spawner
must be :tag:`Trainable=yes`. The following two tags go on the unit that spawns,
not the spawns themselves.

:tagdef:`[TechnoType]Experience.SpawnOwnerModifier=float - multiplier`
  The percentage of experience the unit owning a spawn gains when the spawn
  kills an enemy. This tag has to be set on the spawner unit, not the spawn.
  Defaults to :value:`0%`.
:tagdef:`[TechnoType]Experience.SpawnModifier=float - multiplier`
  The percentage of experience a spawn of this unit gains when the spawn kills
  an enemy. This tag has to be set on the spawner unit, not the spawn.
  Defaults to :value:`100%`.

To split the experience between spawner and spawns, make these values sum up to
100%. This is not required, though.

If a spawner is mind-controlled, both the spawner's and the spawn's experience
is multiplied by :tag:`Experience.MindControlVictimModifier`.
