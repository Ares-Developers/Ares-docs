.. index:: Super Weapons; Lighting

Lighting
````````

The three major super weapons allow for a temporary change of lighting. You can
change any of these values without having to change the others too. If you want
to use the scenario's respective default value, use :value:`-1` for ambient or
colors.

:tagdef:`[SuperWeapon]Light.Enabled=boolean`
  Whether the lighting gets respected or not. Currently only the primary super
  weapons support lighting changes.
:tagdef:`[SuperWeapon]Light.Ambient=integer`
  The brightness of the environment. Too high values will cause a slow-down.
:tagdef:`[SuperWeapon]Light.Red=integer`
  The red component of the lighting.
:tagdef:`[SuperWeapon]Light.Green=integer`
  The green component of the lighting.
:tagdef:`[SuperWeapon]Light.Blue=integer`
  The blue component of the lighting.

.. versionadded:: 0.2
