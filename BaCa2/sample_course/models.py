from django.db import models

import course.models as c

DB = 'sample_course'


class Round(c.Round):
    use_db = DB


class Task(c.Task):
    use_db = DB


class TestSet(c.TestSet):
    use_db = DB


class Test(c.Test):
    use_db = DB


class Submit(c.Submit):
    use_db = DB


class Result(c.Result):
    use_db = DB