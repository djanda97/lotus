# Generated by Django 4.0.5 on 2023-02-14 06:33

from django.db import migrations


def copy_events_to_idempotencecheck(apps, schema_editor):
    Event = apps.get_model("metering_billing", "Event")
    IdempotenceCheck = apps.get_model("metering_billing", "IdempotenceCheck")

    for event in Event.objects.order_by(
        "idempotency_id", "organization", "-time_created"
    ).values("time_created", "idempotency_id", "organization"):
        idempotency_check, created = IdempotenceCheck.objects.get_or_create(
            idempotency_id=event["idempotency_id"],
            organization=event["organization"],
        )
        if created or not idempotency_check.time_created:
            idempotency_check.time_created = event["time_created"]
            idempotency_check.save()


class Migration(migrations.Migration):
    dependencies = [
        ("metering_billing", "0179_idempotencecheck_and_more"),
    ]

    operations = [
        migrations.RunPython(
            copy_events_to_idempotencecheck, reverse_code=migrations.RunPython.noop
        ),
    ]