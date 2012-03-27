echo "Configuring windows development environment..."
mkdir ~/tmp

# Intall python
# TODO: Check to see if python27 already installed before we do this
if ls /cygdrive/c/Python27 | grep python.exe
then
    echo "Python27 already installed."
else
    wget http://www.python.org/ftp/python/2.7.2/python-2.7.2.msi -O ~/tmp/python-2.7.2.msi
    msiexec /i ~/python-2.7.2.msi /qn
fi

# PERMANENTLY Set the path of cygwin
echo 'WScript.Echo CreateObject( "WScript.Shell" ).Environment("SYSTEM")("path")' > ~/tmp/setpath.vbs
export USER=`whoami`
export PATH_UNEXPAND=`cscript.exe //NoLogo c:/cygwin/home/$USER/tmp/setpath.vbs`
if echo $PATH_UNEXPAND | grep Python27
then
    echo "Already set."
else    
    setx PATH "$PATH_UNEXPAND;C:\Python27" /M
    exit
fi

# Clean up after ourselves
rm -rf ~/tmp