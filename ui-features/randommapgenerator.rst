.. index:: Random Map Generator; Place urban areas
.. index:: Random Map Generator; Bridges over rivers
.. index:: Random Map Generator; New terrain style: Archipelago
.. index:: Random Map Generator; New tileset: Desert

Random Map Generator
~~~~~~~~~~~~~~~~~~~~

:game:`Ares` lets you create random maps using some new map styles --
Archipelago terrain and the Desert tileset.

The Random Map Generator will now place bridges at random on maps that include
rivers.

Random Map Generator enhancements:

A new checkbox -- `Create Urban Areas` -- allows the user to add an assortment
of streets and urban combat buildings at random spots throughout the generated
map. The objects placed by this feature can be modified by adding the heading
:tag:`[Urban]` in the :file:`rmgmd.ini` file, and adding the following lists:

:tagdef:`[Urban]Structures=list of BuildingTypes`
  Defaults to :value:`CABUNK01,CABUNK02,CAARMY01,CAARMY02,CAARMY03,CAARMY04,
  CACHIG03,CANEWY01,CANEWY14,CANWY09,CANWY26,CANWY25,CATEXS07`.
:tagdef:`[Urban]Vehicles=list of VehicleTypes`
  Defaults to :value:`TRUCKA,TRUCKB,COP,EUROC,SUVW,SUVB,FTRK,AMBU`.
:tagdef:`[Urban]Infantry=list of InfantryTypes`
  Defaults to :value:`CIV1,CIV2,CIV3,CIVA,CIVB,CIVC`.

.. note:: Urban areas generated in the minimap preview do not always correspond
  to content generated ingame, especially in Desert maps. In addition, there are
  reports of this feature not working at all with certain settings.

.. versionadded:: 0.1
