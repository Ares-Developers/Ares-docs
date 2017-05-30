Fall Rate
~~~~~~~~~

When a unit is dropped onto the battlefield from a plane, with or without
parachute, these settings define how fast it will accelerate and how fast it
will fall at most.

:tagdef:`[TechnoType]FallRate.Parachute=integer`
  The acceleration towards the ground applied each frame a parachuted unit is
  falling. Defaults to :value:`1`.

:tagdef:`[TechnoType]FallRate.NoParachute=integer`
  The acceleration towards the ground applied each frame a unit without
  parachute is falling. Defaults to :value:`1`.

:tagdef:`[TechnoType]FallRate.ParachuteMax=integer`
  The maximum speed a parachuted unit is falling with. Value has to be negative.
  Defaults to :tag:`[General]ParachuteMaxFallRate`.

:tagdef:`[TechnoType]FallRate.NoParachuteMax=integer`
  The maximum speed a unit without parachute is falling with. Value has to be
  negative. Defaults to :tag:`[General]NoParachuteMaxFallRate`.

.. index:: Units; Customizable fall rates

.. versionadded:: 0.D
