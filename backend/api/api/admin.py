from django.contrib import admin
from .models.admin import Admin
from .models.course import Course
from .models.course_material import CourseMaterial
from .models.learner import Learner

admin.site.register([Admin, Course, Learner, CourseMaterial])