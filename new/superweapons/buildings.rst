Building Options
````````````````

.. index::
  Super Weapons; Unlimited super weapons on buildings
  Buildings; Provide unlimited super weapons

Multiple Super Weapons on a Building
------------------------------------

:tagdef:`[BuildingType]SuperWeapons= list of SuperWeaponTypes`
  Comma separated list of :type:`SuperWeaponTypes` which are granted by this
  building in addition to the ones defined as :tag:`SuperWeapon` and
  :tag:`SuperWeapon2`. Defaults to :value:`none`.

  Each individual super weapon can be :doc:`granted conditionally
  </new/superweapons/availability>`. The first available super weapon determines
  the EVA event played when a building of this type is placed, and its charge
  state is indicated by the building animations.

  .. note:: This feature primarily supports providing access to additional super
    weapons. Note that :tag:`SuperWeapon` and :tag:`SuperWeapon2` are still
    considered special, and not all aspects of the logic have been expanded.

.. versionadded:: 0.9


.. index:: Super Weapons; Building animations played correctly

Building Animations
-------------------

Buildings can display specific animations for when the attached super weapon is
charging, is nearly charged (1 minute remaining in the vanilla game), is ready
to be fired, and when it fires. However, in :game:`Yuri's Revenge`, these
animations only work properly for the original super weapons. In :game:`Ares`,
these will work for any super weapon. 

.. versionadded:: 0.1
