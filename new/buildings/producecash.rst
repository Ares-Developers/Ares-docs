Oil Derricks (:captiontag:`ProduceCash`)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

General Changes
```````````````

Building upgrades now support :tag:`ProduceCashDelay`, :tag:`ProduceCashAmount`
and :tag:`ProduceCashStartup` like normal buildings. Each upgrade manages its
own timer, so they will grant the amount independently of the main building or
other upgrades.

:tag:`ProduceCashStartup` has been expanded to support negative values. The
amount is withdrawn from the capturing player's account. If less than the
specified amount is available, then the building can still be captured or
placed. Also, :tag:`ProduceCashStartup` is no longer granted if a building is
captured by a :tag:`MultiplayPassive=yes` house.

Unlike in the original game, :tag:`ProduceCashStartup` does not have to be
non-null for :tag:`ProduceCashdelay` and :tag:`ProduceCashAmount` to work.

.. index:: Tech Structures; Oil Derrick support for building upgrades

.. versionadded:: 0.9

.. versionchanged:: 0.B


Display Cash Produced
`````````````````````

Buildings producing cash can display the amount they generated as a text
appearing over the building. The text will appear above the building and then
move up slightly.

:tagdef:`[BuildingType]ProduceCashDisplay=boolean`
  Whether the building will show the credits it produced. Not respected on
  upgrades. The setting from the main building type will be used instead.
  Defaults to :value:`no`.

:tagdef:`[AudioVisual]DisplayCreditsDelay=double - minutes`
  The interval between two texts appearing to display how many credits a
  building produced. Until then, the amounts are collected to be displayed after
  the interval passed. Defaults to :value:`0.02`.

At the moment the colors are hardcoded to green for positive amounts and red for
negative amounts. the format is hardcoded to the amount with a plus or minus
sign prepended.

.. warning:: This feature might be expanded or changed in the future. Do not
  take the apparance of these texts for granted. Colors, positions, and movement
  speed might change.

.. index:: Tech Structures; Oil Derrick can show the produced cash amount

.. versionadded:: 0.B
