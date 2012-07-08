Destroy Units by EMP
~~~~~~~~~~~~~~~~~~~~

Certain units should be destroyed by EMP rather than just being paralyzed.
Aircraft is destroyed by EMP instantaneously, but flying :type:`TechnoTypes`
like the Siege Chopper, Kirov and Yuri's Disk do not count as Aircraft.
:tag:`EMP.Threshold` changes this behavior. :tag:`EMP.Threshold` defaults to
:value:`inair`, destroying all :type:`TechnoTypes` that are in the air the
instant the EMP hits. Parachuting :type:`TechnoTypes` do not count as being in
the air, yet exceeding the positive threshold will kill them, too.

:tagdef:`[TechnoType]EMP.Threshold=enumeration - one of yes|no|inair *or* integer - frames`
  Specifies whether or not the :type:`TechnoType` will be destroyed by EMP
  weapons. Use an integer to set the exact EMP duration this unit has to exceed
  to get destroyed.

    + Positive values will destroy the unit if the number of EMP frames exceeds
      this value. :value:`yes` equals :value:`1`.
    + Negative values will destroy the unit only if is currently in-air.
      :value:`inair` equals :value:`-1`.
    + A value of zero will disable this feature. :value:`no` equals :value:`0`.


You can both create units that only take a certain amount of EMP before failing
irrecoverably as well as flying and floating units that just crash like
aircraft.

Using :value:`inair` causes the Siege Chopper not to be destroyed when it is
deployed. Using :value:`-100` will crash the Siege Chopper only if it is in-air
and it accumulates an EMP duration of more than 100 frames.

.. index:: EMP; EMP weapons can destroy units.

.. versionadded:: 0.2
