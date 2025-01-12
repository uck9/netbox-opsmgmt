from utilities.choices import ChoiceSet

class OpsTaskTypeChoices(ChoiceSet):
    key = 'OpsTask.types'

    CURRENCY_UPGRADE = 'Version Currency Upgrade'
    VULN_UPGRADE = 'Vulnerability Upgrade'
    RELOAD_PLANNED = 'Reload - Planned'
    RELOAD_UNPLANNED = 'Reload - Unplanned'
    CONFIG_REVIEW = 'Configuration Review'
    CIRCUIT_OUTAGE_PLANNED = 'Circuit Outage - Planned'
    CIRCUIT_OUTAGE_UNPLANNED ='Circuit Outage - Unplanned'

    CHOICES = [
        (CURRENCY_UPGRADE, 'Version Currency Upgrade', 'green'),
        (VULN_UPGRADE, 'Vulnerability Upgrade', 'blue'),
        (RELOAD_PLANNED, 'Reload - Planned','orange'),
        (RELOAD_UNPLANNED, 'Reload - Unplanned', 'red'),
        (CONFIG_REVIEW, 'Configuration Review', 'aqua'),
        (CIRCUIT_OUTAGE_PLANNED, 'Circuit Outage - Planned', 'aqua'),
        (CIRCUIT_OUTAGE_UNPLANNED, 'Circuit Outage - Unplanned', 'aqua'),
    ]

class OpsTaskOutcomeChoices(ChoiceSet):
    key = 'OpsTask.outcomes'

    NO_ISSUES = 'No Unpexected Issues'
    ISSUES = 'Unexpected Issues'

    CHOICES = [
        (NO_ISSUES, 'No Unexpected Issues', 'green'),
        (ISSUES, 'Unexpected Issues', 'red'),
    ] 