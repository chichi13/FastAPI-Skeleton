from locust import HttpUser, between, task

jwt_token = ""


class QuickstartUser(HttpUser):
    wait_time = between(1, 4)

    @task
    def get_all_users(self):
        self.client.get(
            f"/api/v1/health"
        )