def print_func_name(function_name, *args):
    function_name = function_name.__name__.replace('_', ' ').capitalize()
    print(f'\nИмя функции: {function_name}. Аргументы функции: ')

    for arg in args:
        print(arg)

def open_browser(browser_name):
    print_func_name(open_browser, browser_name)


def go_to_companyname_homepage(page_url):
    print_func_name(go_to_companyname_homepage, page_url)


def find_registration_button_on_login_page(page_url, button_text):
    print_func_name(find_registration_button_on_login_page, page_url, button_text)

open_browser("Chrome")
go_to_companyname_homepage("https://google.com/ncr")
find_registration_button_on_login_page("https://google.com/ncr", "Поиск в Google")