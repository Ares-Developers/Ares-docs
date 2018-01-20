Keyboard Commands (Hotkeys)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

:game:`Ares` includes several new commands that can be issued in game via the
use of keyboard hotkeys. Note that the labels for these hotkeys are presently
hard-coded, unlike the standard Yuri's Revenge hotkeys (which use the string
table).


Map Snapshot
````````````

A key can be assigned to save a snapshot of the current game as an YRM map file,
which can be edited in FinalAlert 2 YR.

.. note:: Loading the generated map file in-game causes an Internal Error,
  because the radar preview image is not saved. To circumvent this, add
  \ :tag:`[Preview]Size=0,0,1,1` to the map file.

.. note:: This keyboard can be disabled in release versions of your mod. See
  \ :ref:`Disabling Keyboard Commands <disable-commands>`.

.. index:: Keyboard Commands; Map snapshot command (saves a YRM map file of the current map).

.. versionadded:: 0.1


.. _`debug-logging`:

Debug Logging
`````````````

A key can be assigned to toggle :file:`debug.log` writing on and off. See
:doc:`Internal Errors / Debugging </ui-features/internalerrorsdebugging>`.

.. versionadded:: 0.1



Type Data Dumping
`````````````````

A key can be assigned to output some additional information to the
:file:`debug.log` file (see above). The additional information is written to the
log each time the key is pressed. This includes information such as AI trigger
weighting, so mod authors can see how the AI is performing over the course of a
game. Note that :file:`debug.log` file writing must be turned on otherwise the
data will not be written to the file.

.. note:: This keyboard can be disabled in release versions of your mod. See
  \ :ref:`Disabling Keyboard Commands <disable-commands>`.

.. index:: Keyboard Commands; Type data dumping command (dump type information to a log file, including AI trigger weights).

.. versionadded:: 0.1


AI Base Plan Dumping
````````````````````

To output the current AI players' base plan for debug purposes, you can use this
keyboard command. Each AI player's base plan is dumped into :file:`debug.log`.
This can help diagnose problems in the computer's choice of buildings. Note that
:file:`debug.log` file writing must be turned on otherwise the data will not be
written to the file.

.. note:: This keyboard can be disabled in release versions of your mod. See
  \ :ref:`Disabling Keyboard Commands <disable-commands>`.

.. index:: Keyboard Commands; AI Base Plan data dumping command (see what the AI
  plans to build).

.. versionadded:: 0.1


AI Assume Control
`````````````````

Please refer to section :doc:`Command Line Arguments
</ui-features/commandlinearguments>` under the tag:

:-AI-CONTROL:

.. note:: This keyboard can be disabled in release versions of your mod. See
  \ :ref:`Disabling Keyboard Commands <disable-commands>`.

.. versionadded:: 0.1



FPS Counter
```````````

This keyboard command allows players to display the current frames per second
the game processes, and their total average value. The text is displayed in
white color in the left hand side lower corner of the screen. Pressing the key
again hides the FPS Counter.

.. index:: Keyboard Commands; Display the current and the average frame rate on the screen.

.. versionadded:: 0.3


Toggle Power
````````````

The feature known from :game:`Tiberian Sun` is now accessible from a keyboard
command. See :doc:`Toggle Power </new/buildings/togglepower>`.

.. versionadded:: 0.8


.. _`disable-commands`:

Disabling Keyboard Commands
~~~~~~~~~~~~~~~~~~~~~~~~~~~

It is possible to disable certain debug keyboard commands from
:file:`rulesmd.ini` for the release version of a mod. The affected keyboard
commands are AI Control, Dump Types, Map Snapshot and Dump AI Base Plan.

:tagdef:`[GlobalControls]DebugKeysEnabled=boolean`
  Whether the debug keyboard commands are enabled. Defaults to :value:`yes`.
  If set to :value:`no`, executing a disabled keyboard command will display a
  white text message instead.

The message string displayed to the player is defined by
:value:`TXT_COMMAND_DISABLED`. You can override this string in your language
string file. You may include one (not more) "%s" placeholder, which will be
replaced by the disabled keyboard command's name.

.. warning:: Please note that this is neither a security feature nor any kind of
  real protection from rippers. This function is merely for convenience to not
  make it too easy to extract certain files from the game.

.. versionadded:: 0.2
