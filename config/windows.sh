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

echo_ok "Configuring windows development environment..."

mkdir -p ~/tmp
git config --add color.ui auto

########################################
# Set env.PATH on Windows
########################################
echo 'WScript.Echo CreateObject( "WScript.Shell" ).Environment("SYSTEM")("path")' > ~/tmp/getpath.vbs
export USER=`whoami`
export PATH_UNEXPAND=`cscript.exe //NoLogo c:/cygwin/home/$USER/tmp/getpath.vbs`

if echo $PATH_UNEXPAND | grep Python27
then
    echo_ok "Already added C:/Python27 to PATH in Windows environment."
else    
    setx PATH "$PATH_UNEXPAND;C:\Python27;C:\Python27\Scripts" /M
    echo_err ""
    echo_err "Added c:\Python to PATH in Windows environment."
    echo_err "Restart cygwin environment as administrator and run this script again..."
    echo_err ""
    echo_err "Press any key..."
    read
    exit
fi

########################################
# Intall python-2.7.2
# http://python.org/
########################################
if [ -f /cygdrive/c/Python27/python.exe ]
then
    echo_ok "Already installed Python27"
else
    if [ -f ~/tmp/python-2.7.2.msi ]
    then
        echo_ok "Already downloaded ~/tmp/python-2.7.2.msi"
    else
        wget http://www.python.org/ftp/python/2.7.2/python-2.7.2.msi -O ~/tmp/python-2.7.2.msi
    fi
    
    pushd /cygdrive/c/cygwin/home/$USER/tmp
    msiexec /i python-2.7.2.msi /passive
    popd
    echo_ok "Installed python-2.7.2"
fi

########################################
# Intall wxPython2.9-win32-2.9.3.1
# http://www.wxpython.org/
########################################
if [ -f /cygdrive/c/Python27/Lib/site-packages/wx-2.9.3-msw/wx/__init__.py ]
then
    echo_ok "Already installed wxPython2.9"
else
    if [ -f ~/tmp/wxPython2.9-win32-2.9.3.1-py27.exe ]
    then    
        echo_ok "Already downloaded ~/tmp/wxPython2.9-win32-2.9.3.1-py27.exe"
    else
        wget -O ~/tmp/wxPython2.9-win32-2.9.3.1-py27.exe http://downloads.sourceforge.net/project/wxpython/wxPython/2.9.3.1/wxPython2.9-win32-2.9.3.1-py27.exe
        chmod 755 ~/tmp/wxPython2.9-win32-2.9.3.1-py27.exe
    fi
    pushd ~/tmp
    cmd /C wxPython2.9-win32-2.9.3.1-py27.exe /SILENT
    echo_ok "Installed wxPython2.9"
    popd
fi

########################################
# Intall setuptools
# http://pypi.python.org/pypi/setuptools
########################################
if [ -f /cygdrive/c/Python27/Scripts/easy_install.exe ]
then
    echo_ok "Already installed setuptools"
else
    if [ -f ~/tmp/ez_setup.py ]
    then
        echo_ok "Already downloaded ~/tmp/ez_setup.py"
    else
        wget -O ~/tmp/ez_setup.py http://peak.telecommunity.com/dist/ez_setup.py
    fi
    
    pushd ~/tmp
    python ez_setup.py
    echo_ok "Installed setuptools"
    popd
fi

########################################
# Intall WAF
# http://code.google.com/p/waf/
########################################
if [ -f /usr/local/bin/waf ]
then
    echo_ok "Already installed waf"
else
    if [ -f ~/tmp/]
    then
        "Already downloaded waf-1.6.11"
    else
        wget -O ~/tmp/waf-1.6.11 http://waf.googlecode.com/files/waf-1.6.11
    fi
    
    cp ~/tmp/waf-1.6.11 /usr/local/bin/waf.py
    echo "python c:/cygwin/usr/local/bin/waf.py \$*" > /usr/local/bin/waf
    echo_ok "Installed waf"
fi


wget -O ~/tmp/py2exe-0.6.9.zip http://downloads.sourceforge.net/project/py2exe/py2exe/0.6.9/py2exe-0.6.9.zip

# Clean up after ourselves
rm -rf ~/tmp