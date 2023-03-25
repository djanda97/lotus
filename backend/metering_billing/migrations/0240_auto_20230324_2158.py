# Generated by Django 4.0.5 on 2023-03-24 21:58

from django.db import migrations


def transfer_org_settings(apps, schema_editor):
    OrganizationSetting = apps.get_model("metering_billing", "OrganizationSetting")
    for org_setting in OrganizationSetting.objects.filter(
        setting_name="generate_customer_after_creating_in_lotus"
    ):
        organization = org_setting.organization
        organization.gen_cust_in_stripe_after_lotus = org_setting.setting_values[
            "value"
        ]
        organization.save()
    for org_setting in OrganizationSetting.objects.filter(
        setting_name="gen_cust_in_braintree_after_lotus"
    ):
        organization = org_setting.organization
        organization.gen_cust_in_braintree_after_lotus = org_setting.setting_values[
            "value"
        ]
        organization.save()
    for org_setting in OrganizationSetting.objects.filter(
        setting_name="payment_grace_period"
    ):
        organization = org_setting.organization
        organization.payment_grace_period = org_setting.setting_values["value"]
        organization.save()
    for org_setting in OrganizationSetting.objects.filter(
        setting_name="crm_customer_source"
    ):
        organization = org_setting.organization
        organization.lotus_is_customer_source_for_salesforce = (
            org_setting.setting_values["salesforce"]
        )
        organization.save()


class Migration(migrations.Migration):
    dependencies = [
        (
            "metering_billing",
            "0239_historicalorganization_gen_cust_in_braintree_after_lotus_and_more",
        ),
    ]

    operations = [
        migrations.RunPython(transfer_org_settings),
    ]