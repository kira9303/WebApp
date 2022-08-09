from django.db import models

# Create your models here.


assigned = "ASSIGNED"
in_prog = "IN_PROGRESS"
under_rev = "UNDER_REVIEW"
done = "DONE"

status_choice = (
    (assigned, "assigned"),
    (in_prog, "in_progress"),
    (under_rev, "under_review"),
    # ....
    (done, "done"),
)


class User(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=25)
    email = models.EmailField()
    password = models.CharField(max_length=40)

    def __str__(self):
        return self.username

    def _ret_email(self):
        return self.email

    def _ret_pass(self):
        return self.password



class Team(models.Model):
    id = models.IntegerField(primary_key=True)
    team_name = models.CharField(max_length=30)
    team_leader = models.CharField(max_length=20)
    team_members = models.IntegerField()

    def __str__(self):
        return self.team_name


#id, name, team, team members, status, started_at, completed_at)


class Task(models.Model):
    id = models.IntegerField(primary_key=True)
    task_name = models.CharField(max_length=30)
    team_name = models.CharField(max_length=20)
    status = models.CharField(max_length=30, choices=status_choice, default="IN_PROGRESS")
    started_at = models.DateTimeField()
    completed_at = models.DateTimeField()

    def __str__(self):
        return self.name

    def ret_status(self):
        return self.status

    def ret_team_name(self):
        return self.team_name

    def ret_started_at(self):
        return self.started_at

    def completed_at(self):
        return self.completed_at




