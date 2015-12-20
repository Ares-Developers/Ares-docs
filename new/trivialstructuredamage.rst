Trivial Structure Damage
~~~~~~~~~~~~~~~~~~~~~~~~

When a house is suffering low power, buildings can be made to degrade just like
in the earlier games like :game:`Tiberian Dawn` and :game:`Red Alert`. The
buildings lose health while they are unpowered, defined by an amount and an
interval, down to a minimum health. The damage is always dealt by
:tag:`[General]C4Warhead`.

In the earlier games, only buildings consuming power degraded one hitpoint per
interval until reaching yellow health.

:tagdef:`[General]Degrade.Enabled=boolean`
  Whether structures are damaged in intervals defined by :tag:`DamageDelay` when
  a player has low power. Defaults to :value:`no`.

:tagdef:`[General]Degrade.Percentage=double - percentage`
  The health above which this building will continue to degrade during low power
  situations. Buildings with health equal to or below this will not degrade
  further. Defaults to :tag:`[AudioVisual]ConditionYellow`.

:tagdef:`[General]Degrade.AmountNormal=int - hitpoints`
  The damage caused to buildings with :tag:`Power` equal to or greater than
  :value:`0` in low power situations. Defaults to :value:`0`.

:tagdef:`[General]Degrade.AmountConsumer=int - hitpoints`
  The damage caused to buildings with :tag:`Power` less than :value:`0` in low
  power situations. Defaults to :value:`1`.

These global options can be customized per :type:`BuildingType`.

:tagdef:`[BuildingType]Degrade.Percentage=double - percentage`
  The percentage of health this building will degrade to in low power
  situations. A value of :value:`1.0` will not degrade this building, a value of
  :value:`0.0` will make it degrade till complete destruction. Defaults to
  :tag:`[General]Degrade.Percentage`.

:tagdef:`[BuildingType]Degrade.Amount=int - hitpoints`
  The amount of damage this building will receive each interval of
  :tag:`DamageDelay` in low power situations. A value of :value:`0` will not
  degrade this building. Defaults to :tag:`[General]Degrade.AmountNormal` if
  :tag:`Power` is greater than or equal to :value:`0`, otherwise to
  :tag:`[General]Degrade.AmountConsumer`.

Trivial Structure Damage can be enabled or disabled for each house indiviudally.
By default, :tag:`MultiplayPassive=yes` houses are not affected.

:tagdef:`[House]Degrades=boolean`
  Whether buildings owned by this house degrade in low power situations.
  Defaults to :value:`no` for :tag:`MultiplayPassive=yes`, to :value:`no`
  otherwise.

.. index:: Structures; Trivial Structure Damage in low power situations

.. versionadded:: 0.A
