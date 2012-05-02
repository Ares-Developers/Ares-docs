Random Map Generator
~~~~~~~~~~~~~~~~~~~~

:game:`Ares` lets you create random maps using some new map styles - Archipelago
terrain and the Desert tileset.

The RMG will now place bridges at random on maps that include rivers.

Random Map Generator enhancements:

A new checkbox `Place Urban Areas` allows the user to add an assortment of
streets and urban combat buildings at random spots throughout the generated map.
The objects placed by this feature can be modified by adding the heading
:tag:`[URBAN]` in the :file:`rgdmd.ini` file, and adding the following lists
after :tag:`Structure=`, :tag:`Vehicles=` and :tag:`Infantry=` respectively:

:tagdef:`[URBAN]Structures=list of BuildingTypes`
  Defaults to :value:`CABUNK01,CABUNK02,CAARMY01,CAARMY02,CAARMY03,CAARMY04,
  CACHIG03,CANEWY01,CANEWY14,CANWY09,CANWY26,CANWY25,CATEXS07`.
:tagdef:`[URBAN]Vehicles=list of VehicleTypes`
  Defaults to :value:`TRUCKA,TRUCKB,COP,EUROC,SUVW,SUVB,FTRK,AMBU`.
:tagdef:`[URBAN]Infantry=list of InfantryTypes`
  Defaults to :value:`CIV1,CIV2,CIV3,CIVA,CIVB,CIVC`.

.. note:: Urban areas generated in the minimap preview do not always correspond
  to content generated ingame, especially in Desert maps this is still being
  investigated. In addition, there are reports of this feature not working at
  all with certain settings. (Known issue: `#794
  <http://bugs.renegadeprojects.com/view.php?id=794>`_)

.. index:: Random Map Generator; Place Urban Areas option.
.. index:: Random Map Generator; Bridges over rivers.
.. index:: Random Map Generator; New terrain style: Archipelago.
.. index:: Random Map Generator; New tileset: Desert.

.. versionadded:: 0.1
