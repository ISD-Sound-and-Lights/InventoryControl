from htmlify import *

print("Content-Type: text/html;charset=utf-8")
print()

# head
dispHTML("head", contents=getHTML("script", src="https://use.fontawesome.com/344eca865b.js"))

def showHeader(loggedIn=False):
	# Title and menu
	title = getHTML("h1", "InventoryControl")  # title
	menuItemHome = getHTML("li", contents=getHTML("a", contents="Home", href="/cgi-bin/ic/main.py"))  # menu item 1 -- Home
	menuItemHelp = getHTML("li", contents=getHTML("a", contents="Help", href="/help"))  # menu item 2 -- Help
	if not loggedIn:
		menuItemLogin = getHTML("li", contents=getHTML("a", contents="Login", href="/cgi-bin/ic/login.py"))  # menu item 3 -- Login
	else:
		menuItemLogin = getHTML("li", contents=getHTML("a", contents="Logout", href="/cgi-bin/ic/logout.py"))  # menu item 3 -- Logout
	menu = menuItemHome + menuItemHelp + menuItemLogin  # construct a menu but don't output yet
	menu = getHTML("div", contents=menu, id="menu")  # put menu into a div id="menu"
	header = title + menu  # get a header; don't oput yet.
	dispHTML("div", contents=header, id="header")  # put header into div and oput
	dispHTML("hr")
	dispHTML("br")