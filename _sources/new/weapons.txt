=======
Weapons
=======

:captiontag:`[WeaponTypes]` Section
-----------------------------------
This new section allows you to declare new weapons without having to declare a
dummy unit to parse them (like the official "WEEDGUY" hack). This works in the
same way as the existing ``[Warheads]`` section. Any :type:`WeaponType` listed
under the :tag:`[WeaponTypes]` section will be parsed by the game and can be
used as a shrapnel weapon or a new weapon in a game mode, etc.

.. versionadded:: 0.1

.. index:: Rad beams can have custom colors and duration and amplitude.

Radiation Beams
---------------
Before :game:`Ares`, Radiation beams could not be customized they were always
either green or blue depending on the type of weapon. Now, however, radiation
beams can be customized using the following flags (which affect weapons with
:tag:`IsRadBeam=yes` set and/or :tag:`IsRadEruption=yes` set) in the weapon's
INI section: 

:tagdef:`[Weapon]Beam.Color=R,G,B`
  The color that the beam will be drawn in. Defaults to
  :tag:`[AudioVisual]ChronoBeamColor` for weapons with a Temporal warhead, and
  :tag:`[Radiation]RadColor` for weapons with a non-Temporal warhead.
:tagdef:`[Weapon]Beam.IsHouseColor=boolean`
  Whether or not the beam should be drawn using the firing unit's player color
  instead of the specific color specified by :tag:`Beam.Color`.
:tagdef:`[Weapon]Beam.Duration=integer`
  The number of frames for which the beam should be visible. Default is
  :value:`15` as per original RadBeams. The RadEruption effect originally used
  a random value between 5 and 20.
:tagdef:`[Weapon]Beam.Amplitude=float`
  The amplitude of the beam (possibly measured in pixels?). Defaults to
  :value:`40.0` as per original RadBeams. The RadEruption effect originally used
  a random value between 100.0 and 500.0.

.. versionadded:: 0.1

.. index:: Electric bolts can have custom colors.

Electric Bolt Coloring
----------------------
:tagdef:`[Weapon]Bolt.Color1=R,G,B`
  First color used for drawing this bolt.
:tagdef:`[Weapon]Bolt.Color2=R,G,B`
  Second color used for drawing this bolt.
:tagdef:`[Weapon]Bolt.Color3=R,G,B`
  Third color used for drawing this bolt.

The three colors used to draw this Electric Bolt. Can be omitted to use the
default values (default values are palette-dependent as opposed to RGB). 

.. versionadded:: 0.1


.. index:: Enabled unused IsLaser wave effect.

Wave Effects
------------
An unused weapon effect (present in the game code but disabled) has
been enabled. It is similar in appearance to the old laser beam or the
old disruptor wave from previous games. For now it is referred to as
*Laser*.

:tagdef:`[Weapon]Wave.IsLaser=boolean`
  Should the *Laser* effect be applied to this weapon?
:tagdef:`[Weapon]Wave.IsBigLaser=boolean`
  Should the *BigLaser* effect be applied to this weapon?

:tag:`IsLaser` and :tag:`IsBigLaser` produce two different effects, however
their naming was established before the effects were fully tested:
:tag:`IsLaser` appears to actually render a wider beam! See the image below,
left unit is using :tag:`Wave.IsLaser`, the right one is using
:tag:`Wave.IsBigLaser`:

.. image:: /images/wave_lasers.png
  :alt: Effects of Wave.Is(Big)Laser
  :align: center

.. versionadded:: 0.1

The following flags are applicable to all Wave effects; the aforementioned
:tag:`Wave.Is(Big)Laser=yes` as well as :tag:`Sonic=yes` and
:tag:`IsMagBeam=yes`.

.. index:: Waves can have custom colors.

Wave Coloring
-------------
:tagdef:`[Weapon]Wave.Color=R,G,B`
  The color of the wave. Default value is different depending on the type of
  Wave.
:tagdef:`[Weapon]Wave.IsHouseColor=boolean`
  If this is set to yes then the wave will be drawn in the firing unit's house
  color instead of the color specified by :tag:`Wave.Color`.
  
.. warning:: Sonic Waves do no yet have a sensible default :tag:`Wave.Color`.

.. versionadded:: 0.1

.. index:: Customisable wave direction.

Wave Direction
--------------
Waves are drawn in different directions (from firer to target or vice versa)
depending on the type of wave and the circumstances. This direction can now be
customized in several ways. The following flags all default to no unless
otherwise specified.

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
  target is an :tag:`AircraftType`.
:tagdef:`[Weapon]Wave.ReverseAgainstOthers=boolean`
  Whether or not the wave will be drawn from target to firer when the target is
  anything not covered by the other :tag:`ReverseAgainst` flags (i.e. trees,
  overlays, empty cells, etc.). 

.. versionadded:: 0.1

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

.. index:: Customisable Ivan bomb clones.

.. _custom-ivan-bombs:

Customizable Ivan Bombs
-----------------------
As with many other features of :game:`Yuri's Revenge`, the settings that control
Crazy Ivan Bombs are global so you can't have multiple variations of them with
their own controls. With :game:`Ares` it is now possible to create new Ivan
Bomb-esque weapons new types of sticky bomb with whatever settings you like. The
only aspect of Ivan Bombs that hasn't been de-globalized is the ability to
remote detonate the bombs this feature is either enabled or disabled for all
Ivan Bomb types.

When :tag:`IvanBomb=yes` is set on the weapon's warhead, the weapon can specify
the following flags in order to customize that bomb:

:tagdef:`[Weapon]IvanBomb.Warhead=WarheadType`
  The warhead that will be used when the bomb detonates.
:tagdef:`[Weapon]IvanBomb.Damage=integer`
  The damage that will be dealt when the bomb detonates.
:tagdef:`[Weapon]IvanBomb.Detachable=boolean`
  Whether or not Engineers can remove this bomb from units it has been attached
  to.
:tagdef:`[Weapon]IvanBomb.DestroysBridges=boolean`
  Whether or not this bomb can be used on Bridge Repair Huts in order to destroy
  the corresponding Bridge.
  
  .. note:: Bombs can always be attached to Bridge Huts, but the resulting
    explosion will not destroy the bridge unless
    \ :tag:`IvanBomb.DestroysBridges=yes` is set.
:tagdef:`[Weapon]IvanBomb.Delay=integer`
  The number of frames that will elapse before the bomb detonates automatically.
:tagdef:`[Weapon]IvanBomb.AttachSound=sound name`
  The sound that will be played when the bomb is attached to a target.
:tagdef:`[Weapon][Weapon]IvanBomb.TickingSound=sound name`
  The sound that will be played whilst the bomb is attached to a unit. In order
  for this sound to loop correctly, the sound must have :tag:`Control=loop` set
  in its INI section in :file:`soundmd.ini`.
:tagdef:`[Weapon]IvanBomb.Image=filename, *excluding*the .shp extension`
  The SHP file for the image to display over a unit that has a bomb attached to
  them, in the format "filename"(the ".shp" extension is automatically added by
  the engine). If the image cannot be loaded then the game will fall back to the
  default :file:`bombcurs.shp`.
:tagdef:`[Weapon]IvanBomb.FlickerRate=integer`
  The rate at which the bomb SHP will flip back and forth between two frames to
  give the impression of a flickering fuse. On every game frame, the frame of
  the bomb SHP is calculated as follows:
  
  ``frameToShow = (Game.CurrentFrame - Bomb.PlantingFrame) / (Bomb.Delay /
  (Bomb.Image.Frames - 1))``
  
  ``IF (CurrentFrame mod (2 * Bomb.FlickerRate) >=  Bomb.FlickerRate) THEN``
    ``frameToShow = frameToShow + 1``

Originally this logic was hard-coded to ignore the last frame of the bomb SHP,
which was originally planned to be used for so called "death bombs" which were
cut from the game before :game:`Red Alert 2` was released. This hard-coding has
been changed so that the whole SHP is now considered for the fuse, however this
means that you'll now see that extra frame from :file:`bombcurs.shp`, unless you
replace that SHP file.

.. image:: /images/bombcurs.png
  :alt: Image of bombcurs.shp
  :align: center

.. versionadded:: 0.1

LaserThickness
--------------
:tagdef:`[Weapon]LaserThickness=integer`
  Enables the customization of laser widths.

.. note:: Currently this has the same bugs as the :game:`NPatch` version, only
    works with :tag:`IsHouseColor=yes` and have low quality.

.. versionadded:: 0.2
