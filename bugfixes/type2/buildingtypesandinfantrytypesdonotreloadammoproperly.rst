BuildingTypes and InfantryTypes Do Not Reload Ammo Properly
```````````````````````````````````````````````````````````

See `ModEnc://Ammo`_ for exact details of this problem. Put simply,
ammo/reloading logic did not work properly on BuildingTypes or
InfantryTypes and was essentially useless on those object types. Ares
fixes this logic such that these object types will now reload their
ammo properly. Note that AircraftTypes are hard-coded to require
docking to reload. BuildingTypes and InfantryTypes Do Not Reload Ammo
Properly

NB: There are two tags for which this does not work: `Hospital=` and
`Armory=`. Normally, a building will use up its supply of ammo and
then proceed to reload. Setting `Hospital=` and `Armory=` to `yes`
will in effect disable the ability of that building to reload. After
the building heals or promotes the number of units specified under
`Ammo=`, the building will effectively be useless. This occurs even if
the structure has a weapon set under `Primary`. In that circumstance,
any combination of ammo used will contribute to the exhaustion of ammo
without hope of reload.

.. versionadded:: 0.1



<<<SEPARATOR>>>
