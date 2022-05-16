from user import User
from post import Post
app_user_one = User("kirik", "kirik@gmail.com", "123", "devops")  #Object of class User
app_user_one.get_user_info()

# app_user_one.change_job_title("Devops Engineer")
# app_user_one.get_user_info()

app_user_two = User("abcd", "abcdk@gmail.com", "123", "sre") 
app_user_two.get_user_info()

new_post = Post("On a secret mission today", app_user_two.name)
new_post.get_post_info()