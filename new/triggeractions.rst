Trigger Actions
~~~~~~~~~~~~~~~

:game:`Ares` adds the following Trigger Actions to :game:`Yuri's Revenge`.


.. index:: Trigger Actions; Activate Firestorm

:captiontag:`Activate Firestorm` (92)
`````````````````````````````````````

Activates the Firestorm Wall sections for the house owning the trigger,
regardless of charge state of the super weapon. The Firestorm will not drain the
charge, but it will shut down once the house loses power.

These map action is only supported for non-human controlled houses.

The format is :value:`92,0,0,0,0,0,0,A`.

.. versionadded:: 0.5



.. index:: Trigger Actions; Deactivate Firestorm

:captiontag:`Deactivate Firestorm` (93)
```````````````````````````````````````

Dectivates the Firestorm Wall sections for the house owning the trigger. Use
this only to turn off a Firestorm that was activated using Trigger Action
:value:`92`.

These map action is only supported for non-human controlled houses.

The format is :value:`93,0,0,0,0,0,0,A`.

.. versionadded:: 0.5



.. index:: Trigger Actions; Auxiliary Power

:captiontag:`Auxiliary Power` (146)
```````````````````````````````````

Permanently adds an amount to the specified house's auxiliary power. Can be
negative to create a drain or remove previously given auxiliary power. Applying
this effect multiple times is cumulative.

The format is :value:`146,11,<house id>,0,0,0,0,<power>`.

.. versionadded:: 3.0



.. index:: Trigger Actions; Kill Drivers

:captiontag:`Kill Drivers Of` (147)
```````````````````````````````````

Kills all drivers of the units that have the trigger attached that contains this
action. This action respects Protected Drivers, Iron Curtain and all the other
mechanisms that prevent drivers being killed.

All affected units will change to the country specified by the house index.
Use :value:`-1` to change the owner to the house called :value:`Special`.

The format is :value:`147,0,<house id>,0,0,0,0,A`.

.. versionadded:: 3.0



.. index:: Trigger Actions; Set EVA Voice

:captiontag:`Set EVA Voice` (148)
`````````````````````````````````

Sets the player's EVA voice. The builtin EVAs are :value:`0`, :value:`1`, and
:value:`2` for Allied, Russian and Yuri respectively. Higher numbers represent
the custom EVAs. Use :value:`-1` to disable EVA.

This implements the :game:`Firestorm` trigger actions :value:`Disable EVA` (102)
and :value:`Enable EVA` (103).

The format is :value:`148,0,<eva index>,0,0,0,0,A`.

.. versionadded:: 3.0



.. index:: Trigger Actions; Set Group

:captiontag:`Set Group` (149)
`````````````````````````````

Sets the group number for the object that triggered this action. This can be
used to make units available for recruitment through :type:`TeamTypes` and
:tag:`TaskForces`.

This implements the :game:`Firestorm` trigger action :value:`Set Group` (104).

The format is :value:`149,0,<group number>,0,0,0,0,A`.

.. versionadded:: 3.0
