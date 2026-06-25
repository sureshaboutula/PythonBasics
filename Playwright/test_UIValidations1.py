from playwright.sync_api import Page, expect


def test_UiValidationDynamicScript(page:Page):
    # iPhone X, Nokia Edge -> verify 2 items are showing in cart
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("Learning@830$3mK2")
    page.get_by_role("combobox").select_option("consult")
    # page.get_by_role("checkbox").click()
    page.locator("#terms").check()
    page.get_by_role("link", name="terms and conditions").click()
    page.get_by_role("button", name="Sign In").click()
    iphoneXProduct = page.locator("app-card").filter(has_text="iphone X")
    iphoneXProduct.get_by_role("button").click()
    NokiaEdgeProduct = page.locator("app-card").filter(has_text="Nokia Edge")
    NokiaEdgeProduct.get_by_role("button").click()
    page.get_by_text("Checkout").click()
    expect(page.locator(".media-body")).to_have_count(2)

def test_childWindowHandle(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")

    with page.expect_popup() as newPage_info:
        page.locator(".blinkingText").filter(has_text="Free Access to InterviewQues/ResumeAssistance/Material").click() # new page
        childPage = newPage_info.value
        text = childPage.locator(".red").text_content()
        #print(text)
        email = text.split("at ")[1].split(" ")[0] #email = text.split("at ")[1].split(" ")[0].strip()
        #print(word)
        assert email == "mentor@rahulshettyacademy.com"



