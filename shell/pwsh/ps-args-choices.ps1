param(
    # Required string constrained to a fixed set of values
    [Parameter(Mandatory=$true)]
    [ValidateSet('development', 'staging', 'production')]
    [string]$Environment,

    # Optional string with choices and a default
    [Parameter(Mandatory=$false)]
    [ValidateSet('Debug', 'Release')]
    [string]$Configuration = 'Release',

    # Optional int constrained to specific worker counts
    [Parameter(Mandatory=$false)]
    [ValidateSet(1, 2, 4, 8)]
    [int]$Workers = 4,

    # Optional string with log-level choices
    [Parameter(Mandatory=$false)]
    [ValidateSet('debug', 'info', 'warning', 'error', 'critical')]
    [string]$LogLevel = 'info'
)

Write-Host "Environment: $Environment"
Write-Host "Config:      $Configuration"
Write-Host "Workers:     $Workers"
Write-Host "Log level:   $LogLevel"
