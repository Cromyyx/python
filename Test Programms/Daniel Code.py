from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Instagram account credentials with unique comments
accounts = [
    {"username": "kuchenkuch07", "password": ",katia1,", "comment": "Great post! Keep it up! @daniell.copy"},
]

# Target Instagram account
target_account = "d_a_n_i_e_l_270"  # Replace with the account you want to monitor

# Path to ChromeDriver
service = Service(r"C:\Users\thoma\Documents\msedgedriver.exe")
driver = webdriver.Edge(service=service)

def login(username, password):
    """Log in to Instagram with the given credentials."""
    driver.get("https://www.instagram.com/accounts/login/")
    time.sleep(3)
    driver.find_element(By.NAME, "username").send_keys(username)
    driver.find_element(By.NAME, "password").send_keys(password + Keys.RETURN)
    time.sleep(5)

def get_latest_post():
    """Return the unique identifier (URL) for the latest post on the target account."""
    driver.get(f"https://www.instagram.com/{target_account}/")
    try:
        # Wait for the latest post element to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a[href*='/p/']"))
        )
        latest_post_element = driver.find_element(By.CSS_SELECTOR, "a[href*='/p/']")
        if latest_post_element:
            latest_post = latest_post_element.get_attribute('href')
            print(f"Latest post URL: {latest_post}")
            return latest_post
        else:
            print("No post found.")
            return None
    except Exception as e:
        print(f"Error locating the latest post: {e}")
        return None

def comment_on_post(account_comment, post_url):
    """Navigate to the post and comment."""
    driver.get(post_url)
    try:
        # Wait for the comment box to load
        comment_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "textarea"))
        )
        # Click to activate the comment box
        comment_box.click()
        time.sleep(1)  # Wait a moment after clicking
        # Type the comment
        comment_box.send_keys(account_comment)
        time.sleep(1)  # Wait to simulate human typing
        # Submit the comment
        comment_box.send_keys(Keys.RETURN)
        print(f"Comment posted: {account_comment}")
        time.sleep(2)
    except Exception as e:
        print(f"Error posting comment: {e}")

# Log in with the first account to monitor the target profile
login(accounts[0]["username"], accounts[0]["password"])

# Monitor the account until a new post is detected
print("Waiting for a new post...")
last_post = get_latest_post()

while True:
    try:
        current_post = get_latest_post()
        if current_post != last_post and current_post is not None:  # Check if a new post is detected
            print(f"New post detected: {current_post}")
            for account in accounts:
                # Log in with each account and comment
                login(account["username"], account["password"])
                comment_on_post(account["comment"], current_post)
                driver.delete_all_cookies()  # Log out before switching accounts
            break  # Exit the loop once all accounts have commented
        else:
            print("No new post detected.")
        time.sleep(5)  # Wait before checking again
    except Exception as e:
        print(f"Error: {e}")
        time.sleep(5)  # Retry after a short delay

print("All comments posted. Exiting.")
driver.quit()
