Hard-coded Unit Properties
~~~~~~~~~~~~~~~~~~~~~~~~~~

The game is hard-coded to do certain things with certain unit IDs. Namely the
:tag:`[COW]` and :tag:`[DESO]`. These units can now have said special properties
switched off, and other units can be given these properties if you want.
Hard-coded properties of Cows and Desolators can be toggled on/off for any
infantry.


.. index:: Infantry; Move around randomly like a cow

:captiontag:`IsCow`
```````````````````

The :tag:`[COW]` was hard-coded to play its idle animation more frequently than
other infantry and was also hard-coded to move around randomly. You can now set
:tag:`IsCow=yes` on other :type:`InfantryTypes` or, indeed, :tag:`IsCow=no` on
the :tag:`[COW]`.

:tagdef:`[InfantryType]IsCow=boolean`
  Defaults to :value:`yes` for :tag:`[COW]`, otherwise to :value:`no`.

.. versionadded:: 0.1


.. index:: Infantry;Desolator special handling

:captiontag:`IsDesolator`
`````````````````````````

The :tag:`[DESO]` was hard-coded to have different deploy-weapon firing timing
than other units to coincide with the unit's art :tag:`Sequence`.

Deployable infantry that is also :tag:`ImmuneToRadiation=yes` has an additional
hardcoded effect which causes the unit to automatically fire at the ground when
deployed, depending on the radiation of the cell the unit is deployed on and the
:tag:`RadLevel` of the infantry's secondary weapon.

You can now set :tag:`IsDesolator=yes` on other :type:`InfantryTypes` or,
indeed, :tag:`IsDesolator=no` on the :tag:`[DESO]`.

:tagdef:`[InfantryType]IsDesolator=boolean`
  Whether the firing timing and deploy behavior is changed for this infantry
  unit as described above. Defaults to :value:`yes` for :tag:`[DESO]`, otherwise
  to :value:`no`.

.. versionadded:: 0.1
.. versionchanged:: 3.0
