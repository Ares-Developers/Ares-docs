.. index:: Map Editors; Support for new Team Scripts, Trigger Events and Actions
.. index:: Final Alert 2; Support for new Team Scripts, Trigger Events and Actions

Editor Support
~~~~~~~~~~~~~~

Before using the new :doc:`Team Scripts </new/scripts>`, :doc:`Trigger Events
</new/triggerevents>` and :doc:`Actions </new/triggeractions>` :game:'Ares'
added, their names and data formats have to be made known to your map editor.

:captiontag:`FinalAlert2`
-------------------------

Merge the :download:`definitions for FinalAlert2 </extras/FADataCode.txt>`
(courtesy of Starkku) into :file:`FAData.ini` to gain access to the new Trigger
Actions and Trigger Events in the editor, so you can comfortably use them in the
maps and missions you create.

To also get access to the new Team Scripts from the user interface, you will
need to use :file:`FA2Ext.dll`, a third party extension dll which is not bundled
with :game:`Ares`.

If you already added new :type:`ParamTypes` to :file:`FAData.ini`, you may have
to update the definitions accordingly before you can use them.

.. versionadded:: 3.0
