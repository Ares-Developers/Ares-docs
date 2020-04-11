Trigger Events
~~~~~~~~~~~~~~

:game:`Ares` adds the following Trigger Events to :game:`Yuri's Revenge`.


.. index:: Trigger Events; Electromagnetic Pulse

Electromagnetic Pulse (62-65)
`````````````````````````````

:value:`62,0,0` Under EMP: Triggers when the attached object is disabled by EMP
(works like Trigger Event :value:`53` in :game:`Tiberian Sun`).

:value:`63,0,<house>` Under EMP By House: Triggers when the specified house
disables the attached object by EMP.

:value:`64,0,0` Removed EMP: Triggers when the attached object is reactivated by
a "healing" EMP.

:value:`65,0,<house>` Removed EMP By House: Triggers when the specified house
reactivates the attached object by a "healing" EMP.

These are all incidental and non-persistent.

When deactivating an object, event :value:`63` is triggered before :value:`62`
and when reactivating, :value:`65` is triggered before :value:`64`. This is to
allow a specific house to take precedence over the general case.

.. versionadded:: 3.0



.. index:: Trigger Events; Enemy In Spotlight Now

Enemy In Spotlight Now (66)
```````````````````````````

:value:`66,0,0` Enemy In Spotlight Now: Triggers when the attached building's
searching spotlight found an enemy. This works like event :value:`54` in
:game:`Firestorm`.

This works like event :value:`Enemy In Spotlight` (35) with the minor difference
that the game will not remember if this event occurred.

This event is incidental and non-persistent.

.. versionadded:: 3.0



.. index:: Trigger Events; Kill Driver

Kill Driver (67+68)
```````````````````

:value:`67,0,0` Driver Killed: Triggers when the driver of the attached object
has been killed.

:value:`68,0,<house>` Driver Killed By House: Triggers when the specified house
kills the driver of the attached object.

Both events are incidental and persistent.

When killing a driver, event :value:`68` is triggered before :value:`67`. This
is to allow a specific house to take precedence over the general case.

.. versionadded:: 3.0



.. index:: Trigger Events; Vehicle Taken

Vehicle Taken (69+70)
`````````````````````

:value:`69,0,0` Vehicle Taken: Triggers when the a driver or Vehicle Thief
enters the attached object.

:value:`70,0,<house>` Vehicle Taken By House: Triggers when a driver or Vehicle
Thief of the specified house enters the attached object.

Both events are incidental and persistent.

When taking a vehicle, event :value:`70` is triggered before :value:`69`. This
is to allow a specific house to take precedence over the general case. Both
trigger before the :value:`Entered By` event.

.. versionadded:: 3.0



.. index:: Trigger Events; Abduction

Abduction (71-74)
`````````````````

:value:`71,0,0` Abducted: Triggers when the attached object is abducted.

:value:`72,0,<house>` Abducted By House: Triggers when the specified house
abducts the attached object.

:value:`73,0,0` Abducts Something: Triggers when the attached object abducts
something.

:value:`74,0,<house>` Abducts Something Of House: Triggers when an attached
object abducts something of the specified house.

These events are all incidental and non-persistent.

When an object is abducted, event :value:`72` is triggered before :value:`71`
and when abducting an object, :value:`74` is triggered before :value:`73`. This
is to allow a specific house to take precedence over the general case.

.. versionadded:: 3.0



.. index:: Trigger Events; Super Weapon Activation

Super Weapon Activation (75+76)
```````````````````````````````

:value:`75,0,<super weapon>` Super Weapon Activated: Triggers when the owning
house fires the super weapon.

:value:`76,0,<super weapon>` Super Weapon Deactivated: Triggers when the owning
house deactivates the super weapon. Only Charge-Drain super weapon types
deactivate.

Both events are incidental and persistent.

.. versionadded:: 3.0



.. index:: Trigger Events; Super Weapon Near Waypoint

Super Weapon Near Waypoint (77)
```````````````````````````````

:value:`77,2,<waypoint>,<super weapon ID>` Super Weapon Activated Near Waypoint:
Triggers when the named super weapon is used near the waypoint.

This event is incidental and persistent.

The definition of *near* is the same as for :value:`Comes Near Waypoint`.

.. versionadded:: 3.0



.. index:: Trigger Events; Reverse Engineered

Reverse Engineered (78)
```````````````````````

:value:`78,2,0,<techno type id>` Reverse Engineered: Triggers while the owning
house has access to reverse engineered techno type.

This event is situational and non-persistent.

This event will trigger for the original type that is put into a reverse
engineering structure, not respecting :tag:`ReversedAs=`. It will however only
trigger if a unit has been reversed successfully, that is, that a new unit
became buildable, respecting :tag:`ReversedAs=`.

.. versionadded:: 3.0



.. index:: Trigger Events; Reverse Engineering

Reverse Engineering (79+80)
```````````````````````````

:value:`79,0,0` Reverse Engineers Anything: Triggers when the attached building
successfully reverse engineers any type.

:value:`80,2,0,<techno type id>` Reverse Engineers Type: Triggers when the
attached building successfully reverse engineers the specific type.

Both events are incidental and persistent.

This event will trigger for the original type that is put into a reverse
engineering structure, not respecting :tag:`ReversedAs=`. It will however only
trigger if a unit has been reversed successfully, that is, that a new unit
became buildable, respecting :tag:`ReversedAs=`.

When reverse engineering, event :value:`80` is triggered before :value:`79`.
This is to allow a specific house to take precedence over the general case.

.. versionadded:: 3.0



.. index:: Trigger Events; House Owns Techno Type

House Owns Techno Type (81+82)
``````````````````````````````

:value:`81,2,<count>,<techno type id>` House Owns Techno Type: Triggers while
the owning house has at least count instances of the specified techno type.

:value:`82,2,<count>,<techno type id>` House Doesn't Own Techno Type: Triggers
while the owning house has fewer than count instances of the specified techno
type.

Both events are situational and non-persistent.

These mirror the :value:`Tech Type Exists` (60) and :value:`Tech Type Doesn't
Exist` (61), but they only check the owning house instead of all houses.

.. versionadded:: 3.0



.. index:: Trigger Events; Attacked Or Destroyed By

Attacked Or Destroyed By (83+84)
````````````````````````````````

:value:`83,0,0` Attacked Or Destroyed By Anybody: Triggers when the attached
object is attacked or destroyed by any attack (even ones without source).

:value:`84,0,<house>` Attacked Or Destroyed By House: Triggers when the attached
object is attacked or destroyed by an attack where the source is owned by a
specific house.

Both events are incidental and non-persistent.

These mirror the :value:`Attacked By Anybody` (6) and :value:`Attacked By House`
(44) trigger events, but they will fire even if the object just has been
destroyed with the first strike, that is, also for fatal hits.

Unlike the original game, the house-specific event will fire first to allow the
more specific event to take precedence over the less specific one.

.. versionadded:: 3.0



.. index:: Trigger Events; Destroyed By House

Destroyed By House (85)
```````````````````````

:value:`85,0,<house>` Destroyed By House: Triggers when the attached object is
destroyed by any attack where the source is owned by a specific house.

This event is incidental and persistent.

The house-specific event :value:`85` will fire before the generic event
:value:`Destroyed By Anybody` (7) to allow the more specific event to take
precedence over the less specific one.

.. versionadded:: 3.0



.. index:: Trigger Events; Techno Type Doesn't Exist More Than

Techno Type Doesn't Exist More Than (86)
````````````````````````````````````````

:value:`86,2,<count>,<techno type id>` Techno Type Doesn't Exist More Than:
Triggers while there are no more than count instances of the specified techno
type.

This event is situational and non-persistent.

.. versionadded:: 3.0



.. index:: Trigger Events; All KeepAlives Destroyed

All KeepAlives Destroyed (87+88)
````````````````````````````````

:value:`87,0,<house>` All KeepAlives Destroyed: Triggers when the specified
house has no more :tag:`KeepAlive=yes` objects.

:value:`88,0,<house>` All KeepAlive Buildings Destroyed: Triggers when the
specified house has no more buildings with :tag:`KeepAlive=yes`.

Both events are situational and persistent.

.. versionadded:: 3.0

