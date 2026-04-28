param(
    # Required string
    [Parameter(Mandatory=$true)]
    [string]$Name,

    # Validated string choices
    [Parameter(Mandatory=$false)]
    [ValidateSet('development', 'staging', 'production')]
    [string]$Environment = 'development',

    # Validated build configuration
    [Parameter(Mandatory=$false)]
    [ValidateSet('Debug', 'Release')]
    [string]$Configuration = 'Release',

    # Integer with a default
    [Parameter(Mandatory=$false)]
    [int]$Retries = 3,

    # Float/double
    [Parameter(Mandatory=$false)]
    [double]$Threshold = 0.75,

    # String array
    [Parameter(Mandatory=$false)]
    [string[]]$Tags,

    # Boolean flags
    [switch]$Verbose,
    [switch]$DryRun
)

Write-Host "Name:          $Name"
Write-Host "Environment:   $Environment"
Write-Host "Configuration: $Configuration"
Write-Host "Retries:       $Retries"
Write-Host "Threshold:     $Threshold"
Write-Host "Tags:          $($Tags -join ', ')"
Write-Host "Verbose:       $Verbose"
Write-Host "Dry run:       $DryRun"

if ($DryRun) {
    Write-Host "[DRY RUN] No changes were made."
}
