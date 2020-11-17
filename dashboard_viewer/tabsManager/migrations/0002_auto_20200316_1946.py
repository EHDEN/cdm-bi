# Generated by Django 2.2.7 on 2020-03-16 19:46

import django.db.models.deletion
from django.db import migrations, models


def move_tabs_to_buttons(apps, schema_editor):
    Button = apps.get_model("tabsManager", "Button")
    Tab = apps.get_model("tabsManager", "Tab")

    for tab in Tab.objects.all():
        Button(
            title=tab.title,
            icon=tab.icon,
            position=tab.position,
            visible=tab.visible,
        ).save()


def associate_tab_and_button(apps, schema_editor):
    Button = apps.get_model("tabsManager", "Button")
    Tab = apps.get_model("tabsManager", "Tab")

    for tab in Tab.objects.all():
        button = Button.objects.get(title=tab.title)
        tab.button_ptr = button
        tab.save()


class Migration(migrations.Migration):

    dependencies = [
        ("tabsManager", "0002_auto_20200214_1128"),
    ]

    operations = [
        migrations.CreateModel(
            name="Button",
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
                    "title",
                    models.CharField(
                        help_text="Text to appear on the tab under the icon",
                        max_length=30,
                        unique=True,
                    ),
                ),
                (
                    "icon",
                    models.CharField(
                        help_text="Font awesome icon v5. Just the end part, e.g. fa-clock-o -> clock-o",
                        max_length=20,
                    ),
                ),
                ("position", models.IntegerField()),
                (
                    "visible",
                    models.BooleanField(help_text="If the tab should be displayed"),
                ),
            ],
        ),
        migrations.RunPython(move_tabs_to_buttons),
        migrations.RemoveField(
            model_name="tab",
            name="icon",
        ),
        migrations.RemoveField(
            model_name="tab",
            name="position",
        ),
        migrations.RemoveField(
            model_name="tab",
            name="visible",
        ),
        migrations.AddField(
            model_name="tab",
            name="button_ptr",
            field=models.OneToOneField(
                auto_created=True,
                default=None,
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                parent_link=True,
                serialize=False,
                to="tabsManager.Button",
            ),
            preserve_default=False,
        ),
        migrations.RunPython(associate_tab_and_button),
        migrations.RemoveField(
            model_name="tab",
            name="id",
        ),
        migrations.AlterField(
            model_name="tab",
            name="button_ptr",
            field=models.OneToOneField(
                auto_created=True,
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                primary_key=True,
                parent_link=True,
                serialize=False,
                to="tabsManager.Button",
            ),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name="tab",
            name="title",
        ),
        migrations.CreateModel(
            name="TabGroup",
            fields=[
                (
                    "button_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="tabsManager.Button",
                    ),
                ),
            ],
            bases=("tabsManager.button",),
        ),
        migrations.AddField(
            model_name="tab",
            name="group",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="tabsManager.TabGroup",
            ),
        ),
    ]