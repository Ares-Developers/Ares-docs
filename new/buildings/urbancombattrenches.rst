Urban Combat - Trenches
~~~~~~~~~~~~~~~~~~~~~~~

This section covers several new features that were designed together in order to
allow mod authors to add occupiable trenches to the game. These features do not
all have to be used together to implement trenches though - each feature has
been designed to be customizable and can be used separately.

.. note::  This means that these individual features do not distinguish between
  buildings that are a trench and buildings that are not. It is important that
  you understand how each new flag works - both on its own and in conjunction
  with other trench-related flags.

.. index:: Buildings; Numerous features added to support trenches.


Pass Through
````````````

Urban Combat buildings can now specify what percentage of attacks against them
will 'pass through' to the occupants inside -- damaging them rather than the
building itself.

:tagdef:`[BuildingType]UC.PassThrough=float - chance`
  The percentage of shots that will pass through to the occupants (and therefore
  not damage this building). Defaults to :value:`0%` (i.e. all shots damage the
  building / no shots damage the occupants). When there are no occupants inside
  then :tag:`UC.PassThrough` will be ignored (i.e. all shots damage the
  building).
:tagdef:`[BuildingType]UC.FatalRate=float - chance`
  In the event that a shot has passed through, the percentage of those shots
  that will instantly kill one occupant, disregarding the weapon entirely.
  Defaults to :value:`0%`.
:tagdef:`[BuildingType]UC.DamageMultiplier=float - multiplier`
  If a shot has passed through but isn't necessarily fatal then one occupant
  will be damaged. The damage dealt by the weapon will be multiplied by
  :tag:`UC.DamageMultiplier`. Defaults to :value:`100%` (i.e. no change to the
  damage dealt by the weapon).
:tagdef:`[Projectile]SubjectToTrenches=boolean`
  Whether or not this projectile will override the normal
  :value:`UC.PassThrough` chance on targeted buildings. If the projectile has
  :tag:`SubjectToTrenches=no` set, and the target building has
  :tag:`UC.PassThrough` set greater than zero, then the building will be treated
  as if it had :tag:`UC.PassThrough=100%`, when hit by this projectile. If
  :tag:`SubjectToTrenches=yes` is set (default), then the normal
  :tag:`UC.PassThrough` chance will be used when the building is hit by this
  projectile.

:tag:`SubjectToTrenches` was very much intended for trenches - a Grenadier, for
example, would easily be able to drop their grenade into an open trench and
would therefore definitely harm the occupants.

.. note:: The name :tag:`SubjectToTrenches` is misleading if you are not
  thinking about trenches. This has an effect on all occupiable buildings with
  \ :tag:`UC.PassThrough` > 0%.

.. image:: /images/subjecttotrenches.png
  :alt: Illustration of different SubjectToTrenches values
  :align: center

.. image:: /images/subjecttotrenches_passthrough.png
  :alt: Illustration of different UC.PassThrough values
  :align: center

.. index:: Buildings; Weapons can be made to pass through urban combat buildings
  to the occupants inside (including fatal chance and damage modifier).

.. versionadded:: 0.1


Squatters' Rights
`````````````````

You can now specify that Battle Bunkers, for example, can be captured by enemy
infantry just by having them walk in and garrison the building as if it were
their own.

:tagdef:`[BuildingType]Bunker.Raidable=boolean`
  Whether or not this building can be garrisoned by an enemy player's infantry,
  provided the building is not already occupied.


If :tag:`Bunker.Raidable=yes` is set and the building is empty then the building
can be garrisoned by any player's infantry. When another player garrisons the
building, ownership is transferred to that player. At this point the building
can only be further garrisoned by the player whose troops are inside. If the
occupants leave the building then ownership of the building is transferred back
to its original owner. Whilst a building is held by a player that is not the
"true" owner, that building cannot be sold.

.. index:: Buildings; Unoccupied player buildings can be garrisoned by enemy infantry.

.. versionadded:: 0.1


.. _`trenches-rubble`:

Advanced Rubble
```````````````

If you really hit a trench hard enough to destroy it you're only doing one of
two things; either you're turning a small hole into a larger hole, or you're
making it collapse. Either way, you don't really remove the trench from the
battlefield - just render it unusable. It will be easier to re-dig a trench
there than on untouched soil, and, on the other hand, you can't just build
there like nothing ever happened.

.. index:: Buildings; Buildings can be converted into a different building on
  destruction (rubble) and back again on repair by an engineer.

Note that Engineers will not be 'used up' by this repair process - they keep
existing outside of the trench. This is very much intended for trenches: an
Engineer would not be repairing/rebuilding an entire building, just re-digging a
trench so his work would not be too exhausting.

.. note:: \ :game:`Ares` enforces the foundations of :tag:`Rubble.Destroyed=`
  and :tag:`Rubble.Intact=` to match those of the original :type:`BuildingType`.
  Custom foundations never match built-in foundations. A fatal error will be
  raised if you do not comply with this requirement and the game will exit.

Advanced Rubble is implemented in a similar way to other upgrade systems in
:game:`Ares`. The first set is for converting a building to rubble:

:tagdef:`[BuildingType]Rubble.Destroyed=BuildingType`
  The new :type:`BuildingType` that this :type:`BuildingType` will transform
  into upon destruction. By default the building will be created with maximum
  :tag:`Strength`. Engineers will always get a repair cursor over the building.
  Buildings that are created via `Rubble.Destroyed` will have the following
  properties forced upon them:

  ::

    Capturable=no
    TogglePower=no
    Unsellable=yes
    CanBeOccupied=no

  .. warning:: Do not create loops using :tag:`Rubble.Destroyed`. This can
    freeze the game. A building cannot be its own rubble, neither directly or
    indirectly over one or more other :type:`BuildingTypes`.

:tagdef:`[BuildingType]Rubble.Destroyed.Remove=boolean`
  Whether the building should just disappear instead of being converted to
  rubble. Overrides :tag:`Rubble.Destroyed`. Defaults to :value:`no`.

:tagdef:`[BuildingType]Rubble.Destroyed.Owner=enumeration default|civilian|special|neutral`
  The country the destroyed building will belong to. :value:`default` is the
  current owner, :value:`civilian` is the first country from the side called
  :value:`Civilian`, :value:`special` and :value:`neutral` are the countries
  named :value:`Special` and :value:`Neutral` respectively. Defaults to
  :value:`default`.

:tagdef:`[BuildingType]Rubble.Destroyed.Strength=integer`
  The health the rubble building is created with. Positive values up to
  :tag:`Strength` are used directly. Negative values down to :value:`-99` are a
  percentage of full health, :value:`-1` meaning 1% of health. All other values
  mean full health. Defaults to :tag:`Strength`.

:tagdef:`[BuildingType]Rubble.Destroyed.Anim=AnimationType`
  An animation played when a building converted to rubble or removed. Defaults
  to :value:`none`.

There is a second set of tags to recover a building from rubble, which mirrors
the first set:

:tagdef:`[BuildingType]Rubble.Intact=BuildingType`
  The new :type:`BuildingType` that this :type:`BuildingType` will transform
  into when it is repaired. The repaired building will be created with 1%
  :tag:`Strength`, unless set otherwise.

:tagdef:`[BuildingType]Rubble.Intact.Remove=boolean`
  Whether the building should just disappear instead of being recovered when an
  Engineer enters. Overrides :tag:`Rubble.Intact`. Defaults to :value:`no`.

:tagdef:`[BuildingType]Rubble.Intact.Owner=enumeration default|civilian|special|neutral`
  The country the recovered building will belong to. :value:`default` is the
  current owner, :value:`civilian` is the first country from the side called
  :value:`Civilian`, :value:`special` and :value:`neutral` are the countries
  named :value:`Special` and :value:`Neutral` respectively. Defaults to
  :value:`default`.

:tagdef:`[BuildingType]Rubble.Intact.Strength=integer`
  The health the recovered building is created with. Positive values up to
  :tag:`Strength` are used directly. Negative values down to :value:`-99` are a
  percentage of full health, :value:`-1` meaning 1% of health. All other values
  mean full health. Defaults to :tag:`-1`, 1% of :tag:`Strength`.

:tagdef:`[BuildingType]Rubble.Intact.Anim=AnimationType`
  An animation played when a building is recovered or removed. Defaults to
  :value:`none`.

.. versionadded:: 0.1
.. versionchanged:: 0.8


Traversing Trenches
```````````````````

A major concept of trenches is the ability for infantry to move from one segment
of a trench to the next, on the basis that adjacent segments are connected and,
in essence, the same trench.

:tagdef:`[BuildingType]IsTrench=string - trench type ID`
  Specifies a unique name for this particular trench so that the game knows that
  it is a trench for traversal purposes, and allows occupants to transfer
  between segments of the same trench type.


For example, let's say you have :tag:`IsTrench=AlliedModern`. You have 2
segments of this trench adjacent to one another and one of these segments is
garrisoned. If you select the garrisoned segment and then position the mouse
cursor over the adjacent segment, you will get an 'enter' cursor over the
adjacent segment. Clicking now with the enter cursor showing will transfer the
occupants from the garrisoned segment into the adjacent segment.

.. note:: There is no special image-handling with :tag:`IsTrench` logic (yet);
  you will not get nice rows of trenches with proper joins/closed off ends like
  you do with, say, walls or Laser Fences. 

.. index:: Buildings; Infantry can jump from one urban combat building to an adjacent one.

.. versionadded:: 0.1



Specifying the occupants of a building
``````````````````````````````````````

You can now specify which infantries are allowed to enter into a building.

:tagdef:`[BuildingType]CanBeOccupiedBy=list of InfantryTypes`
  Lists the units which are allowed to enter to this building.

.. index:: Buildings; Specifying the occupants of a building.

.. versionadded:: 0.2
