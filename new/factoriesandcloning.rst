Factories and Cloning
~~~~~~~~~~~~~~~~~~~~~

Different factories for units (Kennels)
```````````````````````````````````````

:tagdef:`[InfantryOrVehicle]BuiltAt=list of BuildingTypes`
  Units will be kicked out of the first not-busy building the house owns that is
  mentioned in this list. If no :type:`BuildingType` is set, all factories that
  can produce this unit will be checked. Defaults to :value:`none`.

:tagdef:`[BuildingType]Factory.ExplicitOnly=boolean`
  Set this to :value:`yes` to only allow this factory to produce units that
  explicitly mention this :type:`BuildingType` in their :tag:`BuiltAt` list.
  Units with empty :tag:`BuiltAt` lists will not be built here. The effect is
  the same as stating :tag:`BuiltAt` lists on every unit, omitting all factories
  that have this tag set. Defaults to :value:`no`.

  .. quickstart:: To recreate the dog from :game:`Red Alert` that is trained in
    a kennel, set :tag:`[KENN]Factory=InfantryType`,
    \ :tag:`[KENN]Factory.ExplicitOnly=yes`, :tag:`[DOG]BuiltAt=KENN` and update
    the :tag:`[DOG]Prerequisite` to contain :tag:`[KENN]`.


"Cloning Vats" for :type:`VehicleTypes`
```````````````````````````````````````

:tagdef:`[BuildingType]CloningFacility=boolean`
  Defines whether this building will clone all :type:`VehicleTypes` with the
  same :tag:`Naval` setting as itself that are :tag:`Cloneable=yes` and
  :tag:`ClonedAt=none`. This is the :type:`VehicleType` version of the Cloning
  Vats. Defaults to :value:`no`.


Cloning options
```````````````

:tagdef:`[InfantryOrVehicle]Cloneable=boolean`
  Whether or not this infantry or unit can be cloned by :tag:`Cloning=yes`,
  :tag:`CloningFacility=yes` or their respective :tag:`ClonedAt` buildings.
  Defaults to :value:`yes`.

:tagdef:`[InfantryOrVehicle]ClonedAt=list of BuildingTypes`
  Each building of the types mentioned in the list owned by the same house will
  kick out an extra clone of this object for free. If a building is blocked, the
  player will get no refunds. Defaults to :value:`none`.

  .. note:: Cloning will ignore buildings with :tag:`Factory=` set. Note that
    \ :tag:`Factory` is not what causes the units to walk or drive out properly,
    \ :tag:`WeaponsFactory=yes`, :tag:`GDIBarracks=yes`, :tag:`NODBarracks=yes`
    and :tag:`YuriBarracks=yes` are.

  .. note:: If :tag:`ClonedAt` is specified, neither :tag:`Cloning=yes` nor
    \ :tag:`CloningFacility=yes` will clone the object.


.. index:: Factories; Build units from certain factories only.

.. index:: Factories; Clone infantry and tanks in clone facilities.

.. versionadded:: 0.2
