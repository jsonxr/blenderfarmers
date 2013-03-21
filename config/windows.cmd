Cygwin setup.exe options:

 -D --download                          Download from internet 
 -L --local-install                     Install from local directory 
 -s --site                              Download site 
 -R --root                              Root installation directory 
 -q --quiet-mode                        Unattended setup mode 
 -h --help                              print help 
 -l --local-package-dir                 Local package directory 
 -r --no-replaceonreboot                Disable replacing in-use files on next 
                                        reboot. 
 -n --no-shortcuts                      Disable creation of desktop and start 
                                        menu shortcuts 
 -N --no-startmenu                      Disable creation of start menu shortcut 
 -d --no-desktop                        Disable creation of desktop shortcut 
 -A --disable-buggy-antivirus           Disable known or suspected buggy anti 
                                        virus software packages during 
                                        execution.
                                  
<pre>
cd \cygwin_install
setup.exe --quiet-mode --disable-buggy-antivirus --site http://cygwin.mirrorcatalogs.com --packages wget,git,openssh,curl,zip
</pre>

<li>Web/wget</li>
<li>Devel/git</li>
<li>Net/openssh</li>
<li>Net/curl</li>
<li>Archive/zip</li>
