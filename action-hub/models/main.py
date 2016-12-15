from django.db import models
from django.db.models import permalink
from django.contrib.auth.models import User
from django.urls import reverse
from django.template.defaultfilters import slugify
#CKEditor
from ckeditor.fields import RichTextField

from .pod import Pod
from .coalition import Coalition
