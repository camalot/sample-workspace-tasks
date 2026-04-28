param(
    # Required string parameter
    [Parameter(Mandatory=$true)]
    [string]$Name,

    # Optional string parameter with a default value
    [Parameter(Mandatory=$false)]
    [string]$Environment = 'development',

    # Optional integer parameter with a default value
    [Parameter(Mandatory=$false)]
    [int]$Retries = 3,

    # Optional float/double parameter
    [Parameter(Mandatory=$false)]
    [double]$Threshold = 0.75,

    # Optional string parameter without a default
    [Parameter(Mandatory=$false)]
    [string]$OutputPath
)

Write-Host "Name:        $Name"
Write-Host "Environment: $Environment"
Write-Host "Retries:     $Retries"
Write-Host "Threshold:   $Threshold"
Write-Host "Output:      $(if ($OutputPath) { $OutputPath } else { '(not set)' })"
