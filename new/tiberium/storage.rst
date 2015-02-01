Storage and Silos
`````````````````

In the earlier games, tiberium and ore were not converted to credits directly.
Instead, the resouces were dumped at the refiniery, and then stored in silos.
This feature was not used in :game:`Red Alert 2` and wasn't working any more.
:game:`Ares` restores the Storage feature.

Bonus money created by ore purifiers is always stored on the bank account
instead of in the silos. This is because the bonus is calculated in tiberium
bails, which would count against storage. When the silo is destroyed, this bonus
money would be placed on the map, which would create tiberium out of nothing.

.. warning:: Storage on undeployable refineries like the Slave Miner is not
  supported. Slave Miners cannot provide storage space, because it is lost
  whenever the building undeploys.

.. index: Refineries; Storage logic has been restored.

.. versionadded:: 0.5


Enabling Storage
----------------

:tag:`Storage` works as it did in :game:`Tiberian Sun`. For reasons of backwards
compatibility you have to use one new tag on a building where tiberium is
dumped:

:tagdef:`[BuildingType]Refinery.UseStorage=boolean`
  Whether the refinery building will store the Tiberium instead of converting it
  to money directly. Tiberium that is converted directly does not require
  storage space. Defaults to :value:`no`.


EVA Notice
----------

In case the storage capacity is either depleted or nearly so, EVA will warn the
player by giving a :value:`EVA_SilosNeeded` notice.

.. note:: The game does not have this EVA message defined and has no audio files
  for it. You have to add them before you can use them.

.. versionadded:: 0.5


Text Message
------------

Complimentary to the EVA event it is possible to show a test message.

:tagdef:`[General]Message.SilosNeeded=csf label`
  Set this to a text that shall be printed whenever the Silos Needed warning
  occurs. You cannot unset this later. If you want to disable this message in a
  game mode or map, you will have to a label of an empty text. Defaults to
  no message.

.. versionadded:: 0.9


:captiontag:`PipScale=Tiberium`
-------------------------------

:value:`Tiberium` is again supported as a valid :tag:`PipScale` value. For
buildings with positive :tag:`Storage`, the pips will show the currently used
storage space compared to the overall space of that building. Ore will show as
yellow pips, gems as blue ones.

To enable :tag:`PipScale=Tiberium` on buildings with :tag:`Refinery=yes` or
:tag:`ResourceDestination=yes`, you also have to enable
:tag:`Refinery.UseStorage=yes`. This requirement was added because otherwise the
original game would show the tiberium scale for the unmodded refineries, which
have :tag:`PipScale=Tiberium` and valid :tag:`Storage` defined.

.. index: Pips; PipScale=Tiberium

.. versionadded:: 0.5
