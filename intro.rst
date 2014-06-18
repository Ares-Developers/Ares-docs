Introduction
============
:game:`Ares` is the new tool to extend the capabilities of :game:`Yuri's
Revenge`. It was conceived by pd near the end of 2007, and is currently in an
early development and testing cycle.

This documentation is aimed primarily at :game:`Ares` testers, as :game:`Ares`
is a work in progress and subject to many further changes. However, the
documentation is also aimed at mod authors wishing to make use of the new
functionality that :game:`Ares` offers.

:game:`Ares` is incorporated into :game:`Yuri's Revenge` via the use of
:game:`Syringe`, a program developed by pd to 'inject' DLL code into a running
executable without modifying the executable itself. In this case, the
:game:`Ares` DLL is injected into the :game:`Yuri's Revenge` 1.001 main
executable, :file:`gamemd.exe`.

:game:`Syringe` can be run directly via a command line prompt, or automatically
using :game:`Launch Base`. See the respective documentations of those programs
for further details.

Compatibility Notes
~~~~~~~~~~~~~~~~~~~
RockPatch/NPatch
----------------
:game:`Ares` is not intended to be used in conjunction with any third party
patch that modifies the executable of the game. :game:`Ares` works by having
its code injected into :game:`Yuri's Revenge` at very specific points, and
modifications to the executable change the locations of these points. This would
lead to :game:`Ares`'s code being injected in the wrong places, leading to
unforeseeable, bad consequences.

Comodo Internet Security
------------------------
Commendably, :game:`Comodo Internet Security` actually complains when one
program tries to modify another at runtime, unlike other anti-virus products,
which happily let it happen. Unfortunately, this is exactly the way
:game:`Syringe`/:game:`Ares` works, making it a so-called "false positive".

In order for :game:`Syringe`/:game:`Ares` to work with :game:`Comodo Internet
Security`, you have to make the following changes to Comodo's settings
(`courtesy of eva-251
<http://forums.renegadeprojects.com/showthread.php?tid=1714&pid=17592#pid17592>`_):

#. :file:`gamemd.exe` and :file:`Syringe.exe` need to be in the "Trusted Files"
   list.
#. Under "Computer Security Policy" -> "Defense+ Rules", :file:`gamemd.exe` and
   :file:`Syringe.exe` need to be marked as "Installer or Updater".
#. "Defense+ Settings" -> "Execution Control Settings" -> "Detect shellcode
   injections" should be checked.
#. Under "Defense+ Settings" -> "Execution Control Settings" -> "Exclusions:"
   add :file:`Syringe.exe`, :file:`Ares.dll`, :file:`Ares.dll.inj`,
   :file:`gamemd.exe`.

This should allow :game:`Syringe`/:game:`Ares` to work properly.

.. warning:: For your own safety, do not *ever* run a Windows-computer without
	active anti-virus protection. Computer worms actively scan the Internet
	for vulnerable machines, so even if you don't do anything, you could
	be infected within minutes.

ZoneAlarm
---------
:game:`ZoneAlarm` is known to prevent :game:`Syringe`/:game:`Ares` from
starting. In case :game:`Yuri's Revenge` does not start (:game:`Syringe`
closes immediately), add :file:`gamemd.exe` and :file:`Syringe.exe` to the
exceptions list.

If this does not help, try to stop the service called :game:`ZoneAlarm
ForceField Service` (:file:`ISWSVC.exe`). This is not recommended and you
should re-enable the service as quickly as possible. `Thanks to FS-21
<https://bugs.launchpad.net/ares/+bug/1090588/comments/3>`_.


Known Major Issues
~~~~~~~~~~~~~~~~~~
Save Games
----------
:game:`Ares` does not support loading save games or scripted IPB videos that
were created with any other version of the game than the very same version of
:game:`Ares` (not even the original :game:`Yuri's Revenge` save games are
supported).

.. note:: Even adding load/save functionality for the exact same :game:`Ares`
	version is a huge and complex undertaking, so while the developers would like
	to add loading and saving one day, it will not happen in the foreseeable
	future.


Known Minor Issues
~~~~~~~~~~~~~~~~~~
Solid Buildings vs. Invisible Projectiles
-----------------------------------------
The SolidHeight/Solid Buildings functionality does not work with
invisible projectiles yet. (`Issue #888
<http://bugs.renegadeprojects.com/view.php?id=888>`_)

Required Changes For Mods Using Ares
====================================
Unfortunately, :game:`Ares` will not simply "work" without changes to the
original game files. The reason for this is that maintaining compatibility with
the original game files whilst still offering the enhancements that are
:game:`Ares`' raison d'être would make implementing :game:`Ares` features
(both for us, the developers, and you, the mod author) considerably more
complex, ultimately wasting time that would be better spent on other tasks.

This section details the modifications you'll most likely need to make to ensure
your mod does not receive any unexpected changes from simply being run whilst
:game:`Ares` is active.

In future these changes will be provided as extensions to the standard files
that are included with the :game:`YR Unofficial 1.002 Mini-Patch Developer's
Pack`.

artmd.ini
~~~~~~~~~
:tag:`[TELE]SecondaryFireFLH=85,0,130`
	See :doc:`/bugfixes/type2/radbeamsandwavesusingthewrongflh`.

bombcurs.shp
~~~~~~~~~~~~
The :file:`bombcurs.shp` animation needs to have its last frame removed if you
don't want to see the previously unused skull image. See
:ref:`IvanBomb.FlickerRate <custom-ivan-bombs>`.

ares.mix
~~~~~~~~
Mods should not include their own version of :file:`ares.mix`. This new MIX file
is bundled with :game:`Ares` to provide any new/modified files that :game:`Ares`
changes/additions rely on. This MIX file presently includes:

:file:`ares.csf` includes a few new strings:

+ `GUI:SelectCampaign=Select your Campaign`
+ `GUI:PlayMission=Play`
+ `GUI:UrbanAreas=Create Urban Areas`
+ `Name:Desert=Desert`
+ `STT:RMGUrbanAreas=Choose whether urban areas will be present on the map.`
+ `STT:MultiEngineer=Engineers can capture damaged buildings only.`
+ `STT:PlayerColorLilac=Choose this to be lilac.`
+ `STT:PlayerColorLightBlue=Choose this to be light blue.`
+ `STT:PlayerColorLime=Choose this to be lime.`
+ `STT:PlayerColorTeal=Choose this to be teal.`
+ `STT:PlayerColorBrown=Choose this to be brown.`
+ `STT:PlayerColorCharcoal=Choose this to be dark grey.`
+ `TXT_COMMAND_DISABLED=The %s command is not available.`
+ `TXT_RELEASE_NOTE=` (empty text)
+ `TXT_SCRNCAP_DESC=Take a snapshot of the game screen. (Saved as
  'SCRN.date-time.BMP' file in Red Alert 2 run directory.)`
+ `TXT_RELEASE=Launch`
