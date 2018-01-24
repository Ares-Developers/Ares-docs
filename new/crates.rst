.. index:: Crates; Random money amount

Crate Settings
~~~~~~~~~~~~~~

Money creates do not only award the amounts set in the rules, but also vary the
amount randomly by 900 credits. This can be customized using this new tag.

:tagdef:`[CrateRules]RandomCrateMoney=integer - credits`
  A random money amount between :value:`0` and this value is added on money
  crate bonuses. To make the granted money amount deterministic, set this to
  :value:`0`. Defaults to :value:`900`.

.. versionadded:: 0.C
