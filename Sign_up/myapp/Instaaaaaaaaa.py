from selenium import webdriver
import time

users = ['Shyam', 'syamkumar_mc', 'shivapriyazz']

insta = webdriver.Chrome(
    executable_path='C:\chromedriver\chromedriver')

insta.maximize_window()

insta.get('https://www.instagram.com/')

time.sleep(2)

username_field = insta.find_element_by_name('username')
username_field.send_keys('space4868')

time.sleep(2)

password_field = insta.find_element_by_name('password')
password_field.send_keys('Photo@18oct')

time.sleep(2)

submit = insta.find_element_by_css_selector("button[type='submit'")
submit.click()

time.sleep(2)

for user in users:
    insta.get(f'https://www.instagram.com/{user}/')
    post, followers, following = insta.find_elements_by_class_name('g47SY')
    print(post.text, followers.text, following.text)

    bio = insta.find_element_by_class_name('-vDIg')
    print(bio.text)

    with open(f"{user}.txt", 'w')as file:
        file.write(
            f"Number Of Posts: {post.text}\nFollowers: {followers.text}\nFollowing: {following.text}\n\nBio: \n{bio.text}")

    time.sleep(1)

