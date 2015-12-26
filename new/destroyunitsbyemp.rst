Destroy Units by EMP
~~~~~~~~~~~~~~~~~~~~

This setting allows objects to be destroyed by EMP rather than just being
deactivated temporarily. This is to bridge a difference between flying aircraft,
which is destroyed by EMP instantaneously, and other flying objects
like the Siege Chopper, Kirov and Yuri's Disk, which are not because they are
no :type:`AircraftTypes`.

You can create units that only take a certain amount of EMP before failing
completely, as well as :tag:`BalloonHover=yes` or :tag:`JumpJet=yes` units that
either crash just like aircraft when in air, or get deactivated like ground
units and just stay alive.

:tagdef:`[TechnoType]EMP.Threshold=enumeration - one of yes|no|inair *or* integer - frames`
  Specifies whether or not an object of this type will be destroyed by EMP
  weapons. Use an integer to set the exact EMP duration this unit has to exceed
  to get destroyed.

  + Positive values will destroy the unit if the number of EMP frames exceeds
    this value. :value:`yes` equals :value:`1`, meaning immediately.
  + Negative values will destroy the unit only if is currently in-air.
    :value:`inair` equals :value:`-1`, meaning immediately if in air.
  + A value of zero will disable this feature. :value:`no` equals :value:`0`.

  Defaults to :value:`inair`, destroying all units if they are in the air the
  instant the EMP hits.

  .. note:: Parachuting units do not count as being in the air. Only exceeding
    their positive threshold (if set) will kill them.

For example, using :value:`inair` causes a deployed Siege Chopper not to be
destroyed. Using :value:`-100` will crash the Siege Chopper only if it is in-air
and it accumulates an EMP duration of more than 100 frames.

.. index:: EMP; EMP weapons can destroy units.

.. versionadded:: 0.2
