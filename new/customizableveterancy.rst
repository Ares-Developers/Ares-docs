Customizable Veterancy
~~~~~~~~~~~~~~~~~~~~~~

Configure the way units get experience from killing enemies.

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
:tagdef:`[TechnoType]Experience.FromAirstrike=boolean`
  If a kill gets credited to an aircraft that was called in by an air strike,
  the designator will get the experience instead of the actual aircraft.
  Defaults to :value:`no`.
:tagdef:`[TechnoType]Experience.AirstrikeModifier=float - multiplier`
  If :tag:`Experience.FromAircraft=yes` is set on the designator of an airstrike
  (like Boris), the experience gain is multiplied by this value. Defaults to
  :value:`100%`.
:tagdef:`[TechnoType]Experience.MindControlSelfModifier=float - multiplier`
  If a mind-controlled unit kills an enemy, its controller gets this percentage
  of the experience the original killer gets. This additional experience is not
  subtracted from the experience gained by the original killer. Defaults to
  :value:`0%`.
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

:tag:`Trainable=no` is always honored, no untrainable unit will get any
experience. Mind that an open-topped vehicle in the unmodified game also could
promote its passengers (but without the mind-control check) if it had
:tag:`Trainable=no` set.

.. index:: Veterancy; Veterancy options for Passengers, Airstrike and Mind-Control.

.. versionadded:: 0.2