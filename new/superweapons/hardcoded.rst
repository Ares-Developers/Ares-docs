.. _sw-postdependent:

Hardcoded Values
````````````````

It made no sense to have the values :tag:`PreClick`, :tag:`PostClick`, and
:tag:`PreDependent` customizable. :game:`Ares` hardcodes these values and they
have no effect any more. Instead, :tag:`SW.PostDependent` takes their place.

:tagdef:`[SuperWeapon]SW.PostDependent=SuperWeapon`
  The super weapon invoked right after firing this super weapon. As in
  :game:`Red Alert 2` the only super weapon using this is the ChronoSphere
  invoking the ChronoWarp. To distinguish between multiple of such super weapons
  you can provide the specific super weapon ID here. For example,
  :tag:`[ChronoSphereSpecial]SW.PostDependent=ChronoWarpSpecial` switches to the
  ChronoWarp type super weapon after you chose the source location.

.. index:: Super Weapons; PreClick, PostClick, and PreDependent are replaced by PostDependent.

.. versionadded:: 0.2
