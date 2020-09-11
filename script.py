
import webbrowser as wb

def webAuto():
    # copy and past your google chrome browser
    chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"

    # list of urls that's you want to open
    urls = [
        "w3schools.com",
        "python.org",
        "blender.org",
        "github.com"
    ]

    # loop through urls list and open them in chrome browser
    for url in urls:
        print("Opening this :", url)
        wb.get(chrome_path).open(url)

# call web automation function
webAuto()