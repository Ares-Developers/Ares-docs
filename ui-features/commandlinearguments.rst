.. index:: Command Line; Don't require the Yuri's Revenge game disk
.. index:: Command Line; Don't play the EA/Westwood logo video

Command Line Arguments
~~~~~~~~~~~~~~~~~~~~~~

:-CD: Allows the game to run without the :game:`Yuri's Revenge` CD. Requires the
  content of the :game:`Yuri's Revenge` CD to be copied to the :game:`Red Alert
  2` directory first. :game:`The First Decade` users already have all the
  required files installed, so no further action has to be taken.
:-NOLOGO: Prevents the EA logo video from playing before the game begins to
  load.
:-LOG: Turns :file:`debug.log` file writing on initially. See :doc:`Internal
  Errors/Debugging </ui-features/internalerrorsdebugging>`.
:-LOG-CSF: Outputs all CSF labels that cannot be found in the language files
  into :file:`debug.log`. Each label is written only once, and prefixed with
  :value:`[CSFLoader]`.
:-STRICT: Throws an Internal Error on game load if a not-necessarily-critical
  error is detected. For example, when you set a flag to a non-empty value that
  cannot be parsed.
  
  .. note:: There are several existing errors in the stock rules that will trip
    this so you will need to clean them up before using it.
:-AI-CONTROL: Enables AI Control feature. Entering this command in the command
  line before opening :game:`Yuri's Revenge` allows the player to assign a
  hotkey to allowing AI control.
  
  .. warning:: This feature was designed primarily for the purposes of offline
    testing and AI design testing. Due to this, feature complexity, lack of
    interest and a change in personnel, please note that this feature is NOT
    officially supported.
:-AFFINITY\:N: Controls which processors the game will run on. :value:`N` is a
  bit mask with one bit for each processor starting with :value:`1` for the
  first, :value:`2` for the second, :value:`4` for the third and so on. If not
  set, :value:`1` is used, meaning the game will run on the first processor
  only. Use :value:`0` to disable this feature.

  .. warning:: Several bits can be combined, like :value:`3` representing the
    first two processors. Usually, the game should run on only one processor
    (that is, :value:`N` being a power of 2), as it is not designed to make use
    of multiple processors.

.. versionadded:: 0.1
