Urban Combat Trenches
~~~~~~~~~~~~~~~~~~~~~

This section covers several new features that were designed together
in order to allow mod authors to add occupiable trenches to the game.
These features do not all have to be used together to implement
trenches though - each feature has been designed to be customizable
and can be used separately.
NB: This means that these individual features do not distinguish
between buildings that are a trench and buildings that are not. It is
important that you understand how each new flag works - both on its
own and in conjunction with other trench-related flags. Numerous
features added to support trenches:



Pass Through
````````````

Urban Combat buildings can now specify what percentage of attacks
against them will 'pass through' to the occupants inside damaging them
rather than the building itself. Weapons can be made to pass through
urban combat buildings to the occupants inside (including fatal chance
and damage modifier).

:[BuildingType]UC.PassThrough= (float - chance): The percentage of
  shots that will pass through to the occupants (and therefore not
  damage this building). Defaults to zero percent (i.e. all shots damage
  the building / no shots damage the occupants). When there are no
  occupants inside then `UC.PassThrough` will be ignored (i.e. all shots
  damage the building). UC.PassThrough=
:[BuildingType]UC.FatalRate= (float - chance): In the event that a
  shot has passed through, the percentage of those shots that will
  instantly kill one occupant, disregarding the weapon entirely.
  Defaults to zero percent. UC.FatalRate=
:[BuildingType]UC.DamageMultiplier= (float - multiplier): If a shot
  has passed through but isn't necessarily fatal then one occupant will
  be damaged. The damage dealt by the weapon will be multiplied by
  `UC.DamageMultiplier`. Defaults to 100% (i.e. no change to the damage
  dealt by the weapon). UC.DamageMultiplier=
:[Projectile]SubjectToTrenches= (boolean): Whether or not this
  projectile will override the normal `UC.PassThrough` chance on
  targeted buildings. If the projectile has `SubjectToTrenches=no` set,
  and the target building has UC.PassThrough set greater than zero, then
  the building will be treated as if it had `UC.PassThrough=100%`, when
  hit by this projectile. If `SubjectToTrenches=yes` is set (default),
  then the normal `UC.PassThrough` chance will be used when the building
  is hit by this projectile. SubjectToTrenches=


SubjectToTrenches was very much intended for trenches - a Grenadier,
for example, would easily be able to drop their grenade into an open
trench and would therefore definitely harm the occupants.
NB: The name 'SubjectToTrenches' is misleading if you are not thinking
about trenches. This has an effect on all occupiable buildings with
UC.PassThrough > 0%.





Squatters' Rights
`````````````````

You can now specify that Battle Bunkers, for example, can be captured
by enemy infantry just by having them walk in and garrison the
building as if it were their own.

:[BuildingType]Bunker.Raidable= (boolean): Whether or not this
  building can be garrisoned by an enemy player's infantry, provided the
  building is not already occupied. Bunker.Raidable=


If `Bunker.Raidable=yes` is set and the building is empty then the
building can be garrisoned by any player's infantry. When another
player garrisons the building, ownership is transferred to that
player. At this point the building can only be further garrisoned by
the player whose troops are inside. If the occupants leave the
building then ownership of the building is transferred back to its
original owner. Whilst a building is held by a player that is not the
"true" owner, that building cannot be sold. Unoccupied player
buildings can be garrisoned by enemy infantry.



Advanced Rubble
```````````````

If you really hit a trench hard enough to destroy it you're only doing
one of two things; either you're turning a small hole into a larger
hole, or you're making it collapse. Either way, you don't really
remove the trench from the battlefield - just render it unusable. It
will be easier to re-dig a trench there than on untouched soil, and,
on the other hand, you can't just build there like nothing ever
happened. Buildings can be converted into a different building on
destruction (rubble) and back again on repair by an engineer.

Advanced Rubble is implemented in a similar way to other upgrade
systems in Ares:

:[BuildingType]Rubble.Destroyed= (BuildingType): The new BuildingType
that this BuildingType will transform into upon destruction. Buildings
that are created via `Rubble.Destroyed` will have the following
properties forced upon them:

::

    Capturable=no
    TogglePower=no
    Unsellable=yes
    CanBeOccupied=no

The building will be created with maximum `Strength`. Engineers will
  always get a repair cursor over the building. Rubble.Destroyed=
:[BuildingType]Rubble.Intact= (BuildingType): The new BuildingType
  that this BuildingType will transform into when it is repaired. The
  repaired building will be created with 1% `Strength`. Rubble.Intact=


Note that Engineers will not be 'used up' by this repair process -
they keep existing outside of the trench. This is very much intended
for trenches: an Engineer would not be repairing/rebuilding an entire
building, just re-digging a trench so his work would not be too
exhausting.
NB: Ares enforces the foundations of `Rubble.Destroyed=` and
`Rubble.Intact=` to match those of the original BuildingType. Custom
foundations never match built-in foundations. A fatal error will be
raised if you do not comply with this requirement and the game will
exit.



Traversing Trenches
```````````````````

A major concept of trenches is the ability for infantry to move from
one segment of a trench to the next, on the basis that adjacent
segments are connected and, in essence, the same trench.

:[BuildingType]IsTrench= (string - trench type ID): Specifies a unique
  name for this particular trench so that the game knows that it is a
  trench for traversal purposes, and allows occupants to transfer
  between segments of the same trench type. IsTrench=


For example, let's say you have `IsTrench=AlliedModern`. You have 2
segments of this trench adjacent to one another and one of these
segments is garrisoned. If you select the garrisoned segment and then
position the mouse cursor over the adjacent segment, you will get an
'enter' cursor over the adjacent segment. Clicking now with the enter
cursor showing will transfer the occupants from the garrisoned segment
into the adjacent segment.
NB: There is no special image-handling with IsTrench logic (yet); you
will not get nice rows of trenches with proper joins/closed off ends
like you do with, say, walls or Laser Fences. Infantry can jump from
one urban combat building to an adjacent one.

.. versionadded:: 0.1



Specifying the occupants of a building
``````````````````````````````````````

You can now specify which infantries are allowed to enter into a
building.

:[BuildingType]CanBeOccupiedBy= (list of InfantryTypes): Lists the
  units which are allowed to enter to this building. CanBeOccupiedBy=

Specifying the occupants of a building.

.. versionadded:: 0.2



<<<SEPARATOR>>>
