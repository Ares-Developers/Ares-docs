.. index::
  Battery; Super weapon to provide auxiliary power

:captiontag:`Type=Battery`
``````````````````````````

According to early previews it was planned for :game:`Tiberian Sun` to include a
battery super weapon that would bridge power outages. As there are no traces of
it anywhere in the game aside from a leftover cameo image, :game:`Ares` uses
some artistic license to implement this super weapon type.

This super weapon uses the Charge/Drain logic: once activated, the effect
will persist for a duration determined by :tag:`SW.ChargeToDrainRatio`, after
which it will automatically shut down and the super weapon will restart its
charging process.

Default values for general tags:

:tagdef:`[SuperWeapon]SW.AITargeting=enumeration`
  Defaults to :value:`LowPower`.

As long as the super weapon is active, the following effects can be applied to
the owning player:

:tagdef:`[SuperWeapon]Battery.Power=integer - power`
  The amount of auxiliary power given to a house while the super weapon is
  active. The power is not provided by any particular building and will thus be
  constant even if the base is heavily damaged. Defaults to :value:`0`.

:tagdef:`[SuperWeapon]Battery.Overpower=list of BuildingTypes`
  The types of buildings this super weapon will temporarily overpower.
  Overpowered buildings use the secondary weapon instead of the primary weapon.
  While this works the same as Tesla Troopers overpowering the Tesla Coil, the
  building types are not required to have :tag:`Overpowerable=yes` set. Defaults
  to :value:`none`.

:tagdef:`[SuperWeapon]Battery.KeepOnline=list of BuildingTypes`
  The types of buildings this super weapon will temporarily keep online. No
  matter the power level, buildings of this type will still be powered up. Can
  be combined with :tag:`Battery.Overpower` to create defenses that are kept
  online and overpowered. Defaults to :value:`none`.

  .. note:: Not all building effects might function while the base has no power,
    but it is possible to keep the radar online even during low power situations
    by adding the building that provides the radar to this list.

.. versionadded:: 3.0
