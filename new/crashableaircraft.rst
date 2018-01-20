Crashing
~~~~~~~~

:captiontag:`Crashable` and Aircraft
------------------------------------

Any :type:`AircraftType` being destroyed in air would explode and crash, causing
damage on the ground. A tag, :tag:`Crashable`, exists, but it only works for the
other :type:`TechnoTypes`, so aircraft cannot be made to not crash. :game:`Ares`
adds support for :tag:`Crashable=no` and aircraft.

:tagdef:`[AircraftType]Crashable=boolean`
  Whether the aircraft will explode and fall down crashing into the ground when
  destroyed. Otherwise the aircraft will explode in mid-air and disappear.
  Defaults to :value:`yes`.

.. index:: Aircraft; Support for Crashable=no.

.. versionadded:: 0.4


Spinning
--------

Aircraft that is going to crash starts to spin uncontrollably. For larger planes
this can look silly and :game:`Ares` adds an option for this to turn it off.

:tagdef:`[AircraftType]CrashSpin=boolean`
  Whether the aircraft should spin when crashing, opposed to gliding down to the
  ground. Defaults to :value:`yes`.

  .. note:: This setting only works for aircraft. :tag:`JumpJet=yes`
    \ :type:`VehicleType`\ s do not support it.

.. index:: Aircraft; Spinning while crashing made optional.

.. versionadded:: 0.6
