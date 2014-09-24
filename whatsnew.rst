==========
What's New
==========

This section contains non-exhaustive lists of features and bugfixes that were
added to a particular version of :game:`Ares`. Internal changes, optimizations
and updates are mentioned here only if they are notable.

.. rubric:: Ares 0.8

+ **Toggle Power** :doc:`keyboard command, customizable cursors and optional
  support for AI players </new/togglepower>`

+ **EM Pulse** :doc:`Super Weapon </new/superweapons/types/empulse>`, with lots
  of enhancements

+ **Super Weapon ranges** :doc:`can be restricted around the firing structures
  and/or around designator units </new/superweapons/range>`

+ **Tech Academies** :doc:`are structures that allow training units with initial
  veterancy </new/academy>`

+ **Forest Fires** :doc:`restored, optional per tree type </new/forestfires>`

+ **Advanced Rubble** :ref:`expanded with customizable owner and inital health
  <trenches-rubble>`

+ **Animation tags** :doc:`Scorch and Flamer have been restored </new/scorchflamer>`

+ **Repair wrenches** can be :doc:`hidden from enemies <new/enemywrench>`, and
  :doc:`no longer reveal cloaked buildings <bugfixes/type2/cloakwrench>`

+ **Unit Delivery** :doc:`placement changed, units guard or hunt, and support
  for giving units to neutral countries </new/superweapons/types/unitdelivery>`


.. rubric:: Ares 0.7

+ **Memory Management** issues were resolved, which results in fewer crashes and
  better support for Windows 8.

+ **Hunter Seeker** :doc:`Super Weapon </new/superweapons/types/hunterseeker>`,
  :doc:`Unit Settings </new/hunterseeker>` and :ref:`Side defaults
  <sides-hunterseeker>`

+ **Drop Pod** :doc:`Super Weapon </new/superweapons/types/droppod>` and
  :doc:`customizable Settings </new/hunterseeker>`

+ **Several weapon additions** like :doc:`Splits and Airburst enhancements
  </new/projectiles/splits>`, :doc:`Ranged </new/projectiles/ranged>` and
  :doc:`ProjectileRange </new/weapons/projectilerange>`, and
  :doc:`BallisticScatter </new/projectiles/ballisticscatter>`

+ **Warheads** that :doc:`prevent units to scatter </new/warheads/general>` when
  hit

+ **Civilian enemies** :doc:`attacked in multiplayer and smarter defense against
  civilian threats </new/civilianenemies>`

+ **Loading themes** for :doc:`campaigns <ui-features/campaignloadscreen>` and
  :doc:`multiplayer </new/sidescountries/uicountry>`

+ **Score screen** :doc:`Graphics and Themes for campaign and multiplayer
  </new/sidescountries/scorescreens>`

+ **Aircraft customization** with :doc:`Smoke animations </new/aircraftsmoke>`
  and :doc:`Airstrike-related voices </new/airstrike>`

+ **MakeInfantryOwner** :doc:`expanded <new/makeinfantryowner>` to work with
  generic infantry death animations

+ **Teams** can :doc:`retaliate </new/teamretaliate>` in case a member is
  attacked

+ **Passable structures** :doc:`units can drive on </new/passablestructures>`
  without side effects like the workarounds have

+ **Dimming deactivated units** :doc:`by reason for deactivation </new/dimming>`

+ **Damage sparks** :doc:`made customizable and enhanced to work with all types
  </new/damageparticlesystems>`


.. rubric:: Ares 0.6

+ **CellSpread** :doc:`not limited to 11 any more, and buildings can define a
  maximum hit count </new/warheads/cellspread>`

+ **Sight** :doc:`values above 10 are supported </new/sight>`

+ **Tech structures** can be :doc:`returned to the neutral house when a player
  is defeated instead of being destroyed </new/techstructures>`

+ **Prerequisites** that :doc:`require a factory build by a certain country
  </new/prerequisites>`

+ **Veterancy from spawns** can be :doc:`awarded to the spawner unit
  </new/customizableveterancy>`

+ **Aircraft** that :doc:`does not spin when crashing </new/crashableaircraft>`

+ **Spawners** now have :doc:`basic support for flying Aircraft Carriers
  </new/spawners>` and are :doc:`allowed to cloak
  </bugfixes/type2/cloakablespawners>`

+ **KillDriver** only applied :doc:`below a certain percentage of health
  </new/killingdrivers>`

+ **Helicopter units** :doc:`animate in air regardless </new/airrate>` of
  whether they are hovering or moving

+ **Drain weapons** power drain amount :doc:`made customizable </new/drain>`

+ **Force Shield** :doc:`customizable per BuildingType </new/forceshield>`


.. rubric:: Ares 0.5

+ **Tiberium features** restored like :doc:`heal </new/tiberium/heal>`,
  :doc:`damage </new/tiberium/damage>`, and :doc:`explosive harvesters
  </new/tiberium/explosive>`, as well as :doc:`spilling on destruction
  </new/tiberium/spill>` and :doc:`Tiberium chain reactions
  </new/tiberium/chainreactions>`, with lots of new settings.

+ **Storage logic** :doc:`has been restored </new/tiberium/storage>`

+ **Cloak enhancements** allow :doc:`units to cloak only if idle, deployed,
  powered, or not at all </new/cloak/cloakstates>`, :doc:`hover units to cloak
  </new/cloak/cloakheight>`, :doc:`customizable cloak sounds
  </new/cloak/cloaksound>`, :doc:`parasites to attack cloaked units
  </new/cloak/general>` and more.

+ **Sensor Arrays** :doc:`work again, with additions </new/cloak/sensorarray>`

+ **Type selection** can now :doc:`consider several unit types as one
  </new/typeselect>`

+ **AttachEffect** expanded with :doc:`settings for decloaking and entering
  transports </new/attacheffect>`

+ **Veterancy** :doc:`insignia can be hidden for enemy players
  </new/customizableinsignia>`

+ **Engineers and Technicians** can be :doc:`defined for each side
  </new/sidescountries/defaultside>`, and :doc:`they can spawn as survivors
  </new/survivors>`

+ **C4 veteran ability** has been restored back :doc:`into working state
  </bugfixes/type2/c4veteranability>`

+ **EVA message** :doc:`in case a unit is destroyed </new/unitlost>`


.. rubric:: Ares 0.4

+ **AttachEffect** feature allows to :doc:`change unit and building stats on the
  battlefield </new/attacheffect>` for a variety of new features and play styles

+ **Super weapon additions** with :doc:`cameos being grayed out
  </new/superweapons/cost>`, and a new :doc:`EVA event for selecting targets
  </new/superweapons/evaevents>`

+ **Aircraft** now :doc:`supports Crashable </new/crashableaircraft>`

+ **Pips** :doc:`support more than only the hardcoded values </new/pips>`

+ **Spy Effects** now support :doc:`PCX cameos and persistent radar reveal
  </new/spybehavior>`, and :doc:`spies can no longer infiltrate allied buildings
  </bugfixes/type1/spyingalliedbuildings>`
  
+ **Gate** :doc:`sounds are now customizable </new/gates>`

+ **Veteran Buildings** :doc:`added to the country options
  </new/sidescountries/defaultcountry>`

+ **Text color** for :doc:`tool tips and message texts customizable
  </new/sidescountries/uiside>`

+ **Chaos Gas** :doc:`prevents the stop command from working now
  </bugfixes/type1/chaosgasandstopcommand>`

+ **Release Note** text can be :doc:`shown on the ingame screen
  </ui-features/releasenote>`

+ **Output all missing CSF labels** :doc:`using a new command line parameter
  </ui-features/commandlinearguments>`


.. rubric:: Ares 0.3

+ **Custom Missiles** like the V3 :doc:`can be added </new/custommissiles>`

+ **Whiteboy bug** has been fixed and now :doc:`more than 74 cameos are
  supported </bugfixes/type2/whiteboybug>`

+ **Cyclic Gattling** :doc:`support to go back to first stage added
  </new/gattlingcycle>`

+ **Unit Delivery** now :doc:`supports Deferment
  </new/superweapons/types/unitdelivery>`

+ **Observer flags** :doc:`customizable for each country
  </new/sidescountries/uicountry>`

+ **FPS counter** can be :doc:`displayed on the ingame screen
  </ui-features/keyboardcommandshotkeys>`
