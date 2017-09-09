MAD Tank Style Relative Damage
``````````````````````````````

This logic is inspired by the MAD Tank known from the :game:`Red Alert` mission
disk :game:`The Aftermath`, where it was used as a large area of effect weapon
that damaged each victim by taking away a share of its health.

Instead of using a fixed damage value, a value relative to the victim's
:tag:`Strength` or current health can be dealt by a warhead. Country armor
multipliers and veterancy bonuses are still applied, as well as :tag:`Verses`.

Relative Damage is not supported on special weapon logics like :tag:`Temporal`
or :tag:`Psychedelic` warheads, and also doesn't support :tag:`ProneDamage` and
:tag:`DeployedDamage` for infantry. Suppressing parasites is also not supported.

:tagdef:`[Warhead]RelativeDamage=boolean`
  Deal damage relative to :tag:`Strength` or current health instead of
  dealing conventional damage. If set to :value:`yes`, the four tags below are
  used depending on target type. If a tag is not defined, no damage is dealt.
  Defaults to :value:`no`.

  .. note:: A dummy :tag:`Damage` is needed on this warhead for targeting, even
    though finally the value is not used. If :tag:`Damage` is negative (like for
    healing weapons), the Relative Damage will be negative also.

:tagdef:`[Warhead]RelativeDamage.Buildings=integer - percent`

:tagdef:`[Warhead]RelativeDamage.Aircraft=integer - percent`

:tagdef:`[Warhead]RelativeDamage.Infantry=integer - percent`

:tagdef:`[Warhead]RelativeDamage.Vehicles=integer - percent`
  The damage defined as percentage from either :tag:`Strength`, if positive, or
  current health, if negative. Supported values range from :value:`-100` to
  :value:`100`. A value of :value:`0` deals no damage. Defaults to :value:`0`.

Relative Damage considers :tag:`Organic=yes` vehicles as infantry and
:tag:`ConsideredAircraft=yes` vehicles as aircraft.

.. index:: Warheads; MAD Tank style Relative Damage

.. versionadded:: 0.E
