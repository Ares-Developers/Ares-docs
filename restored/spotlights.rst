Spotlights
~~~~~~~~~~

Spotlights would cause an Internal Error whenever they were created. The error
no longer occurs so spotlights can now be used.

:tagdef:`[Unit]HasSpotlight=boolean`
  If set to :value:`yes`, creates a spotlight from the unit (note that this is
  now available to all of the Big Four types, not just :type:`BuildingTypes`).
  When attached to a :type:`BuildingType`, the spotlight still behaves like it
  used to, just circling around, but when it is attached to a different unit
  type, such as a :type:`VehicleType`, it is fixed to shine straight ahead.
  Defaults to :value:`no`.
:tagdef:`[Unit]Spotlight.StartHeight=integer - leptons`
  Specifies the number of leptons above the ground at which the spotlight will
  be generated. Defaults to :value:`250`.
:tagdef:`[Unit]Spotlight.Distance=integer - leptons`
  The number of leptons ahead of the unit where the spotlight will reach the
  ground. Defaults to :value:`1024`.
:tagdef:`[Unit]Spotlight.AttachedTo=enumeration - one of body|turret|barrel`
  The part of the unit that the spotlight will align to in regards to facing. If
  set to :value:`body` then the spotlight will be pointed in the direction the
  unit's body is facing, if set to :value:`turret` then the spotlight will be
  pointed in the direction the unit's turret is facing. Does not work on
  :type:`BuildingTypes`. Defaults to :value:`body`.
:tagdef:`[Unit]Spotlight.DisableRed=boolean`
  If set to :value:`yes` then the spotlight will not emit any red light.
  Defaults to :value:`no`.
:tagdef:`[Unit]Spotlight.DisableGreen=boolean`
  If set to :value:`yes` then the spotlight will not emit any green light.
  Defaults to :value:`no`.
:tagdef:`[Unit]Spotlight.DisableBlue=boolean`
  If set to :value:`yes` then the spotlight will not emit any blue light.
  Defaults to :value:`no`.
:tagdef:`[Unit]Spotlight.DisableColor=boolean`
  If set to :value:`yes` then the spotlight will paint the ground darker,
  instead of brighter, and the disable red/green/blue flags mentioned above will
  be ignored. Defaults to :value:`no`.

.. versionadded:: 0.1
