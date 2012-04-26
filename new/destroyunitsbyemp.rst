Destroy Units by EMP
~~~~~~~~~~~~~~~~~~~~

Certain units should be destroyed by EMP rather than just being
paralyzed. Aircraft is destroyed by EMP instantaneously, but flying
TechnoTypes like the Siege Chopper, Kirov and Yuri's Disk do not count
as Aircraft. `EMP.Threshold` changes this behavior. `EMP.Threshold`
defaults to `inair`, destroying all TechnoTypes that are in the air
the instant the EMP hits. Parachuting TechnoTypes do not count as
being in the air, yet exceeding the positive threshold will kill them,
too.

:[TechnoType]EMP.Threshold= (enumeration - one of yes|no|inair *or* integer - frames):
  Specifies whether or not the TechnoType will be destroyed by EMP weapons. Use
  an integer which the EMP duration cannot exceed without destroying this unit.

    + Positive values will destroy the unit if its number of EMP frames
      exceeds this value. `yes` equals `1`.
    + Negative values will destroy the unit only if is currently in-air.
      `inair` equals `-1`.
    + A value of zero will disable this feature. `no` equals `0`.


You can create units that only take a certain amount of EMP before
failing irrecoverably or flying and floating units that just crash.

Using `inair` causes the Siege Chopper not to be destroyed when it is
deployed.

.. index:: EMP; EMP weapons can destroy units.

.. versionadded:: 0.2
