from utilities.choices import ChoiceSet

class ValidationTypeChoices(ChoiceSet):
    key = 'ValidationResult.types'

    V0010_DNS_VALIDATION = 'DNS Validation'
    V0020_AAA_VALIDATION = 'AAA Validation'
    V0030_COLLECTOR_VALIDATION = 'Cisco Collector Validation'
    V0040_LICENSING_VALIDATION = 'Licensing Validation'
    V0050_MONITORING_VALIDATION = 'Monitoring Validation'
    V0060_BACKUP_VALIDATION = 'Backup Validation'
    V0070_NAC_HEALTH_VALIDATION = 'NAC Validation'
    V0080_CONFIG_HEALTH_VALIDATION = 'Config Health Validation'
    V0090_SUPPORT_CONTRACT_VALIDATION = 'Support Contract Validation'

    CHOICES = [
        (V0010_DNS_VALIDATION, 'DNS Validation'),
        (V0020_AAA_VALIDATION, 'AAA Validation'),
        (V0030_COLLECTOR_VALIDATION, 'Cisco Collector Validation'),
        (V0040_LICENSING_VALIDATION, 'Licensing Validation'),
        (V0050_MONITORING_VALIDATION, 'Monitoring Validation'),
        (V0060_BACKUP_VALIDATION, 'Backup Validation'),
        (V0070_NAC_HEALTH_VALIDATION, 'NAC Validation'),
        (V0080_CONFIG_HEALTH_VALIDATION, 'Config Health Validation'),
        (V0090_SUPPORT_CONTRACT_VALIDATION, 'Support Contract Validation'),
    ]
