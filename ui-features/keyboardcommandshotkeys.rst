Keyboard Commands (Hotkeys)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ares includes several new commands that can be issued in game via the
use of keyboard hotkeys. Note that the labels for these hotkeys are
presently hard-coded, unlike the standard Yuri's Revenge hotkeys
(which use the string table).



Map Snapshot
````````````

A key can be assigned to save a snapshot of the current game as a YRM
map file, which can be edited in FinalAlert 2 YR.
NB: Loading the generated map file in-game causes an Internal Error.
The reason for this is not yet known. If you do encounter it then
please provide the developers with the crash information. Map snapshot
command (saves a YRM map file of the current map).

.. versionadded:: 0.1



Debug Logging
`````````````

A key can be assigned to toggle debug.log writing on and off. See
Internal Errors / Debugging

.. versionadded:: 0.1



Type Data Dumping
`````````````````

A key can be assigned to output some additional information to the
debug.log file (see above). The additional information is written to
the log each time the key is pressed. This includes information such
as AI trigger weighting, so mod authors can see how the AI is
performing over the course of a game.
Note that debug.log file writing must be turned on otherwise the data
will not be written to the file. Type data dumping command (dump type
information to a log file, including AI trigger weights).

.. versionadded:: 0.1



AI Assume Control
`````````````````

Please refer to section "Command Line Arguments" below under the tag:
:-AI-CONTROL:

.. versionadded:: 0.1



<<<SEPARATOR>>>
