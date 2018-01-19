:captiontag:`Type=HunterSeeker`
```````````````````````````````

The Hunter Seeker super weapon known from :game:`Tiberian Sun` has been restored
and expanded. The Hunter Seeker is a :type:`VehicleType` that is launched from a
building and then flys into an enemy object, detonating on impact.

Default values for general tags:

:tagdef:`[SuperWeapon]SW.MaxCount=integer`
  The maximum number of buildings launching a Hunter Seeker. Set to negative
  values for unlimited buildings. Defaults to :value:`1`.
:tagdef:`[SuperWeapon]SW.AITargeting=enumeration`
  Defaults to :value:`HunterSeeker`.
:tagdef:`[SuperWeapon]SW.AffectsHouse=enumeration`
  Specifies the houses targeted. Defaults to :value:`enemies`.
:tagdef:`[SuperWeapon]SW.AffectsTarget=enumeration`
  Specifies which types are targeted. Defaults to :value:`all`.
:tagdef:`[SuperWeapon]EVA.Detected=EVA event`
  Defaults to :value:`EVA_HunterSeekerDetected`.
:tagdef:`[SuperWeapon]EVA.Ready=EVA event`
  Defaults to :value:`EVA_HunterSeekerReady`.
:tagdef:`[SuperWeapon]EVA.Activated=EVA event`
  Defaults to :value:`EVA_HunterSeekerLaunched`.
:tagdef:`[SuperWeapon]Text.Ready=CSF label`
  Defaults to :value:`TXT_RELEASE`.


Hunter Seeker specific tags:

:tagdef:`[SuperWeapon]HunterSeeker.Buildings=list of BuildingType`
  The list of :type:`BuildingTypes` that can launch this Hunter Seeker. Does not
  have to be the same buildings that provide this super weapon. If the player
  does not own a building of any type, the super weapon discharges without
  launching a Hunter Seeker. Defaults to :tag:`[SpecialWeapons]HSBuilding`.
:tagdef:`[SuperWeapon]HunterSeeker.Type=VehicleType`
  The Hunter Seeker unit to spawn. Only set this to use a specific unit instead
  of each players' side default. Defaults to the side's :tag:`HunterSeeker`.
:tagdef:`[SuperWeapon]HunterSeeker.RandomOnly=boolean`
  Whether every enemy object on the map has an equal chance of being targeted by
  the Hunter Seeker. If :value:`no`, non-civilian targets are preferred for
  human players in multiplayer games, and only if no preferred target is found,
  a random target is chosen. Defaults to :value:`no`.


Launches up to :tag:`[SuperWeapon]SW.MaxCount` Hunter Seekers of the specified
type from the firing player's buildings that are valid launch sites. Only one
Hunter Seeker is launched per building.

Hunter Seekers might pick other targets while in flight. They will not target
objects under the effect of the Iron Curtain or objects currently being warped
out of time.

See :doc:`Hunter Seeker </new/hunterseeker>` for information on how to define a
valid Hunter Seeker unit and how to prevent certain :type:`TechnoTypes` to be
targeted. See :ref:`Sides & Countries <sides-hunterseeker>` on how to define a
default Hunter Seeker unit for each side.

.. index:: Super Weapons; HunterSeeker recreated.

.. versionadded:: 0.7
.. versionchanged:: 0.D
