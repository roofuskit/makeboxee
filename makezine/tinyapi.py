import mc
import urllib

def search():
    term = mc.ShowDialogKeyboard("Search for:", "", False)
    mc.ShowDialogWait()
    url = "%s%s%s" % ("http://pipes.yahoo.com/pipes/pipe.run?Search=", term, "&_id=acacaff9768ad4f22e06b0644879a6b1&_render=rss")
    quoted = urllib.quote_plus(url)
    apiurl = "http://tinyurl.com/api-create.php?url="
    tinyurl = urllib.urlopen(apiurl + quoted).read()
    mc.GetActiveWindow().GetList(1000).SetContentURL(tinyurl)
    mc.HideDialogWait()
    return tinyurl

