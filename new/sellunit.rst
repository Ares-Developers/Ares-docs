.. index:: Buildings; Sell Units

Sell Units
~~~~~~~~~~

With :game:`Ares`, selling units when they dock at buildings like Repair Depots
can be disabled per structure, and specific units can be made unsellable on dock
structures.

:tagdef:`[BuildingType]UnitSell=boolean`
  Whether this building can sell docked units. Human players can click the Sell
  button and move it over the docked unit. The cursor will change to the
  SellUnit cursor. Defaults to :tag:`UnitRepair`.

:tagdef:`[TechnoType]Unsellable=boolean`
  Whether this unit can be sold at :tag:`UnitSell=yes` docking structures.
  Defaults to :tag:`[General]UnitsUnsellable=`.

:tagdef:`[General]UnitsUnsellable=boolean`
  Whether units are by default :tag:`Unsellable=yes` and thus not sellable at
  :tag:`UnitSell=yes` docking structures. Defaults to :value:`no`.

.. versionadded:: 3.0
