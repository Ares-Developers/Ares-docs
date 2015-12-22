Crush Damage
~~~~~~~~~~~~

This feature known from :game:`Dune 2000` has been added to :game:`Yuri's
Revenge`. In the former, running over a Sardaukar trooper squishes the infantry
while also slightly dealing damage to the tank. This way, crushing infantry
comes at a customizable cost.

:tagdef:`[TechnoType]CrushDamage=integer - hitpoints`

:tagdef:`[TechnoType]CrushDamage.Rookie=integer - hitpoints`

:tagdef:`[TechnoType]CrushDamage.Veteran=integer - hitpoints`

:tagdef:`[TechnoType]CrushDamage.Elite=integer - hitpoints`
  The damage dealt to the unit crushing this object. Defaults to :value:`0`.
  
  .. note:: When the base tag is defined, it will always reset all previous
    veterancy values, and then re-read the veterancy values from the same file.

:tagdef:`[TechnoType]CrushDamage.Warhead=Warhead`
  The warhead used to deal crush damage when this unit is crushed. Defaults to
  :tag:`[General]C4Warhead`.

.. index:: Crush; Crush damage when running over infantry or vehicles

.. versionadded:: 0.A
