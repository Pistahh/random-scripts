import os

CUSTOM_CSS = """
@namespace url("http://www.mozilla.org/keymaster/gatekeeper/there.is.only.xul");

/* to hide the native tabs */
#TabsToolbar {
    visibility: collapse;
}

/* to hide the sidebar header */
#sidebar-header {
    visibility: collapse;
}
"""

profiledir = os.path.join(os.getenv('APPDATA'), 'Mozilla', 'Firefox', 'Profiles')
for profile in os.listdir(profiledir):
    dname = os.path.join(profiledir, profile, 'chrome')
    fname = os.path.join(dname, "userChrome.css")
    try:
        os.mkdir(dname)
    except FileExistsError:
        pass
    try:
        with open(fname, "x") as f:
            f.write(CUSTOM_CSS)
            print("Created {}".format(fname))
    except FileExistsError:
            print("Already there, not updating: {}".format(fname))