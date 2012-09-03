Hard-coded Unit Properties
~~~~~~~~~~~~~~~~~~~~~~~~~~

The game is hard-coded to do certain things with certain unit IDs.
Namely the `[COW]`, `[DESO]` and `[FV]`. These units can now have said
special properties switched off, and other units can be given these
properties if you want. Hard-coded properties of Cows and Desolators
can be toggled on/off for any infantry.



IsCow
`````

The `[COW]` was hard-coded to play its idle animation more frequently
than other infantry and was also hard-coded to move around randomly.
You can now set `IsCow=yes` on other InfantryTypes or, indeed,
`IsCow=no` on the `[COW]`. IsCow=



IsDesolator
```````````

The `[DESO]` was hard-coded to have different deploy-weapon firing
timing than other units. The change to the timing appears to be
related to the unit's art `Sequence` although the exact effect has not
been investigated. You can now set `IsDesolator=yes` on other
InfantryTypes or, indeed, `IsDesolator=no` on the `[DESO]`.
IsDesolator=



Multiple IFVs / Gunner
``````````````````````

The `[FV]` was the only unit to be checked for the special turret and
weapon flags, such as `SniperTurretIndex`. With Ares, all VehicleTypes
with `Gunner=yes` set will read those flags. This means that you can
now have multiple types of IFV. Custom IFV clones.

.. versionadded:: 0.1



VoiceIFVRepair
``````````````

In Ares you can specify the VoiceIFVRepair tag on any IFV unit.

:[VehicleType]VoiceIFVRepair = ( soundmd entry ): Specifies the
  response this IFV gives when ordered to repair something.

VoiceIFVRepair can be specified on any IFV unit. VoiceIFVRepair=

.. versionadded:: 0.2
