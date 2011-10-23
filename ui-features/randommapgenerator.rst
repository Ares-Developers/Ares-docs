Random Map Generator
~~~~~~~~~~~~~~~~~~~~

Ares lets you create random maps using some new map styles Archipelago
terrain and the Desert tileset.

The RMG will now place bridges at random on maps that include rivers.
Random Map Generator enhancements:

A new checkbox 'Place Urban Areas' allows the user to add an
assortment of streets and urban combat buildings at random spots
throughout the generated map. The objects placed by this feature can
be modified by adding the heading " `[URBAN]`" in the `rgdmd.ini`
file, and adding the following lists after `Structure=, Vehicles=` and
` Infantry=` respectively:


+ Structures: CABUNK01, CABUNK02, CAARMY01, CAARMY02, CAARMY03,
  CAARMY04, CACHIG03, CANEWY01, CANEWY14, CANWY09, CANWY26, CANWY25,
  CATEXS07
+ Vehicles: TRUCKA, TRUCKB, COP, EUROC, SUVW, SUVB, FTRK, AMBU
+ Infantry: CIV1, CIV2, CIV3, CIVA, CIVB, CIVC


Place Urban Areas option. Bridges over rivers. New terrain style:
Archipelago. New tileset: Desert. NB: Urban areas generated in the
minimap preview do not always correspond to content generated ingame,
especially in Desert maps this is still being investigated.
In addition, there are reports of this feature not working at all with
certain settings. (Known issue: `#794`_)

.. versionadded:: 0.1



<<<SEPARATOR>>>
