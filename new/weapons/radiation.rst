.. index::
  single: Weapons; RadBeam colors, duration, and amplitude
  single: Radiation Beams; Colors, duration, and amplitude

Radiation Beams
~~~~~~~~~~~~~~~

Before :game:`Ares`, Radiation beams could not be customized -- they were always
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
  a random value between :value:`5` and :value:`20`.
:tagdef:`[Weapon]Beam.Amplitude=float`
  The amplitude of the beam (possibly measured in pixels?). Defaults to
  :value:`40.0` as per original RadBeams. The RadEruption effect originally used
  a random value between :value:`100.0` and :value:`500.0`.

.. versionadded:: 0.1
