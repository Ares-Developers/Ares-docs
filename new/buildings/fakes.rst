Fakes
~~~~~

Fakes are buildings known from :game:`Red Alert` which look like their original
counterparts but are weaker and serve no function. There mere purpose is to
hide the location of the real buildings.

Fakes show the string defined by :value:`TXT_FAKE` when selected by the owning
player and its allies, and also by enemies if they infiltrated the building and
it has the :ref:`Reveal Production Spy Effect <spybehavior-revealproduction>`
enabled.

:tagdef:`[BuildingType]Fake=boolean`
  Whether this building is considered a fake. Defaults to :value:`no`.

See :doc:`EnemyUIName </new/enemyuiname>` to find out how to hide the real name
of the building from enemy players.

.. index:: Fakes; Decoy buildings

.. versionadded:: 0.B
