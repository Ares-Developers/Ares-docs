Range Limits
````````````

There are two ways to restrict the targets a super weapon can fire at by range.
One is the distance to the building firing the super weapon at the target, the
second is the distance of a certain unit to the target area, which is called a
designator.

Range around Launch Site
------------------------

Two tags define the range a super weapon can fire in: the maximum range the
target can be away from the super weapon building, and the minimum range, below
which the super weapon cannot fire.

A super weapon can fire at a location, if at least one building providing this
super weapon satisfies both range requirements. If not, the :tag:`NoCursor` is
shown.

.. note:: The AI does not support range checks yet. This might change in the
  future.

:tagdef:`[SuperWeapon]SW.RangeMaximum=float - cell range`
  Distance in cells the target coordinates may be away from a player's building
  providing this super weapon. Values below :value:`0.0` mean type-specific
  default, which usually disables this range check. Defaults to :value:`-1.0`.

:tagdef:`[SuperWeapon]SW.RangeMinimum=float - cell range`
  Distance in cells the target coordinates must be away from a player's building
  providing this super weapon. Values below :value:`0.0` mean type-specific
  default, which usually disables this range check. Defaults to :value:`-1.0`.

.. index:: Super Weapons; Limit minimum and maximum firing range.


Designators
-----------

A designator is a unit that does the reconnaissance and provides a targeting
area around itself. A super weapon requiring a designator can only fire at a
location if at least one designator is in range. If no designator is in range,
the :tag:`NoCursor` is shown.

.. note:: The AI does not support range checks yet. This might change in the
  future.

:tagdef:`[SuperWeapon]SW.Designators=list of TechnoTypes`
  List of units eligible for designating the target location. An empty list
  requires no designator. Defaults to :value:`none`.

:tagdef:`[SuperWeapon]SW.AnyDesignator=boolean`
  Whether any unit is considered a valid designator for this super weapon.
  Overrides :tag:`SW.Designators`. Defaults to :value:`no`.

The designator range can be customized for each :type:`TechnoType` individually.

:tagdef:`[TechnoType]DesignatorRange=integer - cells`
  Range in cells around the unit or structure that becomes targetable by super
  weapons requiring this object as designator. Defaults to
  :tag:`[TechnoType]Sight`.

.. index:: Super Weapons; Designators providing targets.

.. versionadded:: 0.8
