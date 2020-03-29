
from django.db import models
from django.db.models.signals import post_save, post_delete

class Country(models.Model):
    class Meta:
        db_table = "country"
        ordering = ("country",)
    country   = models.CharField(
        max_length = 100,
        unique = True,
        help_text = "Country name."
    )
    continent = models.CharField(
        max_length = 50,
        help_text = "Continent associated."
    )

    def __str__(self):
        return f"{self.country}"

    def __repr__(self):
        return self.__repr__()


class DatabaseType(models.Model):
    class Meta:
        db_table = "database_type"

    type = models.CharField(
        max_length=40,
        unique=True,
        help_text="Defines the database type."
    )

    def __str__(self):
        return self.type

    def __repr__(self):
        return self.__str__()

#Not following the relational rules in the database_type field, but it will simplify the SQL queries in the SQL Lab
class DataSource(models.Model):
    class Meta:
        db_table = "data_source"

    name            = models.CharField(
        max_length  = 40,
        unique      = True,
        help_text   = "Name of the data source."
    )
    slug            = models.SlugField(
        max_length  = 50,
        unique      = True,
        help_text   = "Short label for the data source, containing only letters, numbers, underscores or hyphens."
    )
    release_date    = models.DateField(
        help_text   = "Date at which DB is available for research for current release."
    )
    database_type   = models.CharField(
        max_length  = 40,
        help_text   = "Type of the data source. You can create a new type."
    )
    country         = models.ForeignKey(
        Country,
        on_delete   = models.SET_NULL,
        null        = True,
        help_text   = "Country where the data source is located.",
    )
    latitude        = models.FloatField()
    longitude       = models.FloatField()
    link            = models.URLField(
        help_text   = "Link to home page of the data source",
        blank       = True
    )

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()


def after_data_source_saved(sender, **kwargs):
    """
    TODO After a data source is inserted dashboards on superset might need to be updated
    """
    pass


post_save.connect(after_data_source_saved, sender=DataSource)


def after_data_source_deleted(sender, **kwargs):
    """
    TODO After a data source is deleted dashboards on superset might need to be updated
    """
    pass


post_delete.connect(after_data_source_deleted, sender=DataSource)


class UploadHistory(models.Model):
    class Meta:
        ordering = ("-upload_date",)
        db_table = "upload_history"

    data_source              = models.ForeignKey(DataSource, on_delete=models.CASCADE)
    upload_date              = models.DateTimeField()
    achilles_version         = models.CharField(max_length=10)
    achilles_generation_date = models.DateField()
    cdm_version              = models.CharField(max_length=10)
    vocabulary_version       = models.CharField(max_length=10)


class AchillesResults(models.Model):
    class Meta:
        db_table = "achilles_results"
        indexes = [
            models.Index(fields=("data_source",)),
            models.Index(fields=("analysis_id",))
        ]

    data_source = models.ForeignKey(DataSource, on_delete=models.CASCADE)
    analysis_id = models.BigIntegerField()
    stratum_1   = models.TextField()
    stratum_2   = models.TextField()
    stratum_3   = models.TextField()
    stratum_4   = models.TextField()
    stratum_5   = models.TextField()
    count_value = models.BigIntegerField()


class AchillesResultsArchive(models.Model):
    class Meta:
        db_table = "achilles_results_archive"
        indexes = [
            models.Index(fields=("data_source",)),
            models.Index(fields=("analysis_id",))
        ]

    upload_info = models.ForeignKey(UploadHistory, on_delete=models.CASCADE)
    data_source = models.ForeignKey(DataSource, on_delete=models.CASCADE)
    analysis_id = models.BigIntegerField()
    stratum_1   = models.TextField()
    stratum_2   = models.TextField()
    stratum_3   = models.TextField()
    stratum_4   = models.TextField()
    stratum_5   = models.TextField()
    count_value = models.BigIntegerField()

