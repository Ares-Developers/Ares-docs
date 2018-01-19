:captiontag:`Type=SpyPlane`
```````````````````````````

Default values for general tags:

:tagdef:`[SuperWeapon]SW.AITargeting=enumeration`
  Defaults to :value:`ParaDrop`.
:tagdef:`[SuperWeapon]Cursor=mouse cursor`
  Defaults to :value:`SpyPlane`.


Spy Plane specific tags:

:tagdef:`[SuperWeapon]SpyPlane.Type=AircraftType`
  The :type:`AircraftType` that will be sent as a spy plane. Defaults to
  :value:`SPYP`.
:tagdef:`[SuperWeapon]SpyPlane.Count=integer`
  The number of spy planes to be sent out. Defaults to :value:`1`.
:tagdef:`[SuperWeapon]SpyPlane.Mission=mission`
  The mission that the aircraft will be sent on (:value:`Guard`,
  :value:`Attack`, :value:`Move`, etc). Defaults to :value:`SpyPlane Approach`.

.. index:: Super Weapons; SpyPlane can now specify which AircraftType, how many,
  and what mission to perform.


.. versionadded:: 0.1
