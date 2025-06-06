import os
import time
from playwright.sync_api import sync_playwright
from pyvirtualdisplay import Display

# Config
COOKIES_FILE = "/cookies/cookies.txt"
YOUTUBE_URL = "https://youtube.com"
PROFILE_DIR = "/profile"
EXPORT_INTERVAL = int(os.environ.get("EXPORT_INTERVAL_MINUTES", 60))

def export_cookies():
    with sync_playwright() as p:
        browser = p.chromium.launch_persistent_context(
            PROFILE_DIR, headless=True, args=["--no-sandbox"]
        )
        page = browser.new_page()
        page.goto(YOUTUBE_URL)
        time.sleep(10)  # Wait for page load/login if needed

        cookies = browser.cookies()
        with open(COOKIES_FILE, "w") as f:
            f.write("# Netscape HTTP Cookie File\n")
            for c in cookies:
                f.write(
                    "\t".join([
                        c.get("domain", ""),
                        "TRUE" if c.get("domain", "").startswith(".") else "FALSE",
                        c.get("path", "/"),
                        "TRUE" if c.get("secure", False) else "FALSE",
                        str(int(c.get("expires", 0))),
                        c.get("name", ""),
                        c.get("value", ""),
                    ]) + "\n"
                )
        browser.close()
        print("Cookies exported.")

def run_loop():
    while True:
        try:
            export_cookies()
        except Exception as e:
            print("Cookie export error:", e)
        print(f"Sleeping for {EXPORT_INTERVAL} min...")
        time.sleep(EXPORT_INTERVAL * 60)

if __name__ == "__main__":
    # On first run, you may want to run with headless=False and DISPLAY for login!
    # If not using a real display, use Xvfb/pyvirtualdisplay:
    display = Display(visible=0, size=(1024, 768))
    display.start()
    run_loop()
