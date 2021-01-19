from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


RATE_VALIDATION = (MinValueValidator(1), MaxValueValidator(10))


class ActiveQuerySet(models.QuerySet):
    """
    ActivatorQuerySet

    Query set that returns statused results
    """

    def active(self):
        """ Return active query set """
        return self.filter(is_active=True, is_deleted=False)

    def inactive(self):
        """ Return inactive query set """
        return self.filter(is_active=False, is_deleted=False)


class ActiveModelManager(models.Manager):
    """
    ActiveModelManager

    Manager to return instances of ActivatorModel: SomeModel.objects.active() / .inactive()
    """

    def get_queryset(self):
        """ Use ActiveQuerySet for all results """
        return ActiveQuerySet(model=self.model, using=self._db)

    def active(self):
        """
        Return active instances of BaseModel:

        SomeModel.objects.active(), proxy to ActiveQuerySet.active
        """
        return self.get_queryset().active()

    def inactive(self):
        """
        Return inactive instances of BaseModel:

        SomeModel.objects.inactive(), proxy to ActiveQuerySet.inactive
        """
        return self.get_queryset().inactive()


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True, editable=False)

    objects = models.Manager()
    active_objects = ActiveModelManager()

    class Meta:
        abstract = True

    def soft_delete(self, force_save=True):
        self.is_deleted = True
        if force_save:
            self.save()

    def un_soft_delete(self, force_save=True):
        self.is_deleted = False
        if force_save:
            self.save()
