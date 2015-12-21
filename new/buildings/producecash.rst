Oil Derricks (:captiontag:`ProduceCash`)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Building upgrades now support :tag:`ProduceCashDelay`, :tag:`ProduceCashAmount`
and :tag:`ProduceCashStartup` like normal buildings. Each upgrade manages its
own timer, so they will grant the amount independently of the main building or
other upgrades.

:tag:`ProduceCashStartup` has been expanded to support negative values. The
amount is withdrawn from the capturing player's account. If less than the
specified amount is available, then the building can still be captured or
placed.

.. index:: Tech Structures; Oil Derrick support for building upgrades

.. versionadded:: 0.9
