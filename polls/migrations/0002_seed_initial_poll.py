from django.db import migrations
from django.utils import timezone


def seed_poll(apps, schema_editor):
    Question = apps.get_model("polls", "Question")
    Choice = apps.get_model("polls", "Choice")

    if not Question.objects.filter(question_text="What's up?").exists():
        q = Question.objects.create(
            question_text="What's up?",
            pub_date=timezone.now(),
        )
        Choice.objects.create(question=q, choice_text="Not much", votes=0)
        Choice.objects.create(question=q, choice_text="The sky", votes=0)


def unseed_poll(apps, schema_editor):
    Question = apps.get_model("polls", "Question")
    Question.objects.filter(question_text="What's up?").delete()


class Migration(migrations.Migration):
    dependencies = [
        ("polls", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(seed_poll, unseed_poll),
    ]
