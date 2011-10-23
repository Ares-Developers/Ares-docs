Weapons
~~~~~~~



`[WeaponTypes]` Section
```````````````````````

This new section allows you to declare new weapons without having to
declare a dummy unit to parse them (like the official "WEEDGUY" hack).
This works in the same way as the existing `[Warheads]` section. Any
WeaponType listed under the `[WeaponTypes]` section will be parsed by
the game and can be used as a shrapnel weapon or a new weapon in a
game mode, etc.

.. versionadded:: 0.1



Radiation Beams
```````````````

Before Ares, Radiation beams could not be customized they were always
either green or blue depending on the type of weapon. Now, however,
radiation beams can be customized using the following flags (which
affect weapons with `IsRadBeam=yes` set and/or `IsRadEruption=yes`
set) in the weapon's INI section: Rad beams can have custom colors,
duration and amplitude.

:[Weapon]Beam.Color= (R,G,B): The color that the beam will be drawn
  in. Defaults to `[AudioVisual]ChronoBeamColor` for weapons with a
  Temporal warhead, and `[Radiation]RadColor` for weapons with a non-
  Temporal warhead. Beam.Color=
:[Weapon]Beam.IsHouseColor= (boolean): Whether or not the beam should
  be drawn using the firing unit's player color instead of the specific
  color specified by `Beam.Color`. Beam.IsHouseColor=
:[Weapon]Beam.Duration= (integer): The number of frames for which the
  beam should be visible. Default is 15 as per original RadBeams. The
  RadEruption effect originally used a random value between 5 and 20.
  Beam.Duration=
:[Weapon]Beam.Amplitude= (float): The amplitude of the beam (possibly
  measured in pixels?). Defaults to 40.0 as per original RadBeams. The
  RadEruption effect originally used a random value between 100.0 and
  500.0. Beam.Amplitude=


.. versionadded:: 0.1



Electric Bolt Coloring
``````````````````````

:[Weapon]Bolt.Color1= (R,G,B) [Weapon]Bolt.Color2= (R,G,B)
  [Weapon]Bolt.Color3= (R,G,B): The three colors used to draw this
  Electric Bolt. Can be omitted to use the default values (default
  values are palette-dependent as opposed to RGB). Electric bolts can
  have custom colors. Bolt.Color1= Bolt.Color2= Bolt.Color3=


.. versionadded:: 0.1



Wave Effects
````````````

An unused weapon effect (present in the game code but disabled) has
been enabled. It is similar in appearance to the old laser beam or the
old disruptor wave from previous games. For now it is referred to as
Laser. Enabled unused IsLaser wave effect.

:[Weapon]Wave.IsLaser= (boolean): :[Weapon]Wave.IsBigLaser= (boolean):

`IsLaser` and `IsBigLaser` produce two different effects, however
their naming was established before the effects were fully tested:
`IsLaser` appears to actually render a wider beam! See the image
below, left unit is using `Wave.IsLaser`, the right one is using
`Wave.IsBigLaser`:


.. versionadded:: 0.1

The following flags are applicable to all Wave effects; the
aforementioned `Wave.Is(Big)Laser=yes` as well as `Sonic=yes` and
`IsMagBeam=yes`. Wave.IsLaser= Wave.IsBigLaser=



Wave Coloring
`````````````

:[Weapon]Wave.Color= (R,G,B): The color of the wave. Default value is
  different depending on the type of Wave. NB: Sonic Waves do no yet
  have a sensible default Wave.Color. Wave.Color=
  :[Weapon]Wave.IsHouseColor= (boolean): If this is set to yes then the
  wave will be drawn in the firing unit's house color instead of the
  color specified by `Wave.Color`. Waves can have custom colors.
  Wave.IsHouseColor=





.. versionadded:: 0.1



Wave Direction
``````````````

Waves are drawn in different directions (from firer to target or vice
versa) depending on the type of wave and the circumstances. This
direction can now be customized in several ways. The following flags
all default to no unless otherwise specified.

:[Weapon]Wave.ReverseAgainstVehicles= (boolean): Whether or not the
  wave will be drawn from the target to the firer when the target is a
  VehicleType. Defaults to yes if `IsMagBeam=yes` is set on the weapon.
  Wave.ReverseAgainstVehicles= :[Weapon]Wave.ReverseAgainstBuildings=
  (boolean): Whether or not the wave will be drawn from the target to
  the firer when the target is a BuildingType.
  Wave.ReverseAgainstBuildings= :[Weapon]Wave.ReverseAgainstInfantry=
  (boolean): Whether or not the wave will be drawn from the target to
  the firer when the target is an InfantryType.
  Wave.ReverseAgainstInfantry= :[Weapon]Wave.ReverseAgainstAircraft=
  (boolean): Whether or not the wave will be drawn from the target to
  the firer when the target is an AircraftType.
  Wave.ReverseAgainstAircraft= :[Weapon]Wave.ReverseAgainstOthers=
  (boolean): Whether or not the wave will be drawn from target to firer
  when the target is anything not covered by the other 'ReverseAgainst'
  flags (i.e. trees, overlays, empty cells, etc.). Customisable wave
  direction. Wave.ReverseAgainstOthers=











.. versionadded:: 0.1



Wave Ambient Damage
```````````````````

All waves can now deal disruptor-style damage to objects that they
pass through, a feature that was previously limited to Sonic Waves
only. As a reminder, the flags that control this are:

:[Weapon]AmbientDamage= (integer): How much damage the wave deals to
  objects it passes through. Defaults to zero. :[Weapon]Warhead=
  (WarheadType): The warhead used to deal ambient damage as well as
  normal damage. Customisable Ivan bomb clones.





.. versionadded:: 0.1



Customizable Ivan Bombs
```````````````````````

As with many other features of Yuri's Revenge, the settings that
control Crazy Ivan Bombs are global so you can't have multiple
variations of them with their own controls. With Ares it is now
possible to create new Ivan Bomb-esque weapons new types of sticky
bomb with whatever settings you like. The only aspect of Ivan Bombs
that hasn't been de-globalized is the ability to remote detonate the
bombs this feature is either enabled or disabled for all Ivan Bomb
types.

When `IvanBomb=yes` is set on the weapon's warhead, the weapon can
specify the following flags in order to customize that bomb.

:[Weapon]IvanBomb.Warhead= (WarheadType): The warhead that will be
used when the bomb detonates. IvanBomb.Warhead=
:[Weapon]IvanBomb.Damage= (integer): The damage that will be dealt
when the bomb detonates. IvanBomb.Damage=
:[Weapon]IvanBomb.Detachable= (boolean): Whether or not Engineers can
remove this bomb from units it has been attached to.
IvanBomb.Detachable= :[Weapon]IvanBomb.DestroysBridges= (boolean):
Whether or not this bomb can be used on Bridge Repair Huts in order to
destroy the corresponding Bridge. NB: Bombs can always be attached to
Bridge Huts, but the resulting explosion will not destroy the bridge
unless `IvanBomb.DestroysBridges=yes` is set.
IvanBomb.DestroysBridges= :[Weapon]IvanBomb.Delay= (integer): The
number of frames that will elapse before the bomb detonates
automatically. IvanBomb.Delay= :[Weapon]IvanBomb.AttachSound= (Sound
name): The sound that will be played when the bomb is attached to a
target. IvanBomb.AttachSound= :[Weapon]IvanBomb.TickingSound= (Sound
name): The sound that will be played whilst the bomb is attached to a
unit. In order for this sound to loop correctly, the sound must have
`Control=loop` set in its INI section in soundmd.ini.
IvanBomb.TickingSound= :[Weapon]IvanBomb.Image= (filename, *excluding*
the .shp extension): The SHP file for the image to display over a unit
that has a bomb attached to them, in the format "filename"(the ".shp"
extension is automatically added by the engine). If the image cannot
be loaded then the game will fall back to the default bombcurs.shp.
IvanBomb.Image= :[Weapon]IvanBomb.FlickerRate= (integer): The rate at
which the bomb SHP will flip back and forth between two frames to give
the impression of a flickering fuse. On every game frame, the frame of
the bomb SHP is calculated as follows:

::

    frameToShow = (Game.CurrentFrame  Bomb.PlantingFrame) / (Bomb.Delay / (Bomb.Image.Frames  1))
    				IF (CurrentFrame mod (2 * Bomb.FlickerRate) >= Bomb.FlickerRate) THEN frameToShow = frameToShow + 1

Originally this logic was hard-coded to ignore the last frame of the
  bomb SHP, which was originally planned to be used for so called "death
  bombs" which were cut from the game before Red Alert 2 was released.
  This hard-coding has been changed so that the whole SHP is now
  considered for the fuse, however this means that you'll now see that
  extra frame from bombcurs.shp, unless you replace that SHP file.
  IvanBomb.FlickerRate=


















.. versionadded:: 0.1



LaserThickness
``````````````

:[Weapon]LaserThickness= (integer): Enables the customization of laser
  widths. LaserThickness=



NB: Currently this has the same bugs as the NPatch version, only works
with `IsHouseColor=yes` and have low quality.

.. versionadded:: 0.2



<<<SEPARATOR>>>
