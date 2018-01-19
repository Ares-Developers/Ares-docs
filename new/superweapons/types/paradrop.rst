:captiontag:`Type=ParaDrop` and :captiontag:`Type=AmerParaDrop`
```````````````````````````````````````````````````````````````

Default values for general tags:

:tagdef:`[SuperWeapon]SW.AITargeting=enumeration`
  Defaults to :value:`ParaDrop`.
:tagdef:`[SuperWeapon]Cursor=mouse cursor`
  Defaults to :value:`ParaDrop`.


The original flags that control the units provided by the generic paradrop super
weapons (:tag:`AllyParaDropInf`, :tag:`SovParaDropInf` and
:tag:`YuriParaDropInf`) and the American paradrop (:tag:`AmerParaDropInf`) only
accept :type:`InfantryTypes`. If you try to include a :type:`VehicleType` via
these lists then the game will create a new :type:`InfantryType` instead - with
the same parameters as the existing :type:`VehicleType` - ultimately resulting
in an invisible :type:`InfantryType` being delivered in the paradrop.

With :game:`Ares`, there are new country-specific flags that override the old
flags and enhance the way paradrops are delivered. :tag:`ParaDrop.Types` will
accept :type:`VehicleTypes` as well as :type:`InfantryTypes`. You can send
multiple airplanes of user-defined type.

Each plane consists of the following properties:

:tagdef:`[SuperWeapon]ParaDrop.Types=list of InfantryTypes and/or VehicleTypes`
  The units that will be paradropped by this super weapon. For
  :tag:`Type=AmerParaDrop` super weapons, this defaults to
  :tag:`AmerParaDropInf=`.

  .. note:: The original flags used to control the paradrop units only accept
    \ :type:`InfantryTypes`. To include :type:`VehicleTypes` in a paradrop you
    must use the new :tag:`ParaDrop.Types` and :tag:`ParaDrop.Num` flags.

:tagdef:`[SuperWeapon]ParaDrop.Num=list of integers`
  The quantity of each corresponding unit (listed against :tag:`ParaDrop.Types`)
  that will be paradropped. For :tag:`Type=AmerParaDrop` super weapons, this
  defaults to :tag:`AmerParaDropNum=`.
:tagdef:`[SuperWeapon]ParaDrop.Aircraft=AircraftType`
  The type of aircraft that will deliver the units. Defaults to the
  corresponding country's :tag:`ParaDrop.Aircraft=`.
:tagdef:`[SuperWeapon]ParaDrop.Count=integer - number of planes`
  This controls how many planes should be send to drop paratroopers. Defaults to
  :value:`1`.


You can define every plane for each country, side or the super weapon
separately. The syntax is as follows:

:tagdef:`[Superweapon]ParaDrop.ID.PlaneX.*=`
  *ID* is name of the country or side. *X* is a positive integer, with no
  leading zeros, starting with *2* up to `Count`. To customize the first plane
  (which will also act as the default plane), do not use the *PlaneX* segment.
  If you want to set the default properties for all sides, do not use the *ID*
  segment. The :tag:`Count` tags can't have a *PlaneX* segment.

The Airplane and its contents will be read separately, thus it is possible to
only define :tag:`Aircraft`; :tag:`Types` and :tag:`Nums` will use the default
value by going though the list until the tags are defined. This also works vice
versa.

:tag:`Types` and :tag:`Nums` have to be defined together; it is not possible to
change the number of units without restating the types.

Values are read in this order, top down. The first value found is used.

#. :tag:`[Superweapon]ParaDrop.Country.PlaneX.*=` (the SW's country-specific
   plane number X)
#. :tag:`[Superweapon]ParaDrop.Side.PlaneX.*=` (the SW's side-specific plane
   number X)
#. :tag:`[Superweapon]ParaDrop.PlaneX.*=` (the SW's default plane number X)
#. :tag:`[Superweapon]ParaDrop.Country.*=` (the SW's country-specific default
   plane)
#. :tag:`[Superweapon]ParaDrop.Side.*=` (the SW's side-specific default plane)
#. :tag:`[Superweapon]ParaDrop.*=` (the SW's default plane)
#. :tag:`[Country]ParaDrop.*=` (the country-specific default plane)
#. :tag:`[Side]ParaDrop.*=` (the side-specific default plane)
#. :tag:`[General]*=` (the Rules' default plane)

Examples:

+ :tag:`[Superweapon]ParaDrop.Russia.Plane3.Types=BORIS` (and proper
  :tag:`Nums`) would replace the contents of the third plane for the country
  :tag:`Russia`.

+ :tag:`[Superweapon]ParaDrop.Nod.Aircraft=SPLANE` would replace the aircraft
  for all Soviet side countries.

.. quickstart:: \ To give all countries the same items, use
  \ :tag:`[Superweapon]ParaDrop.Count=`, :tag:`[Superweapon]ParaDrop.Aircraft=`,
  \ :tag:`[Superweapon]ParaDrop.Types=`, and :tag:`[Superweapon]ParaDrop.Num=`.
  This creates a clone of the American Paradrop.

You can create unlimited new paradrop superweapons with different properties.
:tag:`Type=ParaDrop` and :tag:`Type=AmerParaDrop` are treated equally, but they
differ by the default values. The AI will use both types as in the unmodified
game.

.. versionadded:: 0.2
