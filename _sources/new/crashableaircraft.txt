:captiontag:`Crashable` and Aircraft
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Any :type:`AircraftType` being destoyed in air would explode and crash, causing
damage on the ground. A tag, :tag:`Crashable`, exists, but it only works for the
other :type:`TechnoTypes`, so aircraft cannot be made to not crash. :game:`Ares`
adds support for :tag:`Crashable=no` and aircraft.

:tagdef:`[AircraftType]Crashable=boolean`
  Whether the aircraft will explode and fall down crashing into the ground when
  destroyed. Otherwise the aircraft will explode in mid-air and disappear.
  Defaults to :value:`yes`.

.. index:: Aircraft; Support for Crashable=no.

.. versionadded:: 0.4
