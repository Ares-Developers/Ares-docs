Customizable Veterancy
~~~~~~~~~~~~~~~~~~~~~~

Configure the way units get experience from killing enemies. Veterancy
options for Passengers, Airstrike and Mind-Control.

:[TechnoType]Experience.FromPassengers= (boolean): Allow
  `OpenTopped=yes` and `Gunner=yes` units to gain experience when a
  passenger kills an enemy. If this is `no` the unit only gets promoted
  when killing enemies itself. For gunners like the IFV this means the
  vehicle may not have any passengers to gain experience. Defaults to
  `yes`. Experience.FromPassengers=
:[TechnoType]Experience.PromotePassengers= (boolean): If an
  `OpenTopped=yes` or `Gunner=yes` unit is trainable and already elite,
  the passenger shooting will get the experience instead. If this is
  `no` the additional experience will be lost as the vehicle is elite
  already. Defaults to `no`. Experience.PromotePassengers=
:[TechnoType]Experience.PassengerModifier= (float - multiplier): If a
  kill gets credited to a passenger, the experience gain is multiplied
  by this value. Defaults to `100%`. Experience.PassengerModifier=
:[TechnoType]Experience.FromAirstrike= (boolean): If a kill gets
  credited to an aircraft that was called in by an air strike, the
  designator will get the experience instead of the actual aircraft.
  Defaults to `no`. Experience.FromAirstrike=
:[TechnoType]Experience.AirstrikeModifier= (float - multiplier): If
  `Experience.FromAircraft=yes` is set on the designator of an airstrike
  (like Boris), the experience gain is multiplied by this value.
  Defaults to `100%`. Experience.AirstrikeModifier=
:[TechnoType]Experience.MindControlSelfModifier= (float - multiplier):
  If a mind-controlled unit kills an enemy, its controller gets a
  percentage of the experience the original killer gets. This additional
  experience is not subtracted from the original killers gained
  experience. Defaults to `0%`. Experience.MindControlSelfModifier=
:[TechnoType]Experience.MindControlVictimModifier= (float -
  multiplier): If a mind-controlled unit kills an enemy, its gained
  experience is multiplied by this value. Use this for example to
  subtract the amount the unit's controller gets by having this value
  and `Experience.MindControlSelfModifier` sum up to 100%. Defaults to
  `100%`. Experience.MindControlVictimModifier=


Mind-controlled open-topped vehicles will not gain any experience from
it's passengers if the mind-controller's and the open-topped's players
aren't allied. Mind-controllers will not gain experience from killing
enemies with a captured allied unit.

`Trainable=no` is always honored, no untrainable unit will get any
experience. Mind that an open-topped vehicle in the unmodified game
also could promote its passengers (but without the mind-control check)
if it had `Trainable=no` set.

.. versionadded:: 0.2
