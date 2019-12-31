from locust import HttpLocust, TaskSet, task, between

class UserBehavior(TaskSet):
    @task(2)
    def index(self):
        self.client.get("/users/")

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    wait_time = between(0.1,0.1)
