Sensor Arrays
`````````````

Sensor Arrays are buildings that can detect enemy stealth units and structures,
as well as subterranean unit movements. The feature was introduced along with
Cloak Generators in :game:`Tiberian Sun`, but didn't work correctly in
:game:`Red Alert 2`.

.. index: Sensor Array; Restored and extended.

.. versionadded:: 0.5


Changes
-------

:tag:`SensorArray=yes` uses :tag:`SensorsSight=` as range to detect stealth and
subterranean units, while :game:`Tiberian Sun` reused the Cloak Generator range.
This is also used to draw the radial indicator.

The bug that the sensor stayed active even after the Sensor Array was destroyed
is fixed.

Sensor Arrays were not supposed to be powered or to change owner (by capture or
mind-control) and weren't updated for temporal weapons. All of this should work
now.

Two new EVA warnings have been added, :value:`EVA_CloakedUnitDetected` and
:value:`EVA_SubterraneanUnitDetected`, which are played when a Sensor Array
detects cloaked units or units moving underground respectively.

.. note:: You have to add these EVA voices to :file:`evamd.ini` before you can
  use them. The game does not contain audio files for the three original EVA
  voices.


Suppress Sensor Array Warnings
------------------------------

:tagdef:`[TechnoType]SensorArray.Warn=boolean`
  Whether EVA warnings and radar events should be generated if this type is
  detected. This does not hide the unit or building from the Sensor Array, and
  the object will still become visible. Defaults to :value:`yes`.

.. index: Sensor Array; Disable warnings per type.

.. versionadded:: 0.5
