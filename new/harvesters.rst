.. index:: Harvester; Scan and Distance Settings
.. index:: Slave Miner; Scan and Distance Settings
.. index:: Slaves; Scan and Distance Settings

Harvesters, Slave Miners, and Slaves
====================================

The following new tags deglobalize settings that define harvesting behavior like
scan ranges for Harvesters and Slaves and intervals in which to wake up Slave
Miners.

:tagdef:`[TechnoType]Harvester.LongScan=integer - cells`
  Overrides the distance to consider for long scans. For :tag:`Harvester=yes`
  units, defaults to :tag:`[General]TiberiumLongScan`. For Slave Miners,
  defaults to :tag:`[General]SlaveMinerLongScan`.

:tagdef:`[TechnoType]Harvester.ShortScan=integer - cells`
  Overrides the distance to consider for short scans. For :tag:`Harvester=yes`
  units, defaults to :tag:`[General]TiberiumShortScan`. For Slave Miners,
  defaults to :tag:`[General]SlaveMinerShortScan`, and for Slaves defaults to
  :tag:`[General]SlaveMinerSlaveScan`.

:tagdef:`[BuildingType]Harvester.ScanCorrection=integer - cells`
  Overrides the distance to consider better when scooting forward. For Slave
  Miner buildings only. Defaults to :tag:`[General]SlaveMinerScanCorrection`.

:tagdef:`[VehicleType]Harvester.TooFarDistance=integer - cells`
  Overrides the distance to consider too far to reserve a refinery. Requires
  :tag:`Harvester=yes`. Defaults to :tag:`[General]ChronoHarvTooFarDistance` for
  :tag:`Teleporter=yes` units, otherwise to
  :tag:`[General]HarvesterTooFarDistance`.

:tagdef:`[VehicleType]Harvester.KickDelay=integer - frames`
  Overrides the interval in which to wake up the Slave Miner. For Slave Miner
  unis only. Use :value:`-1` to not wake up the Slave Miner automatically.
  Defaults to :tag:`[General]SlaveMinerKickFrameDelay`.

.. versionadded:: 3.0
