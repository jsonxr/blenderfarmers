########################################
# Colors
########################################
# Foreground Colors
# -----------------
# Black       0;30     Dark Gray     1;30
# Blue        0;34     Light Blue    1;34
# Green       0;32     Light Green   1;32
# Cyan        0;36     Light Cyan    1;36
# Red         0;31     Light Red     1;31
# Purple      0;35     Light Purple  1;35
# Brown       0;33     Yellow        1;33
# Light Gray  0;37     White         1;37
function echo_ok {
    echo -e '\033[1;32m'$*'\033[0m'
}
function echo_err {
    echo -e '\033[1;31m'$*'\033[0m'
}
function echo_warn {
    echo -e '\033[1;33m'$*'\033[0m'
}

echo_ok "Configuring mac development environment..."
mkdir ~/tmp
# This script assumes you've installed Home Brew already
#brew install python

echo_err "You need to set your path to include /usr/local/share/python/"

if [ -d /usr/local/lib/wxPython-2.9.3.1/lib/python2.7/site-packages/wx-2.9.3-osx_cocoa/wx/ ]
then
    echo_ok "Already installed wxPython2.9"
else
    if [ -f ~/tmp/wxPython2.9-osx-2.9.3.1-cocoa-py2.7.dmg ]
    then    
        echo_ok "Already downloaded ~/tmp/wxPython2.9-win32-2.9.3.1-py27.exe"
    else
        wget -O ~/tmp/wxPython2.9-osx-2.9.3.1-cocoa-py2.7.dmg http://downloads.sourceforge.net/project/wxpython/wxPython/2.9.3.1/wxPython2.9-osx-2.9.3.1-cocoa-py2.7.dmg
        pushd ~/tmp
        device=$(hdiutil attach -readonly -noverify -noautoopen "wxPython2.9-osx-2.9.3.1-cocoa-py2.7.dmg" | egrep '^/dev/' | sed 1q | awk '{print $1}')        
        cp /Volumes/wxPython2.9-osx-2.9.3.1-cocoa-py2.7/wxPython2.9-osx-cocoa-py2.7.pkg ~/tmp/wxPython2.9-osx-cocoa-py2.7.pkg
        hdiutil detach ${device}
        popd
    fi
    pushd ~/tmp
    open wxPython2.9-osx-cocoa-py2.7.pkg
    echo_err "The script needs to wait until the wxPython is installed."
    echo_err "Press any key when ready to continue..."
    echo_err ""
    echo_ok "Installed wxPython2.9"
    popd
fi

########################################
# Intall setuptools
# http://pypi.python.org/pypi/setuptools
########################################
pushd ~/tmp
wget http://pypi.python.org/packages/2.7/s/setuptools/setuptools-0.6c11-py2.7.egg
sh setuptools-0.6c11-py2.7.egg
popd