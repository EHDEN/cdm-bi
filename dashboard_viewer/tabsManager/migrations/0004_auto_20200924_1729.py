# Generated by Django 2.2.16 on 2020-09-24 17:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("tabsManager", "0003_logo"),
    ]

    operations = [
        migrations.RenameField(
            model_name="logo",
            old_name="imageContainerCss",
            new_name="image_container_css",
        ),
        migrations.RenameField(
            model_name="logo",
            old_name="imageCss",
            new_name="image_css",
        ),
        migrations.RenameField(
            model_name="logo",
            old_name="imageOnHoverCss",
            new_name="image_on_hover_css",
        ),
    ]