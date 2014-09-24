Tiberian Fiends
~~~~~~~~~~~~~~~

:game:`Tiberian Sun` had wildlife, which was yet more aggressive than :game:`Red
Alert 2`'s cows. Among them was the Tiberian Fiend, which hid in patches of
Tiberium and could attack and heavily damage units and structures on the
battlefield. :game:`Ares` recreates this remarkably nasty piece of fauna.

Refer to `Doggie on ModEnc <http://modenc.renegadeprojects.com/Doggie>`_ to get
a full description of this feature. See :doc:`/new/civilianenemies` to prevent
players to be overrun by Tiberian Fiends without retaliating automatically.

:tagdef:`[InfantryType]Doggie=boolean`
  Whether this unit exhibits Tiberian Fiend behavior: Sitting down on Tiberium
  when in guard mode, aborting attack missions and running for Tiberium when
  badly hurt, and being easily aggravated. Requires :tag:`Crawls=yes`, otherwise
  the unit will not sit down on Tiberium, as well as :tag:`NotHuman=yes` to not
  show human death animations when killed. Defaults to :value:`no`.

.. index:: InfantryTypes; Tiberian Fiends restored, Doggie

.. versionadded:: 0.8
