.. _charge-drain-sw:

.. index:: Super Weapons; Charge to drain ratio for each super weapon

Charge/Drain Super Weapons
``````````````````````````

Instead of one global setting, :value:`Ares` supports customizable
:tag:`ChargeToDrainRatio` settings for each super weapon. All settings here
only apply for super weapons with :tag:`UseChargeDrain=yes` set.

:tagdef:`[SuperWeapon]SW.ChargeToDrainRatio=float multiplier`
  The recharge time multiplied by this value is how long the super weapon will
  stay active. Must not be :value:`0`. Defaults to
  :tag:`[General]ChargeToDrainRatio`.
:tagdef:`[SuperWeapon]SW.Unstoppable=boolean`
  Whether this super weapon can be stopped when active. Otherwise clicks on the
  super weapon's cameo are ignored. Defaults to :value:`no`.

.. note:: Note that :tag:`UseChargeDrain` is supported for the Firewall super
  weapon only. Using it along with any other super weapon types it will lead to
  unexpected results.

.. versionadded:: 0.2
