versionify
==========

A simple python script to backup and create versions of files.

Known issues:
* Doesn't support mounted network shares if they are not mapped to a drive.
* Creates a "lib" directory in the SendTo folder in addition to the versionify.exe.

How to Install

1. Run [/blob/master/dist/versionify-0.1-amd64.msi](versionify-0.1-amd64.msi)

How to Use

When you want to create a backup version of a file on Windows, right click on the file, and select
"versionify.exe" from the SendTo menu.

A backup of the file will be created in an Old Versions directory with the file name, your initials,
and a time stamp.