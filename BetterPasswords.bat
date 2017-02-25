@ECHO OFF

echo +=====================================================================================================================+
echo +                                                                                                                     +
echo +                                                  BETTER PASSWORDS                                                   +
echo +                                                 by Cillian Collins                                                  +
echo +                                                                                                                     +
echo +=====================================================================================================================+

set /p id="Enter Your Password: "
if defined id if "%id:~5,1%"=="" (
    echo Your passsword must be more than 6 characters.
    echo Please open the batch file again!
    pause
    exit
) else (

echo Success! Loading...
pause
echo Your NEW Password: #%id%%random:~-1%%random:~-1%%random:~-1%%random:~-1%
echo #%id%%random:~-1%%random:~-1%%random:~-1%%random:~-1% >> Password.txt
start notepad "Password.txt"
echo Please find your new password in Password.txt
pause )
