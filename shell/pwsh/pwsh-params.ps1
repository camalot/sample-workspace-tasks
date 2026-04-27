param(
    [Parameter(Mandatory=$true)]
    [string]$Environment,

    [Parameter(Mandatory=$false)]
    [ValidateSet('Debug','Release')]
    [string]$Configuration = 'Release',

    [switch]$DryRun
)

Write-Host "Running tests in $Environment environment with $Configuration configuration."
