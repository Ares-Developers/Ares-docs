Waves
~~~~~

.. index::
  Weapons; IsLaser and IsBigLaser wave effect
  Waves; IsLaser and IsBigLaser effect

Wave Effects
------------

An unused weapon effect (present in the game code but disabled) has been
enabled. It is similar in appearance to the old laser beam or the old Disruptor
wave from previous games. For now it is referred to as *Laser*.

:tagdef:`[Weapon]Wave.IsLaser=boolean`
  Should the *Laser* effect be applied to this weapon?
:tagdef:`[Weapon]Wave.IsBigLaser=boolean`
  Should the *BigLaser* effect be applied to this weapon?

:tag:`Wave.IsLaser` and :tag:`Wave.IsBigLaser` produce two different effects,
however their naming was established before the effects were fully tested:
:tag:`Wave.IsLaser` appears to actually render a wider beam! See the image
below, left unit is using :tag:`Wave.IsLaser`, the right one is using
:tag:`Wave.IsBigLaser`:

.. image:: /images/wave_lasers.png
  :alt: Effects of Wave.Is(Big)Laser
  :align: center

.. versionadded:: 0.1

The following flags are applicable to all Wave effects; the aforementioned
:tag:`Wave.Is(Big)Laser=yes` as well as :tag:`IsSonic=yes` and
:tag:`IsMagBeam=yes`.


.. index::
  Weapons; Wave colors
  Waves; Colors

Wave Coloring
-------------

:tagdef:`[Weapon]Wave.Color=R,G,B`
  The color of the wave. Default value is different depending on the type of
  Wave.
:tagdef:`[Weapon]Wave.IsHouseColor=boolean`
  If this is set to :value:`yes` then the wave will be drawn in the firing
  unit's house color instead of the color specified by :tag:`Wave.Color`.
  
.. warning:: Sonic Waves do not yet have a sensible default :tag:`Wave.Color`.

.. versionadded:: 0.1


.. index::
  Weapons; Wave drawing direction
  Waves; Direction the wave is drawn in

Wave Direction
--------------

Waves are drawn in different directions (from firer to target or vice versa)
depending on the type of wave and the circumstances. This direction can now be
customized in several ways. The following flags all default to :value:`no`
unless otherwise specified.

:tagdef:`[Weapon]Wave.ReverseAgainstVehicles=boolean`
  Whether or not the wave will be drawn from the target to the firer when the
  target is a :type:`VehicleType`. Defaults to :value:`yes` if
  :tag:`IsMagBeam=yes` is set on the weapon.
:tagdef:`[Weapon]Wave.ReverseAgainstBuildings=boolean`
  Whether or not the wave will be drawn from the target to the firer when the
  target is a :type:`BuildingType`.
:tagdef:`[Weapon]Wave.ReverseAgainstInfantry=boolean`
  Whether or not the wave will be drawn from the target to the firer when the
  target is an :type:`InfantryType`.
:tagdef:`[Weapon]Wave.ReverseAgainstAircraft=boolean`
  Whether or not the wave will be drawn from the target to the firer when the
  target is an :type:`AircraftType`.
:tagdef:`[Weapon]Wave.ReverseAgainstOthers=boolean`
  Whether or not the wave will be drawn from target to firer when the target is
  anything not covered by the other :tag:`ReverseAgainst` flags (i.e. trees,
  overlays, empty cells, etc.). 

.. versionadded:: 0.1


.. index::
  Weapons; Wave ambient damage
  Waves; Ambient damage for all types

Wave Ambient Damage
-------------------
All waves can now deal disruptor-style damage to objects that they pass through,
a feature that was previously limited to Sonic Waves only. As a reminder, the
flags that control this are:

:tagdef:`[Weapon]AmbientDamage=integer`
  How much damage the wave deals to objects it passes through. Defaults to zero.
:tagdef:`[Weapon]Warhead=WarheadType`
  The warhead used to deal ambient damage as well as normal damage.

.. versionadded:: 0.1
