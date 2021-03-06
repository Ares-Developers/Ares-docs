Additional ArmorTypes and Verses
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The new `[ArmorTypes]` section can be used to define new ArmorTypes
for objects (in addition to the 11 existing ArmorTypes; none, flak,
plate, light, medium, heavy, wood, steel, concrete, special_1 and
special_2).


::

    [ArmorTypes]
    		paper=steel
    		magic=11%


`paper=steel` declares a new ArmorType called "paper" whose `Verses`
on each warhead defaults to being the same as that warhead's `Verses`
against the "steel" ArmorType. `magic=11%` declares a new ArmorType
called "magic" whose `Verses` on all warheads defaults to 11%.
These ArmorTypes can be assigned to objects in the same way as the
standard ArmorTypes (case-insensitively). Their susceptibility to
specific warheads can be specified as follows:

:[Warhead]Versus.magic=150%: makes this warhead very good at damaging
  objects with `Armor=magic`. Versus.*=


Note that each individual ArmorType's versus value is specified using
the new "Versus.*" flag, whereas the original 11 ArmorTypes versus
values are specified using the original Verses flag (note Westwood's
misspelling of "versus").

The original `Verses=` flag parser no longer crashes if you specify
less than 11 values. Additional armor types which can default to
reacting like an existing armor type. ArmorTypes

.. versionadded:: 0.1



Warhead Verses' Special Values
``````````````````````````````

The Verses flag has three special-case values that can be used to
define additional behavior:


+ 0% means no force fire, no retaliate, no passive acquire
+ 1% means no retaliate, no passive acquire
+ 2% means no passive acquire


These behaviors can now be toggled on or off independently of the
damage multiplier (so you can now have a warhead that is 100%
effective against an armor type but, at the same time, will not
directly target a unit with that ArmorType).

:[Warhead]Versus.magic.ForceFire= (boolean): Whether or not this
  warhead is allowed to be force-fired on the "magic" ArmorType.
  Versus.*.ForceFire=
:[Warhead]Versus.steel.Retaliate= (boolean): Whether or not this
  warhead is allowed to be used in retaliation against the "steel"
  ArmorType Versus.*.Retaliate=
:[Warhead]Versus.clingfilm.PassiveAcquire= (boolean): Whether or not
  this warhead is allowed to be used to attack the "clingfilm" ArmorType
  automatically. Versus.*.PassiveAcquire=


Note Ares' correct spelling of "acquire". Warhead verses special
behaviours can be decoupled from Verses
(ForceFire/Retaliate/PassiveAcquire).

.. versionadded:: 0.1



Immunities
``````````

The original game has a way to make certain units immune to certain
warheads, however this is severely limited. For example, the `[DESO]`
infantry has the flag `ImmuneToRadiation=yes` and the
`[RadBeamWarhead]` warhead has the flag `Radiation=yes`. This means
that the Desolator is immune to damage from the radiation beams fired
by other Desolators. This immunity system has 2 limitations:


+ 1. Only a small handful of working flag pairs exist, and
+ 2. The immunity only prevents the unit from taking damage from the
  warhead. It does not prevent the unit from being targeted. In the
  above example, Desolators can fire at each other ineffectually.


Ares overcomes these limitations with new armor types, as mentioned
above. If you want to have additional 'old-style' immunities that
still allow units to target things they can't damage (e.g. because
they will affect enemies in an area around the target) then you can
create a new armor type that will emulate this as follows:


::

    	[ArmorTypes]
    	flakImmuneToFrost=flak
    		
    	[IceMan]
    	Armor=flakImmuneToFrost
    	Primary=IceBlast
    		
    	[IceBlast]
    	Warhead=IceBlastWH
    		
    	[IceBlastWH]
    	Versus.flakImmuneToFrost=0%
    	Versus.flakImmuneToFrost.ForceFire=yes
    	Versus.flakImmuneToFrost.Retaliate=yes
    	Versus.flakImmuneToFrost.PassiveAcquire=yes


The above settings give the IceMan unit a damage immunity to the
IceMan weapon, even though he can still be attacked by that weapon.



<<<SEPARATOR>>>
