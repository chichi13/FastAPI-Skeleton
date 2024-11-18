from locust import HttpUser, task


class QuickstartUser(HttpUser):
    @task
    def get_health(self):
        self.client.get(
            f"/api/v1/health"
        )
