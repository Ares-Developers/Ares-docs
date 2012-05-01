Additional :type:`ArmorTypes` and :captiontag:`Verses`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The new :tag:`[ArmorTypes]` section can be used to define new :type:`ArmorTypes`
for objects (in addition to the 11 existing :type:`ArmorTypes`; :value:`none`,
\ :value:`flak`, :value:`plate`, :value:`light`, :value:`medium`,
\ :value:`heavy`, :value:`wood`, :value:`steel`, :value:`concrete`,
\ :value:`special_1` and :value:`special_2`).


::

    [ArmorTypes]
    paper=steel
    magic=11%


:tag:`paper=steel` declares a new :type:`ArmorType` called "paper" whose
verses on each warhead defaults to being the same as that warhead's verses
against the "steel" :type:`ArmorType`. :tag:`magic=11%` declares a new
:type:`ArmorType` called "magic" whose Verses on all warheads defaults to 11%.
These :type:`ArmorTypes` can be assigned to objects in the same way as the
standard :type:`ArmorTypes` (case-insensitively). Their susceptibility to
specific warheads can be specified as follows:

:tagdef:`[Warhead]Versus.magic=float - modifier`
	Sets the efficiency of this warhead against the armor called :tag:`magic`.

Note that each individual :type:`ArmorType`'s versus value is specified using
the new :tag:`Versus.*` flag, whereas the original 11 :type:`ArmorTypes` versus
values are specified using the original :tag:`Verses` flag (note Westwood's
misspelling of "versus").

The original :tag:`Verses` flag parser no longer crashes if you specify less
than 11 values.

.. index:: ArmorTypes; Add custom ArmorTypes to warheads.

.. versionadded:: 0.1



Warhead :captiontag:`Verses`' Special Values
````````````````````````````````````````````

The Verses flag has three special-case values that can be used to define
additional behavior:


+ :value:`0%` means no force fire, no retaliate, no passive acquire
+ :value:`1%` means no retaliate, no passive acquire
+ :value:`2%` means no passive acquire


These behaviors can now be toggled on or off independently of the damage
multiplier (so you can now have a warhead that is 100% effective against an
armor type but, at the same time, will not directly target a unit with that
armor type).

:tagdef:`[Warhead]Versus.magic.ForceFire=boolean`
  Whether or not this warhead is allowed to be force-fired on the :tag:`magic`
  :type:`ArmorType`.
:tagdef:`[Warhead]Versus.steel.Retaliate=boolean`
  Whether or not this warhead is allowed to be used in retaliation against the
  :tag:`steel` :type:`ArmorType`.
:tagdef:`[Warhead]Versus.clingfilm.PassiveAcquire=boolean`
  Whether or not this warhead is allowed to be used to attack the
  :tag:`clingfilm` :type:`ArmorType` automatically.


Note :game:`Ares`' correct spelling of "acquire".

.. index:: ArmorTypes; Warhead verses special behaviours can be decoupled from Verses (ForceFire/Retaliate/PassiveAcquire).

.. versionadded:: 0.1



Immunities
``````````

The original game has a way to make certain units immune to certain warheads,
however this is severely limited. For example, the :tag:`[DESO]` infantry has
the flag :tag:`ImmuneToRadiation=yes` and the :tag:`[RadBeamWarhead]` warhead
has the flag :tag:`Radiation=yes`. This means that the Desolator is immune to
damage from the radiation beams fired by other Desolators. This immunity system
has two limitations:


1. Only a small handful of working flag pairs exist, and
2. The immunity only prevents the unit from taking damage from the warhead. It
   does not prevent the unit from being targeted. In the above example,
   Desolators can fire at each other ineffectually.


:game:`Ares` overcomes these limitations with new armor types, as mentioned
above. If you want to have additional 'old-style' immunities that still allow
units to target things they can't damage (e.g. because they will affect enemies
in an area around the target) then you can create a new armor type that will
emulate this as follows:


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


The above settings give the IceMan unit a damage immunity to the IceBlast
weapon, even though he can still be attacked by that weapon.

.. index:: ArmorTypes; Define your own immunities from certain warheads.

.. versionadded:: 0.1
