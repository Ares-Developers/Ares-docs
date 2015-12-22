Hijackers
~~~~~~~~~

Vehicle thieves can steal enemy units, effectively hijacking them on the battle
field. If you enable hijacking by setting :tag:`VehicleThief=yes` on an
:type:`InfantryType`, you can customize it in various ways:

:tagdef:`[InfantryType]VehicleThief.EnterSound=Sound name`
  Specifies the sound played when a hijacker captures an enemy vehicle. This
  also works for infantry with :tag:`CanDrive=yes` when reclaiming neutralized
  units. Defaults to :value:`none`.
:tagdef:`[InfantryType]VehicleThief.LeaveSound=Sound name`
  Specifies the sound played when a hijacker leaves a vehicle when it is
  destroyed. Defaults to :value:`none`.
:tagdef:`[InfantryType]VehicleThief.BreakMindControl=boolean`
  Whether the vehicle thief can hijack units that are mind-controlled. The link
  between the controller and the unit will be broken when the hijacker enters.
  Otherwise the hijacker cannot steal the unit. Defaults to :value:`yes`.
:tagdef:`[InfantryType]VehicleThief.OneTime=boolean`
  Whether the vehicle thief will be consumed in the procees of capturing a unit.
  Otherwise the hijacker will emerge when the captured unit is destroyed. In
  every case the hijacker will be reimbursed when the unit is grinded. Defaults
  to :tag:`no`.
:tagdef:`[InfantryType]VehicleThief.KillPilots=integer`
  The number of pilots the vehicle thief kills when entering a unit. These
  pilots will have no chance to escape the unit when it is destroyed. Use
  :value:`-1` to kill all pilots. In :game:`Tiberian Sun` the hijacker will
  prevent any crew from escaping a destroyed vehicle. Defaults to :value:`0`.

In :game:`Tiberian Sun` the vehicle thief was not allowed to hijack units that
had :tag:`NonVehicle=yes` set. :game:`Ares` does not use :tag:`NonVehicle`,
because it affects many other features as well, which might be undesirable.
Instead, you will have to use the new dedicated flag :tag:`VehicleThief.Allowed`
to change whether a unit can be hijacked.

:tagdef:`[TechnoType]VehicleThief.Allowed=boolean`
  Whether this :type:`VehicleType` or :type:`AircraftType` can be hijacked by
  vehicle thieves. Defaults to :value:`yes`.

.. note:: Vehicle Thieves cannot drive neutralized vehicles by default, but
  \ :tag:`VehicleThief=yes` can be combined with :tag:`CanDrive=yes` without
  problems.

Hijackers remember their health and their previous veterancy level. When the
vehicle they stole are destroyed, they respawn with a random health up to half
their previous health, and their old rank.

Hijacking works well together with Mind Control now. If a mind-controlled unit
is captured, the connection to the controller is broken and there will be no
bogus links left behind. Likewise, mind-controlled hijackers will capture
vehicles for their original owning houses, not for their capturers'. The
mind-control link will be transferred to the captured vehicle, if it isn't
immune to mind control. Otherwise, the mind-controller loses control over both
hijacker and its vicitm. Same is true for the opposite case: When a hijacked and
mind-controlled unit is destroyed, the link is transferred to the hijacker, if
it isn't immune to psionics.

Vehicle Thieves cannot hijack friendly units or vehicles neutralized by the Kill
Driver warheads. See :doc:`KillDriver and CanDrive </new/killingdrivers>`.

.. index:: Infantry; Expanded VehicleThief logic.

.. versionadded:: 0.2
