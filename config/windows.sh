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

function download()
{
    local filename="$(basename "$1")"

    if [ -f ~/tmp/$filename ]
    then
        echo_ok "Already downloaded $filename"
    else
        wget -O ~/tmp/$filename --no-check-certificate $1
        chmod 755 ~/tmp/$filename
    fi
}

echo_ok "Configuring windows development environment2..."

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
    echo_err "Added c:\Python27 to PATH in Windows environment."
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
    download "http://www.python.org/ftp/python/2.7.2/python-2.7.2.msi"
    
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
    download "http://downloads.sourceforge.net/project/wxpython/wxPython/2.9.3.1/wxPython2.9-win32-2.9.3.1-py27.exe"

    pushd ~/tmp
    cmd /C wxPython2.9-win32-2.9.3.1-py27.exe /SILENT
    echo_ok "Installed wxPython2.9"
    popd
fi

########################################
# Intall setuptools
# http://pypi.python.org/pypi/setuptools
########################################

# Need to use this instead of what I wrote on 3 lines below
if [ -f /cygdrive/c/Python27/Scripts/easy_install.exe ]
then
    echo_ok "Already installed setuptools"
else
    download "http://pypi.python.org/packages/2.7/s/setuptools/setuptools-0.6c11.win32-py2.7.exe"
    
    pushd ~/tmp
    cmd /C  setuptools-0.6c11.win32-py2.7.exe
    popd
    
    echo_ok "Installed setuptools"
fi


########################################
# Intall WAF
# http://code.google.com/p/waf/
########################################
if [ -f /usr/local/bin/waf ]
then
    echo_ok "Already installed waf"
else
    download "http://waf.googlecode.com/files/waf-1.6.11"
    
    cp ~/tmp/waf-1.6.11 /usr/local/bin/waf.py
    echo "python c:/cygwin/usr/local/bin/waf.py \$*" > /usr/local/bin/waf
    echo_ok "Installed waf"
fi

########################################
# Intall py2exe
# http://www.py2exe.org
########################################

if [  -f /cygdrive/c/Python27/Lib/site-packages/py2exe/__init__.py ]
then
    echo_ok "Already installed py2exe"
else
    download "http://sourceforge.net/projects/py2exe/files/py2exe/0.6.9/py2exe-0.6.9.win32-py2.7.exe"
    
    pushd ~/tmp
    chmod 755 py2exe-0.6.9.win32-py2.7.exe
    cmd /C py2exe-0.6.9.win32-py2.7.exe
    echo_ok "Installed py2exe"
    popd
    
#    echo_err "Press any key after py2exe is installed..."
#    read
fi

########################################
# Intall pyInstaller
# http://www.py2exe.org
########################################
if [  -f /cygdrive/c/pyinstaller-1.5.1/pyinstaller.py ]
then
    echo_ok "Already installed pyInstaller"
else
    download "https://github.com/downloads/pyinstaller/pyinstaller/pyinstaller-1.5.1.tar.bz2"
    
    pushd /cygdrive/c
    tar -xjvf ~/tmp/pyinstaller-1.5.1.tar.bz2
    popd
    
    echo_ok "Installed pyInstaller"
fi


########################################
# pywin32
# http://sourceforge.net/projects/pywin32/files/
########################################
if [ -f /cygdrive/c/Python27/Lib/site-packages/win32com/__init__.py ]
then
    echo_ok "Already installed pywin32"
else
    download "http://downloads.sourceforge.net/project/pywin32/pywin32/Build%20217/pywin32-217.win32-py2.7.exe"
    
    pushd ~/tmp
    cmd /C pywin32-217.win32-py2.7.exe
    popd
fi


########################################
# Microsoft DLL
########################################


# Download the MSV dll to bundle python py2exe
#wget -O ~/tmp/vcredist_x86.exe "http://download.microsoft.com/download/1/1/1/1116b75a-9ec3-481a-a3c8-1777b5381140/vcredist_x86.exe"
#chmod 755 ~/tmp/vcredist_x86.exe
#pushd ~/tmp
#cmd /C vcredist_x86.exe /qb!
#popd ~/tmp


#http://www.microsoft.com/download/en/details.aspx?displaylang=en&id=29

# Clean up after ourselves
#rm -rf ~/tmp
