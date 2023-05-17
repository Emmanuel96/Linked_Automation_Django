from django.shortcuts import render
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from django.http import HttpResponse
import time
import logging
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options

logger = logging.getLogger("django")


# Create your views here.
def apply(request):
    if request.method == "POST":
        username = request.POST.get("email")
        password = request.POST.get("password")

        chrome_options = Options()
        chrome_options.add_argument("--headless")

        driver = webdriver.Chrome(options=chrome_options)
        driver.get("https://www.linkedin.com")
        time.sleep(5)
        # Automate email and password input
        email = driver.find_element(By.ID, "session_key")
        pass1 = driver.find_element(By.ID, "session_password")
        email.send_keys(username)
        pass1.send_keys(password)

        submit = driver.find_element(
            By.CLASS_NAME, "sign-in-form__submit-btn--full-width"
        ).click()
        time.sleep(60)
        # Get search bar
        search = driver.find_element(By.CLASS_NAME, "search-global-typeahead__input")
        # add input
        search.send_keys("Python Developer")
        search.send_keys(Keys.ENTER)
        time.sleep(10)

        primary_filter = driver.find_element(By.ID, "search-reusables__filters-bar")
        primary_filter_ul = primary_filter.find_element(By.TAG_NAME, "ul")
        primary_filter_li = primary_filter_ul.find_elements(
            By.CLASS_NAME, "search-reusables__primary-filter"
        )
        people = primary_filter_li[0]
        people.click()
        time.sleep(10)

        all_jobs = driver.find_elements(By.CSS_SELECTOR, ".job-card-container--clickable")
        for job in all_jobs:
            print(job.text)
            job.click()
            time.sleep(10)
            try:
                apply_button = driver.find_element(By.CSS_SELECTOR, ".jobs-apply-button--top-card")
                apply_button.click()
                time.sleep(5)
                next = driver.find_element(By.CSS_SELECTOR, "footer button")
                next.click()
                time.sleep(5)
                review = driver.find_element(By.CLASS_NAME, "artdeco-button--primary")
                if review.get_attribute("data-control-name") == "continue unify":
                    close = driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss")
                    close.click()
                    time.sleep(5)
                    discard = driver.find_elements(
                    By.CLASS_NAME, "artdeco-modal__confirm-dialog-btn"
                    )[1]
                    discard.click()
                    print("ooop!!!")
                    continue
                else:
                    review.click()
                    time.sleep(5)
                    submitbtn = driver.find_element(By.CLASS_NAME, "artdeco-button--primary")
                    if submitbtn.get_attribute("data-control-name") == "submit_unify":
                        submitbtn.click()
                        time.sleep(5)
                        close = driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss")
                        close.click()
                    else:
                        close = driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss")
                        close.click()
                    time.sleep(5)
                    discard = driver.find_elements(
                    By.CLASS_NAME, "artdeco-modal__confirm-dialog-btn"
                    )[1]
                    discard.click()
                    print("ooop!!!")
                    continue
            except NoSuchElementException:
                print("No such element")
                continue

        try:
            name_element = driver.find_element(By.CLASS_NAME, "global-nav__me-photo")
            name = name_element.get_attribute("alt")
            response = f"Login successful. Welcome {name}!"
        except:
            response = "Login failed. Please check your credentials."

        # Close the web driver
        driver.quit()

        # Return the response to the client
        return HttpResponse(response)
    return render(request, "apply.html")


def connect(request):
    if request.method == "POST":
        username = request.POST.get("email")
        password = request.POST.get("password1")

        # chrome_options = Options()
        # chrome_options.add_argument("--headless")

        driver = webdriver.Chrome()
        driver.get("https://www.linkedin.com")
        time.sleep(5)
        # Automate email and password input
        email = driver.find_element(By.ID, "session_key")
        pass1 = driver.find_element(By.ID, "session_password")
        email.send_keys(username)
        pass1.send_keys(password)

        submit = driver.find_element(
            By.CLASS_NAME, "sign-in-form__submit-btn--full-width"
        ).click()

        search = driver.find_element(By.CLASS_NAME, "search-global-typeahead__input")
        # add input
        search.send_keys("Software Engineer")
        search.send_keys(Keys.ENTER)
        time.sleep(10)

        primary_filter = driver.find_element(By.ID, "search-reusables__filters-bar")
        primary_filter_ul = primary_filter.find_element(By.TAG_NAME, "ul")
        primary_filter_li = primary_filter_ul.find_elements(
            By.CLASS_NAME, "search-reusables__primary-filter"
        )
        people = primary_filter_li[0].click()
        time.sleep(10)

        # people_ul = driver.find_element(By.TAG_NAME, "ul")
        people = driver.find_elements(
            By.CLASS_NAME, "reusable-search__result-container"
        )
        p = []
        for person in people:
            p.append(person.text)
            print(person.text)
            person.find_element(By.TAG_NAME, "button").click()
            time.sleep(2)
            modal = driver.find_element(By.CLASS_NAME, "artdeco-modal-overlay")
            send = modal.find_element(By.CLASS_NAME, "artdeco-button--primary")
            send.click()

        try:
            name_element = driver.find_element(By.CLASS_NAME, "global-nav__me-photo")
            name = name_element.get_attribute("alt")
            response = f"Login successful. Welcome {name}!\n{p}"
        except:
            response = "Login failed. Please check your credentials."

        # Close the web driver
        driver.quit()

        # Return the response to the client
        return HttpResponse(response)
    context = {}
    return render(request, "connect.html", context)


def home(request):
    context = {}
    return render(request, "home.html", context)
