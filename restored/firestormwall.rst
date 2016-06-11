==============
Firestorm Wall
==============

The Firestorm Wall and the corresponding super weapon can now be implemented in
:game:`Yuri's Revenge`.

When the Firestorm Defense is activated, all structures owned by the firing
player that have :tag:`Firestorm.Wall=yes` set will emit an energy field,
blocking all hostile projectiles from passing through. The energy field also
destroys any friend or foe unlucky (or stupid) enough to come into direct
contact with active cells.

:tag:`IgnoresFirestorm` is respected and if :value:`yes`, neither units nor
bullets are destroyed when passing an active Firestorm Wall. If an object is
destroyed, crew or passengers will not be ejected.

See the :doc:`Firestorm super weapon </new/superweapons/types/firestorm>` for
more details.

.. versionadded:: 0.1
.. versionchanged:: 0.C


Defining a Wall
~~~~~~~~~~~~~~~

:type:`BuildingTypes` with :tag:`Firestorm.Wall=yes` set will act as a section
of the Firestorm Wall and auto-connect to other nearby pieces (check the
original building's SHP from :game:`Tiberian Sun` to see how the art is
controlled).

:tagdef:`[BuildingType]Firestorm.Wall=boolean`
  Whether this building is part of the Firestorm Defense System. Defaults to
  :value:`no`.


Global Settings
~~~~~~~~~~~~~~~

:tagdef:`[CombatDamage]FirestormWarhead=Warhead`
  The warhead used by active Firestorm Walls to destroy objects. Cannot be
  :value:`none`. Defaults to :tag:`[General]C4Warhead`.

:tagdef:`[General]DamageToFirestormDamageCoefficient=double - multiplier`
  The multiplier for the damage dealt to active Firestorm Walls to convert
  hitpoints to frames to subtract from the Firestorm Defense Super Weapon's
  change time. Higher values reduce remaining active time faster. Defaults to
  :value:`0.0`.

  .. note:: \ :game:`Tiberian Sun` defaulted to :value:`0.1`, but :game:`Ares`
    did not have this feature and just nullified all damage. This is what a
    value of :value:`0.0` still does.

There are four global tags that define the animations played when a Firestorm
Wall is active, or idle, or immolating something.

:tagdef:`[AudioVisual]FirestormActiveAnim=AnimationType`
  The optional animation played randomly on Firestorm Wall sections when active.
  This is drawn in the building's palette. Defaults to :value:`GAFSDF_A`.

:tagdef:`[AudioVisual]FirestormIdleAnim=AnimationType`
  The optional animation played randomly on Firestorm Wall sections when active.
  This is drawn in the building's palette. Defaults to :value:`FSIDLE`.

:tagdef:`[AudioVisual]FirestormGroundAnim=AnimationType`
  The animation to display when an active Firestorm Wall destroys an object on
  or close to the ground. This is drawn in the animation palette. Defaults to
  :value:`FSGRND`.

:tagdef:`[AudioVisual]FirestormAirAnim=AnimationType`
  The animation to display when an active Firestorm Wall destroys an object in
  the air. This is drawn in the animation palette. Defaults to :value:`FSAIR`.


Firestorm Map Actions
~~~~~~~~~~~~~~~~~~~~~

:game:`Ares` restores the two map actions related to the Firestorm Defense from
:game:`Tiberian Sun`. Map actions 92 and 93 activate and deactivate the
Firestorm Walls unconditionally, and while it is active from these map actions,
it will not drain the charge and thus stay active indefinitely.

If a building providing the Firestorm super weapon owned by the house is
destroyed, loses power or goes offline due to other game logics, the Firestorm
Defense is turned off like usual.

.. note:: These map actions are only supported for non-human controlled houses.

.. index:: Map Actions; Firestorm related actions 92 and 93 restored
