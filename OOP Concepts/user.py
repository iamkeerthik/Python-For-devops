class User:
    def __init__(self, uname, email, password, current_job):
        self.name =  uname
        self.email = email
        self.password = password
        self.current_job_title = current_job
    
    def change_passwd(self, new_password):
        self.password = new_password

    def change_job_title(self, new_job): #functions belongs to  classes are called as methods
        self.current_job_title=new_job

    def get_user_info(self):
        print(f'user {self.name} currently working as a {self.current_job_title}, you can contact them at {self.email}')

