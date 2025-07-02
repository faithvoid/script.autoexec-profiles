import os
import xbmc

# Get the current logged-in user
username = xbmc.getInfoLabel("System.ProfileName").lower().replace(" ", "_")

# Construct the user-specific script filename
autoexec_script = os.path.join(xbmc.translatePath('special://home/scripts/'), 'autoexec-' + username + '.py')

# Check if the script exists and execute it
if os.path.exists(autoexec_script):
    try:
        execfile(autoexec_script)
        xbmc.log("Executed " + autoexec_script, xbmc.LOGINFO)
    except Exception as e:
        xbmc.log("Error executing " + autoexec_script + ": " + str(e), xbmc.LOGERROR)
else:
    xbmc.log("No autoexec script found for user: " + username, xbmc.LOGINFO)
