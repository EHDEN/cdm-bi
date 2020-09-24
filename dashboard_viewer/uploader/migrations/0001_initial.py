# Generated by Django 2.2.7 on 2020-02-12 14:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Country",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "country",
                    models.CharField(
                        help_text="Country name.", max_length=100, unique=True
                    ),
                ),
                (
                    "continent",
                    models.CharField(help_text="Continent associated.", max_length=50),
                ),
            ],
            options={
                "db_table": "country",
                "ordering": ("country",),
            },
        ),
        migrations.CreateModel(
            name="DatabaseType",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "type",
                    models.CharField(
                        help_text="Defines the database type.",
                        max_length=40,
                        unique=True,
                    ),
                ),
            ],
            options={
                "db_table": "database_type",
            },
        ),
        migrations.CreateModel(
            name="DataSource",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="Name of the data source.", max_length=40, unique=True
                    ),
                ),
                (
                    "slug",
                    models.SlugField(
                        help_text="Short label for the data source, containing only letters, numbers, underscores or hyphens.",
                        unique=True,
                    ),
                ),
                (
                    "release_date",
                    models.DateField(
                        help_text="Date at which DB is available for research for current release."
                    ),
                ),
                (
                    "database_type",
                    models.CharField(
                        help_text="Type of the data source. You can create a new type.",
                        max_length=40,
                    ),
                ),
                ("latitude", models.FloatField()),
                ("longitude", models.FloatField()),
                (
                    "link",
                    models.URLField(
                        blank=True, help_text="Link to home page of the data source"
                    ),
                ),
                (
                    "country",
                    models.ForeignKey(
                        help_text="Country where the data source is located.",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="uploader.Country",
                    ),
                ),
            ],
            options={
                "db_table": "data_source",
            },
        ),
        migrations.CreateModel(
            name="UploadHistory",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("upload_date", models.DateTimeField()),
                ("achilles_version", models.CharField(max_length=10)),
                ("achilles_generation_date", models.DateField()),
                ("cdm_version", models.CharField(max_length=10)),
                ("vocabulary_version", models.CharField(max_length=10)),
                (
                    "data_source",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="uploader.DataSource",
                    ),
                ),
            ],
            options={
                "db_table": "upload_history",
                "ordering": ("-upload_date",),
            },
        ),
        migrations.CreateModel(
            name="AchillesResultsArchive",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("analysis_id", models.BigIntegerField()),
                ("stratum_1", models.TextField()),
                ("stratum_2", models.TextField()),
                ("stratum_3", models.TextField()),
                ("stratum_4", models.TextField()),
                ("stratum_5", models.TextField()),
                ("count_value", models.BigIntegerField()),
                (
                    "data_source",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="uploader.DataSource",
                    ),
                ),
                (
                    "upload_info",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="uploader.UploadHistory",
                    ),
                ),
            ],
            options={
                "db_table": "achilles_results_archive",
            },
        ),
        migrations.CreateModel(
            name="AchillesResults",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("analysis_id", models.BigIntegerField()),
                ("stratum_1", models.TextField()),
                ("stratum_2", models.TextField()),
                ("stratum_3", models.TextField()),
                ("stratum_4", models.TextField()),
                ("stratum_5", models.TextField()),
                ("count_value", models.BigIntegerField()),
                (
                    "data_source",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="uploader.DataSource",
                    ),
                ),
            ],
            options={
                "db_table": "achilles_results",
            },
        ),
        migrations.AddIndex(
            model_name="achillesresultsarchive",
            index=models.Index(
                fields=["data_source"], name="achilles_re_data_so_4baf12_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="achillesresultsarchive",
            index=models.Index(
                fields=["analysis_id"], name="achilles_re_analysi_98b026_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="achillesresults",
            index=models.Index(
                fields=["data_source"], name="achilles_re_data_so_cc95c9_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="achillesresults",
            index=models.Index(
                fields=["analysis_id"], name="achilles_re_analysi_873019_idx"
            ),
        ),
    ]
