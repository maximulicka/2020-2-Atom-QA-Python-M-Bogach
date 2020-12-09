from locust import HttpUser, task, between, TaskSet
import json


class Scenario1(TaskSet):

    def on_start(self):
        r = self.client.get("/", auth=('max', 111))
        self.client.headers.update({'Authorization': r.request.headers.get('Authorization')})
        assert 200 == r.status_code

    def on_stop(self):
        self.client.get("/logout")

    @task
    def profile(self):
        self.client.get("/profile")

    @task
    def message(self):
        self.client.get("/message")


class Scenario2(TaskSet):

    def on_start(self):
        r = self.client.get("/", auth=('julia', 222))
        self.client.headers.update({'Authorization': r.request.headers.get('Authorization')})
        assert 200 == r.status_code

    def on_stop(self):
        self.client.get("/logout")

    @task
    def profile(self):
        self.client.get("/profile")

    @task
    def sport_team(self):
        self.client.get("/sport_team")


class Scenario3(TaskSet):

    def on_start(self):
        r = self.client.get("/", auth=('boris', 333))
        self.client.headers.update({'Authorization': r.request.headers.get('Authorization')})
        assert 200 == r.status_code

    def on_stop(self):
        self.client.get("/logout")

    @task
    def index(self):
        self.client.get("/")

    @task
    def post_method(self):
        data = {'name': 'Milan', 'Country': 'Italy', 'Stadium': 'San Siro', 'price_team': '500 million $'}
        self.client.post("/sport_team", data=json.dumps(data))


class WebSiteUser(HttpUser):
    tasks = [Scenario1, Scenario2, Scenario3]
    wait_time = between(1, 2)
